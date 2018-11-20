using System;
using System.Linq;

namespace prd
{
    class Program
    {
        static void Main(string[] args)
        {
            var nq = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            int n = nq[0], q = nq[1];
            var a = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            for(int query = 1; query <= q; query++)
            {
                var lr = Console.ReadLine().Trim().Split(' ').Select(int.Parse).OrderBy(j=>j).ToArray();
                int[] triangle = FindTriangle(a, lr[0] - 1, lr[1] - 1);
                triangle = triangle?.Select(i => i + 1).OrderBy(i=>i).ToArray();
                Console.WriteLine(triangle != null ? string.Join(" ", triangle) : "-1");
            }
        }

        private static int[] FindTriangle(int[] ints, int l, int r)
        {
            int len = r - l + 1;
            var sorted = ints.Select((v, inx) => Tuple.Create(inx, v)).Skip(l).Take(len).OrderBy(t=>t.Item2).ToArray();
            for (int i = len - 1; i > 1; i--)
            {
                Tuple<int,int> a = sorted[i], b = sorted[i-1], c = sorted[i-2];
                if (a.Item2 < c.Item2 + b.Item2)
                    return new[] {a.Item1, b.Item1, c.Item1};
            }

            return null;
        }
    }
}
