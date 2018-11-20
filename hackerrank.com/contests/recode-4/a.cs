/*
 * 1<= s <= 100
 * p prefix
 * find p - max number as ss
 
 1) BF. T n*n. S 1
 */

using System;

namespace recode_4
{
	class a
	{
		static void Main(string[] args)
		{
			var s = Console.ReadLine().Trim();
			var n = s.Length;
			var max = 1;
			for (int i = 0; i < n; i++)
			{
				int found = 1;
				for (int j = 1; j < n-i; j++)
				{
					if (Compare(s, i, j))
					{
						found++;
					}
				}

				if (found > max)
					max = found;
			}
			Console.WriteLine(max);
		}

		private static bool Compare(string s, int p, int j)
		{
			for (int i = 0; i <= p; i++)
			{
				if (j + i >= s.Length)
					return false;
				if (s[i] != s[j + i])
					return false;
			}

			return true;
		}
	}
}
