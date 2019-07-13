/*

 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;

public static class Primes
{
    public static void Main(string[] argv)
    {
        if (argv.Length == 0)
        {
            Console.Write("Prints primes < n. Usage: primes n.");
            return;
        }
        int n = int.Parse(argv[0]);
        if (n < 2)
            return;
        var seive = new BitArray(n, true);
        for (int i = 3; i < (int) Math.Sqrt(n) + 1; i += 2)
        {
            if (seive[i])
            {
                for (int j = i*i; j < n; j += i*2) 
                    seive[j] = false;
            }
        }
        Console.Write("2");
        for (int i = 3; i < n; i += 2) 
        {
            if (seive[i]) 
            {
                Console.Write(' ');
                Console.Write(i);
            }
        }
        Console.Write("\n");
    }
}
