using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Math
{
	public static class CombinatoricsAlgorithms
	{
        /// <summary>
		/// Returns next permutation. 
		/// First:
		/// </summary>
		/// <example>First:1234. Last:4321.</example>
		/// <param name="X"></param>
		/// <returns></returns>
		public static int[] NextPermutation(int[] X)
		{
			int i = X.Length - 2,
				j;

			//найдем наибольшее i, меньшее следующих
			while (i >= 0 && X[i] > X[i + 1])
				i--;

			if (i >= 0)
			{
				//После этого X[i] нужно увеличить минимально возможным способом, т.е. найти среди X[i+1],...,X[N] наименьшее число, большее его.
				j = i + 1;
				while (j + 1 < X.Length && X[j + 1] > X[i])
					j++;
				Swap(ref X[i], ref X[j]);

				//расположить числа с номерами i+1,...,N так, чтобы перестановка была наименьшей, то есть в возрастающем порядке. 
				for (j = i + 1; j < (int) (X.Length + i+1) / 2; j++)
				{
					Swap(ref X[j], ref X[X.Length - j + i]);
				}
				return X;
			}
			return null;
		}

		private static void Swap(ref int i1, ref int i2)
		{
			int i3 = i1;
			i1 = i2;
			i2 = i3;
		}

		/// <summary>
		/// Returns next distribution
		/// </summary>
		/// <param name="places">Array of natural numbers</param>
		/// <param name="maxValue">Maximum number</param>
		/// <returns>Next distribution or null if there are no more distributions</returns>
		public static int[] NextDistribution(int[] places, int maxValue)
		{
			int i = places.Length - 1;
			while (i >= 0 && places[i] == maxValue)
			{
				places[i] = 1;
				i--;
			}
			if (i >= 0)
			{
				places[i]++;
				return places;
			}

			return null;
		}
	}
}
