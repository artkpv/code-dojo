/*
 
1 <= s1 , s2 <= 5000
Longest common child?


I1
Remove non-common chars.
N - first , M - second
For D1 in first in from max(N,M) - min(N,M) to N-1:  // ~N
    Choose and remove D1 chars in first              // ~ comb(D1, N)
    Choose and remove min(M, N-D1) chars in second   // ~ comb(min(M,N-D1), M)
    if match:
        return this

Time: O(N* (1 + N!/(N-1)!/2 + .. ) * (1 + M!/(M-1)!/2 + ..) * (min(N*M)) ) ~= N*(N!+M!)*N
Space: N+M


I2
Remove non-common chars.

L (i, j) - longest child for strings starting at i and j.
max(
    if left[i] == right[j] then 1 + L(left[i+1:], right[j+1:]) else -1,
    L(i, j+1),  # remove right
    L(i+1, j)   # remove left
)


Longest child at i-th = longest child of A[:i] and B[:j] + longest child 

Longest = longest so far + longest from these three:
ABCD
ABDC

ABCD
BDC
    
BCD
ABDC


TIME (I1): ~(N*M)


Idea 3
Bottom-up

init L
for i in left: N-1..0
  for j in right: M-1..0
     fill table L
return L[N-1][M-1]


Ex1
ABCD ABDC
3 : ABC ABD

ABCD
i
ABDC
   j
i\j 0 1 2 3 4 
0   3 1 1 1 0
1   2 2 1 1 0
2   1 1 1 1 0
3   1 1 1 0 0
4   0 0 0 0 0 


Ex2 
HARRY
SALLY
2  AY 

 */
using System;
using System.Collections.Generic;
using System.Linq;

namespace common_child
{
    class Program
    {
        private const int NEG_INF = int.MinValue;

        static void Main(string[] args)
        {
            string a = Console.ReadLine();
            string b = Console.ReadLine();
            int[][] L = new int[a.Length+1][];
            for (int i = 0; i < a.Length; i++) 
            {
                L[i] = Enumerable.Repeat(NEG_INF, b.Length).Concat(new [] {0}).ToArray();
            }               
            L[a.Length] = Enumerable.Repeat(0, b.Length+1).ToArray();

            for (int i = a.Length-1; i >= 0; i--)  
            {
                for (int j = b.Length-1; j >= 0; j--)
                {
                    L[i][j] = new int[] {
                        a[i] == b[j] ? 1 + L[i+1][j+1] : NEG_INF,
                        L[i][j+1],
                        L[i+1][j]
                    }.Max();
                }
            }
            Console.WriteLine(L[0][0]);
        }
    }
}
