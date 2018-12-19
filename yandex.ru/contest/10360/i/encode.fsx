
open System
open System.IO

module Crypto =
    open System.Numerics

    type RsaConfig = { modulo: int; publicExp: int; privateExp: int }

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

    let encode = RsaConfig { exp = 30593; modulo = 66043 } |> rsaEncode

let pass = Crypto.encode "123" 
printfn pass