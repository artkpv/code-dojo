/*

n,m,k
2<=n<=200_000
1<=m
2<=k
m*k <= n
-10^9 <= a_i <= 10^9

I1 BF.
All k subseq. 
(n-k)*(n-k-1).. | k times

Permutations: (n k)
Find max: n

Time: (n k) * n = O(n^k*n)


I2
Find max: sort, choose m*k last memebers - NO. See ex2


I3 Greedy...

k arrays with >=m numbers


m=2, k=3
1 1  2 2  3 3
1 1 2  2 3  3 4  | 15   or 1 1  2 2  3 3 4 | 13


k = 3
2 2 1 1 10 


m*k - min 
+1 el at right: can change k subarrays. 
1:
5 2
5 2
4 1 | 19

2: + 1 
5 2 5
2 4 
1 1 | 18

5 2
5 2 4
1 1 | 19

5 2 
5 2
4 1 1 | 19

3: + 3
(3 * 3 variants)

5 2
5 2 
4 1 1 3 | 21

4: + 2 
(3 * 3 * 3 vars = 9)

5 2
5 2 4
1 1 3 2 | 21

Time: (n-m*k) * k 
O((200_000-2) * 1


Ex1
9 2 3
5 2 5 2 4 1 1 3 2
>
21
3 5 


Ex2
1000 3 2 
99 0 .. 0 99 0 .. 0 .. (10)
100       100
>
198  (not 99*3!)
1

Ex3
k = 3, m = 2 
1 1  1 1  10 5 5 | 19
1 1 1  1 10  5 5 | 23


 */
using System;
using System.Collections.Generic;
using System.Linq;

namespace _1114
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nmk = Console.ReadLine().Trim().Split(' ').Select(Int32.Parse).ToArray();
            int n = nmk[0], m = nmk[1], k = nmk[2];
            int[] a = Console.ReadLine().Trim().Split(' ').Select(Int32.Parse).ToArray();

            int[] sorted = a.OrderByDescending().ToArray();

            var divs = new int[k];
            var div_inxs = new LinkedList<int>[k];
            var div_mins = new int[k];
            for (int i = 0; i < k; i++) {
                divs[i] = Math.Max(0, i*m - 1);
                div_inxs[i] = new LinkedList<int>(Enumerable.Range(i*k, m));
                div_mins[i] = a.Skip(i*k).Take(m).Min();
            }

            for (int i = m*k; i < n; i++)
            {
                int new_inx = i;
                // Increase sizes of divs greedily:
                for (int ii = k-1; ii >= 1; ii--) {
                    // Update maxs in adj divs, shrink right one w/o decrease of sum.

                    // 1) Is to replace left most with new_inx?
                    // 2) Otherwise if to update min with the new_inx?
                    //    BUT then we BREAK linked list!

                    int compare = a[div_inxs[ii].First.Value] - a[new_inx];
                    int compare2 = a[div_maxs[ii][0]] - a[div_maxs[ii-1][m-1]];

                    int first = divs[ii];
                    if (a[first] > a[last]) {
                        break;
                    }
                    else if (a[first] == a[last])
                }
            }

            int max = 0;
            // count max
            for (int i = 0; i < k; i++)
            {
                int start = divs[i];
                int len = (i+1 < k ? divs[i+1] : n) - start;

                max += a.Skip(divs[i]).Take(len).OrderByDescending(ii => ii).Take(m).Sum();
            }

            Console.WriteLine(max);
            Console.WriteLine(string.Join(' ', divs.Skip(1).Select(i=>i.ToString())));
        }
    }
}
