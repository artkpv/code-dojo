#r "packages/Suave/lib/net461/Suave.dll"
#r "packages/Newtonsoft.Json/lib/net45/Newtonsoft.Json.dll"
#r "packages/Mono.Data.SQLite/lib/net40/Mono.Data.SQLite.dll"
#r "packages/SQLProvider/lib/net451/FSharp.Data.SQLProvider.dll"
#r "System.Transactions"

#load "Constants.fsx"

open System
open System.IO
open FSharp.Data.Sql
open Newtonsoft.Json
open Suave

let json smth = JsonConvert.SerializeObject smth

let ofJson<'a> str =
    try
        Some (JsonConvert.DeserializeObject<'a> str)
    with e ->
        do Console.Error.WriteLine e.Message
        None

module Crypto =
    open System.Numerics

    type RsaKey = { exp: int; modulo: int }

    type RsaConfig = { modulo: int; publicExp: int; privateExp: int }

    module RsaConfig =
        let toPublic config = { exp = config.publicExp; modulo = config.modulo }
        let toPrivate config = { exp = config.privateExp; modulo = config.modulo }

    let private getConfig path =
        if File.Exists path then
            File.ReadAllText path
            |> ofJson<RsaConfig>
        else
            None

    let config =
        match getConfig Constants.ConfigFilename with
        | Some config ->
            config
        | None ->
            failwithf "RSA config is expected to be in %s, but it is not" Constants.ConfigFilename

    let rsaEncode publicKey (message: string) =
        message
        |> Seq.collect (fun c ->
            let power = BigInteger.Pow (c |> int |> BigInteger, publicKey.exp) in
            publicKey.modulo
            |> BigInteger
            |> fun m -> power % m
            |> int32
            |> BitConverter.GetBytes)
        |> Seq.toArray
        |> Convert.ToBase64String

    let rsaDecode privateKey message =
        let bytes = Convert.FromBase64String message
        [|0 .. sizeof<int32> .. bytes.Length - 1|]
        |> Array.map (fun i ->
            let code = BitConverter.ToInt32 (bytes, i) |> BigInteger
            let power = BigInteger.Pow (code, privateKey.exp)
            privateKey.modulo
            |> BigInteger
            |> fun m -> power % m
            |> int32
            |> char)
        |> String.Concat

    let encode = config |> RsaConfig.toPublic |> rsaEncode

    let decode = config |> RsaConfig.toPrivate |> rsaDecode


type User = { id: Guid; username: string; password: string }

module Storage =
    type Database = SqlDataProvider<Common.DatabaseProviderTypes.SQLITE,
                                    Constants.ConnectionString>

    let dbContext = Database.GetDataContext ()

    let createUser username password =
        try
            let entity =
                dbContext.Main.Users.``Create(password, username)`` (password, username)
            let id = Guid.NewGuid ()
            do entity.Id <- string id
            do dbContext.SubmitUpdates ()
            Some { id = id;
                   username = username;
                   password = password }
        with e ->
            do Console.Error.WriteLine e.Message
            None

    let findUser userId =
        query { for user in dbContext.Main.Users do
                where (user.Id = userId)
                select { id = Guid.Parse user.Id;
                         username = user.Username;
                         password = user.Password } }
        |> Seq.tryHead

    let findUserByName username =
        query { for user in dbContext.Main.Users do
                where (user.Username = username)
                select { id = Guid.Parse user.Id;
                         username = user.Username;
                         password = user.Password } }
        |> Seq.tryHead

    let createData data userId =
        try
            let entity =
                dbContext.Main.UserData.``Create(data, userId)``(data, userId)
            do dbContext.SubmitUpdates ()
            Some entity.Id
        with e ->
            do Console.Error.WriteLine e.Message
            None

    let findData dataId userId =
        query { for data in dbContext.Main.UserData do
                where (data.Id = dataId && data.UserId = userId)
                select data.Data }
        |> Seq.tryHead

    let getUserData userId =
        query { for data in dbContext.Main.UserData do
                where (data.UserId = userId)
                select data.Id }
        |> Seq.toList

module Endpoint =
    open Suave
    open Suave.Filters
    open Suave.Operators

    module Successful =
        let JSON model =
            model
            |> json
            |> Successful.OK
            >=> Writers.setMimeType "application/json; charset=utf-8"

    let private bodyOf request =
        request.rawForm
        |> Text.Encoding.UTF8.GetString

    let private bindModel<'a> handler context =
        let body = bodyOf context.request in
        match ofJson<'a> body with
        | Some model ->
            handler model context
        | None ->
            RequestErrors.BAD_REQUEST "Wrong request body format" context

    type LoginData = { userId: string; expireDate: DateTime }

    type Token = { token: string; expireDate: DateTime }

    let (|ValidToken|_|) str =
        str
        |> Crypto.decode
        |> ofJson<LoginData>
        |> Option.bind (fun token ->
            if token.expireDate > DateTime.Now then Some token else None)

    let generateToken userId =
        let loginData = { userId = string userId;
                          expireDate = DateTime.Now + (TimeSpan.FromHours 2.) } in
        { token = loginData |> json |> Crypto.encode;
          expireDate = loginData.expireDate }

    let authorize handler context =
        let authValueOpt = context.request.header "Authorization"
        match authValueOpt with
        | Choice1Of2 value ->
            match String.split ' ' value with
            | ["Bearer"; ValidToken token] ->
                match Storage.findUser token.userId with
                | Some user ->
                    handler user context
                | None ->
                    RequestErrors.UNAUTHORIZED "Invalid authorization header value" context
            | _ ->
                RequestErrors.UNAUTHORIZED "Invalid authorization header value" context
        | Choice2Of2 errorMsg ->
            RequestErrors.UNAUTHORIZED errorMsg context

    type UserDesc = { username: string; encryptedPassword: string }

    let registerUser userRequest =
        match Storage.findUserByName userRequest.username with
        | None ->
            let password = Crypto.decode userRequest.encryptedPassword
            match Storage.createUser userRequest.username password with
            | Some _ ->
                Successful.OK ""
            | None ->
                ServerErrors.SERVICE_UNAVAILABLE "Cannot create user."
        | Some _ ->
            RequestErrors.BAD_REQUEST "Such username already exists."

    let login userRequest =
        let password = Crypto.decode userRequest.encryptedPassword
        match Storage.findUserByName userRequest.username with
        | Some user ->
            if user.password = password then
                Successful.JSON (generateToken user.id)
            else
                RequestErrors.NOT_FOUND ""
        | None ->
                RequestErrors.NOT_FOUND ""

    type UserData = { data: string }
    type UserDataCreationResponce = { dataId: int64 }

    let createData user data =
        match Storage.createData data.data (string user.id) with
        | Some id ->
            Successful.JSON { dataId = id }
        | None ->
            ServerErrors.SERVICE_UNAVAILABLE "Could not save data."

    let getData id user =
        let userId = string user.id
        match Storage.findData id userId with
        | Some data ->
            Successful.JSON { data = data }
        | None ->
            RequestErrors.NOT_FOUND ""

    let getDataIds user =
        let allData = Storage.getUserData (string user.id)
        Successful.JSON allData

    let app =
        choose [
            path "/users" >=> choose [
                POST >=> bindModel<UserDesc> registerUser
                RequestErrors.BAD_REQUEST "Illegal operation for resource 'user'."
            ]
            path "/login" >=> choose [
                POST >=> bindModel<UserDesc> login
                RequestErrors.BAD_REQUEST "Illegal operation for resource 'login'."
            ]
            path "/data" >=> choose [
                POST >=> authorize (fun user -> bindModel<UserData> (createData user))
                GET >=> authorize getDataIds
                RequestErrors.BAD_REQUEST "Illegal operation for resource 'data'."
            ]
            pathScan "/data/%d" (fun dataId ->
                choose [
                    GET >=> authorize (getData dataId)
                    RequestErrors.BAD_REQUEST "Illegal operation for resource 'data'."
                ])
            path "/key" >=> choose [
                GET >=> Successful.JSON (Crypto.RsaConfig.toPublic Crypto.config)
                RequestErrors.BAD_REQUEST "Illegal operation for resource 'key'."
            ]
            RequestErrors.BAD_REQUEST "Unknown resource."
        ]

do startWebServer defaultConfig Endpoint.app
