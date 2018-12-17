// Learn more about F# at http://fsharp.org

open System
open System.IO
open Newtonsoft.Json

let json smth = JsonConvert.SerializeObject smth

module Crypto =
    open System.Numerics

    type RsaConfig = { modulo: int; exp: int }

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

    let encode = { exp = 30593; modulo = 66043 } |> rsaEncode

type LoginData = { userId: string; expireDate: DateTime }

type Token = { token: string; expireDate: DateTime }

let generateToken userId date =
    let loginData = { userId = string userId;
                      expireDate = date } in
    System.Console.WriteLine (loginData |> json)
    { token = loginData |> json |> Crypto.encode;
      expireDate = date }


[<EntryPoint>]
let main argv =
    let date = argv |> Seq.head
    System.Console.WriteLine (generateToken "2875ea1c-a1fa-4cd9-8862-0b31f37842b4" (DateTime.Parse date))
    // System.Console.WriteLine (Crypto.encode password)
    0 // return an integer exit code
