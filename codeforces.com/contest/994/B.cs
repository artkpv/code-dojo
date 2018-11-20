using System;
using System.Collections.Generic;
using System.Linq;

namespace _994
{
    class B
    {
        static void Main(string[] args)
        {
            int[] n_k = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            int n = n_k[0];
            int k = n_k[1];
            long[] powers = Console.ReadLine().Trim().Split(' ').Select(long.Parse).Take(n).ToArray();
            long[] coins = Console.ReadLine().Trim().Split(' ').Select(long.Parse).Take(n).ToArray();

            var knights = powers.Select<long, Tuple<int,long,long>>((p, i) => new Tuple<int, long, long>(i, p, coins[i])).OrderBy((tuple => tuple.Item2)).ToArray();

            long[] res_coins = Enumerable.Repeat(0, n).Select(i=>(long)i).ToArray();
            for (int i = 0; i < knights.Length; i++)
            {
                int key = knights[i].Item1;
                long res = knights[i].Item3;

                //Array.Sort(knights, 0, i, Comparer<Tuple<int,long,long>>.Create((tuple, tuple1) => tuple.Item3.CompareTo(tuple1.Item3)));
                int last = i-1;
                for (int j = i - 2; j >= 0; j--)
                {
                    if (knights[j].Item3 < knights[j + 1].Item3)
                        break;
                    swap(knights, j, j + 1);
                    if (i - last <= k && last >= 0)
                    {
                        res += knights[last].Item3;
                        last = last - 1;
                    }
                }

                while (i - last <= k && last >= 0)
                {
                    res += knights[last].Item3;
                        last = last - 1;
                }

                res_coins[key] = res;
            }
            Console.WriteLine(string.Join(" ", res_coins));
            return;
        }

        private static void swap(Tuple<int, long, long>[] knights, int i, int i1)
        {
            var k = knights[i];
            knights[i] = knights[i1];
            knights[i1] = k;
        }
    }
}
