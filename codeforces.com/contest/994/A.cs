using System;
using System.Linq;

namespace _994
{
    class A
    {
        static void MainA(string[] args)
        {
            int[] n_m = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            int[] a = Console.ReadLine().Trim().Split(' ').Select(int.Parse).Take(n_m[0]).ToArray();
            int[] b = Console.ReadLine().Trim().Split(' ').Select(int.Parse).Take(n_m[1]).ToArray();
            Console.WriteLine(a.Where(i=>b.Contains(i)).Aggregate("",(s,s1)=>s+ " " + s1).Trim());
        }
    }
}
