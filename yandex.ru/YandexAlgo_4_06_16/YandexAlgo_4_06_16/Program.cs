using System;
using System.Diagnostics.Eventing.Reader;

namespace YandexAlgo_4_06_16
{
	class Program
	{
		// https://contest.yandex.ru/algorithm2016/contest/2529/problems/B/
		static void Main(string[] args)
		{
			char[][] a = new char[3][];
			for (int i = 0; i < 3; i++)
			{
				a[i] = new char[3];
				var line = Console.ReadLine();
				for (int j = 0; j < 3; j++)
				{
					a[i][j] = line[j];
				}
			}

			bool desc = false;
			int current = -1, previous = -1;
			int firstNumber = -1;
			int firstNumberIndex = -1;
			Iter(
				(i, j, k) =>
				{
					char c = a[i][j];
					int value;
					if (int.TryParse(c.ToString(), out value))
					{
						if (firstNumber == -1)
						{
							firstNumber = value;
							firstNumberIndex = k;
						}

						current = value;
						if (previous != -1)
						{
							desc = current < previous;
						}
						else
						{
							previous = current;
						}

					}
				});

			Fill(a, firstNumberIndex, firstNumber, desc);
			

			for (int i = 0; i < 3; i++)
			{
				for (int j = 0; j < 3; j++)
					Console.Write(a[i][j]);
				Console.Write("\n");
			}
		}

		private static void Fill(char[][] a, int firstNumberIndex, int firstNumber, bool desc)
		{
			int startNumber = 0;
			// TODO
			if (!desc)
				startNumber = (firstNumber - 2) - firstNumberIndex ;

			Iter(
				(i, j, k) =>
				{
					char c = a[i][j];
					int num;
					if (!desc)
						num = (startNumber + k) % 8 + 2;
					else
						num = (startNumber + k) % 8 + 1; // todo

					int value;
					if (int.TryParse(c.ToString(), out value))
						if(num != value)
							throw new Exception("invalid number");
					else
						a[i][j] = num.ToString()[0];

				});
		}

		private static void Iter(Action<int, int, int> action)
		{
			for (int i = 0; i < 8; i++)
			{
				int row, col;
				if (i < 3)
				{
					row = 0;
					col = i;
				} 
				else if (i == 4)
				{
					row = 1;
					col = 2;
				}
				else if (i < 8)
				{
					row = 2;
					col = 7 - i;
				}
				else
				{
					row = 1;
					col = 0;
				}

				action(row, col, i);
			}

		}
	}
}