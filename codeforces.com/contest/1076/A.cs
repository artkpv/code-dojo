/*
 s, 2<=|s|<= 2*10^5
 remove at most 1
 get smallest possible

 1) BF. T ~n^2, S ~1
 
 2) 

 */

using System;
using System.Diagnostics.Eventing.Reader;

namespace _1076
{
	class A
	{
		static void Main(string[] args)
		{
			int n = int.Parse(Console.ReadLine().Trim());
			string s = Console.ReadLine().Trim();

			var res = Mnimize(n, s);
			Console.WriteLine(res);
		}

		private static string Mnimize(int n, string s)
		{
			int k = -1;
			for (int i = 0; i < n; i++)
			{
				int j = Math.Min(k >= 0 ? k : 0, i);
				for (; j < n - 1; j++)
				{
					int cmp =
						s[j >= k ? j + 1 : j].CompareTo(s[j >= i ? j + 1 : j]);
					if (cmp > 0)
					{
						k = j;
						break;
					}
				}

				if (k == -1 && j == n - 1)
					k = n - 1;
			}

			var res = k >= 0 ? s.Remove(k, 1) : s;
			return res;
		}
	}
}
