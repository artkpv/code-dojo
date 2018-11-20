/*
n <= 2e5
p - num of c on left 
c - num of p on right 
1 swap

1) BF. Swap & calc, from left, from right:
T n^3. S 1

2) swap most left c and most right p and calc


pccppc 2
ppcpcc 1+1

 */

using System;

namespace recode_4
{
	class a
	{
		static void Main(string[] args)
		{
			var s = Console.ReadLine().Trim();
			int c = -1, p = s.Length;
			for (int i = 0; i < s.Length; i++)
			{
				if (s[i] == 'p') p = i;
				if (s[i] == 'c' && c == -1) c = i;
			}

			if (c == -1 || p == s.Length || c > p)
			{
				c = -1;
				p = s.Length;
			}

			int tastiness = 0;

			int cakes = 0;
			for (int i = 0; i < s.Length; i++)
			{
				if (i == p)
					cakes++;
				else if (i == c)
					tastiness += cakes;
				else if (s[i] == 'c')
					cakes++;
				else if (s[i] == 'p')
					tastiness += cakes;
			}

			int pies = 0;
			for (int i = s.Length-1; i >= 0; i--)
			{
				if (i == c)
					pies++;
				else if (i == p)
					tastiness += pies;
				else if (s[i] == 'p')
					pies++;
				else if (s[i] == 'c')
					tastiness += pies;
			}

			Console.WriteLine(tastiness);
		}
	}
}
