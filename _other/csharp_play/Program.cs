using System;

namespace csharp_play
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string line = Console.ReadLine();
            line switch {
                null => throw new NullReferenceException("Null"),
                 => Console.WriteLine($"Parsed {lineInt}"),
                _ => throw new Exception("Default exception")
            };
        }
    }
}
