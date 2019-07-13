using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
1 <= n , q  <= 1e6
1<= l, r <= n

eat -> increase remain

1) BF. T: O(q*n*n) S: O(q)

2) p - 0, q - 1

	p q r
	1 1 2
	2 0 1+2 = 3
	3 0 1+2+4 = 7
	4 0 1+2+4+8 = 15
	3 1 1+2+4+7 = 14
	3 2 1+2+4 + 7+14 = 28
	3 3 1+2+4 + 7+14+28 = 28

	(2^p-1) + pp*(1-2^q)/(1-2) = 

	T: O(n*n) S: O(1)

	Calc 0s 1s till i-th

Ex1
	1011 0
	21-2 1
	43-- 3
	-7-- 7
	---- 14

	000111 0
	11122- 1
	3334-- 3
	777--- 7
	14 14  14
	28 -   28
	-      56


	011 0
	12- 1
	3-- 3
	--- 6

 */

namespace _1062
{
	class A
	{
		static long pow(int a, int b, int n)
		{
			long x = 1, y = a;
			while (b > 0)
			{
				if (b % 2 == 1)
				{
					x = (x * y) % n; // multiplying with base
				}

				y = (y * y) % n; // squaring the base
				b /= 2;
			}

			return x % n;
		}

		static void Main(string[] args)
		{
			const int MOD = (int)1e9 + 7;
			int[] n_q = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
			string s = Console.ReadLine().Trim();
			int[] zeros = new int[s.Length];
			int[] ones = new int[s.Length];
			zeros[0] = s[0] == '0' ? 1 : 0;
			ones[0] = s[0] == '1' ? 1 : 0;
			for (int i= 1; i < s.Length; i++)
			{
				zeros[i] = zeros[i-1] + (s[i] == '0' ? 1 : 0);
				ones[i] = ones[i-1] + (s[i] == '1' ? 1 : 0);
			}

			int queries = n_q[1];
			while (queries > 0)
			{
				int[] l_r = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
				int l = l_r[0]-1, r = l_r[1]-1;
				int p = ones[r] - ones[l] + (s[l] == '1' ? 1 : 0);
				int q = zeros[r] - zeros[l] + (s[l] == '0' ? 1 : 0);

				long pp = pow(2, p, MOD) - 1;
				long qq = pp * (pow(2, q, MOD) - 1);
				long res = (pp + qq) % MOD;
				Console.WriteLine(res);
				queries--;
			}
		}
	}
}
