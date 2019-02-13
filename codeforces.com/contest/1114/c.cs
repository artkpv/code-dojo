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
            Int64[] a = Console.ReadLine().Trim().Split(' ').Select(Int64.Parse).ToArray();
            var maxs = new Dictionary<Int64,int>();
            Int64 max = 0;
            foreach (var i in a.Select((e,i) => new {e, i}).OrderByDescending(i => i.e).Take(m*k))
            {
                max += i.e;
                if (maxs.ContainsKey(i.e))
                    maxs[i.e]++;
                else
                    maxs[i.e] = 1;
            }
            
            // fill divs going from left to right and taking all from sorted:
            var divs = new int[k];
            int count = 0;
            int j = 0;
            for (int i = 0; i < a.Length; i++)
            {
                if (maxs.ContainsKey(a[i]) && maxs[a[i]] > 0){
                    count++;
                    maxs[a[i]]--;
                    if (count == m) {
                        divs[j++] = i;
                        count = 0;
                    }
                }
            }

            Console.WriteLine(max);
            Console.WriteLine(string.Join(" ", divs.Take(k-1).Select(i=>(i+1).ToString())));
        }
    }
}
