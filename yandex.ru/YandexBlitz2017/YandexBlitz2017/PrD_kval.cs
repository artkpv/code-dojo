using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Numerics;

namespace YandexBlitz2017
{
	public static class PrD
	{
		public static bool IsPossible(int[] purses, int m)
		{
			purses = purses.OrderBy(i=>i).ToArray(); // O(n*lg(n))
			var n = purses.Length;
			var max = purses.Sum(); // O(n)
			var min = purses[purses.Length - 1];
			if (max == m || min == m)
				return true;
			if (m < min || max < m)
				return false;

			// O(2**n) !
			for (BigInteger combination = 0; combination < (BigInteger) Math.Pow(2, n - 1); combination++)
			{
				int minus = purses.Select((i, inx) => ((1 << inx) & combination) > 0 ? i : 0).Sum();
				if (m == max - minus)
					return true;
			}

			return false;
		}
	}

	public static class Program
	{
		public static void Main(string[] args)
		{
			var n = int.Parse(Console.ReadLine());
			var purses = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
			var prevSum = int.Parse(Console.ReadLine());
			Console.WriteLine(PrD.IsPossible(purses, prevSum) ? "Yes" : "No");
		}
	}
}