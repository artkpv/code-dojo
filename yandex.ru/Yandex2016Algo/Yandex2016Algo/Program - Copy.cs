using System;
using System.Collections.Generic;

namespace Yandex2016Algo
{
	class Program
	{
		static void Main(string[] args)
		{
			var N = int.Parse(Console.ReadLine());

			if (N == 0)
			{
				Console.WriteLine("0");
				return;
			}
			else if(N < 0)
				throw new ArgumentException();

			int min = int.MaxValue, max = int.MinValue;
			List<char> readChars = new List<char>();
			int ch;
			int count = 0;
			while (true)
			{
				ch = Console.Read();

				if (ch == -1 || ch ==  ' ')
				{
					int a;
					if(int.TryParse(new string(readChars.ToArray()), out a) && a >= 0)
					{
						if (a < min)
							min = a;
						if (a > max)
							max = a;

						count++;
						if (count >= N)
							break;
					}

					readChars.Clear();
					if (ch == -1)
						break;
				}
				else
				{
					readChars.Add((char)ch);
				}
			}

			Console.WriteLine(max - min);
			return;
		}
	}
}
