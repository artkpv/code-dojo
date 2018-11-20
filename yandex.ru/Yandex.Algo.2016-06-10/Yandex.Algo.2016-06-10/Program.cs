using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text.RegularExpressions;

namespace Yandex.Algo._2016_06_10
{
	class Program
	{
		static void Main(string[] args)
		{
			var firstSplit = Console.In.ReadLine().Split(' ');
			var options = new Options();
			options.Actors = new SortedSet<Tuple<int, string, List<Tuple<int, int>>>>(
				Comparer<Tuple<int, string, List<Tuple<int, int>>>>.Create((tuple, tuple1) => tuple.Item1.CompareTo(tuple1.Item1)));
			options.S = Console.In.ReadLine();
			int N = int.Parse(firstSplit[1]);
			for (int i = 0; i < N; i++)
			{
				var numbers = Console.In.ReadLine().Split(' ');
				var wording = Console.In.ReadLine();
				options.Actors.Add(new Tuple<int, string, List<Tuple<int, int>>>(int.Parse(numbers[1]), wording, new List<Tuple<int, int>()));
			}

			int minCharge = CalculateFromLarge(options);
			Console.Out.WriteLine(minCharge);
		}

		private static int CalculateFromLarge(Options options)
		{
			var minCharge = 0;
			var s = options.S;
			for (int i = 0; i < s.Length; i++)
			{
				int currentCharge = -1;
				for (int j = s.Length - i; j > 0; j--)
				{
					currentCharge = FindCharge(options, s.Substring(i, j));
					if (currentCharge != -1)
					{
						i = i + j - 1;
						break;
					}
				}

				if (currentCharge == -1) // not found 
					return -1;

				minCharge += currentCharge;
			}
			return minCharge;
		}

		private static int CalculateFromSmall(Options options)
		{
			var minCharge = 0;
			var s = options.S;
			for (int i = 0; i < s.Length; i++)
			{
				int currentCharge = -1;
				for (int j = 1; j + i < s.Length
				{
					currentCharge = FindCharge(options, s.Substring(i, j));
					if (currentCharge != -1)
					{
						i = i + j - 1;
						break;
					}
				}

				if (currentCharge == -1) // not found 
					return -1;

				minCharge += currentCharge;
			}
			return minCharge;
		}


		private static int FindCharge(Options options, string substring)
		{
			int currentCharge = -1;
			Regex r = new Regex(substring);

			foreach (var actor in options.Actors)
			{
				var m = r.Match(actor.Item2);
				if (m.Success)
				{
					int used = m.Length;

					foreach (var tuple in actor.Item3)
					{
						int i = tuple.Item1;
						int n = tuple.Item2;
						// TODO
						
						if(m.Index <= i)
							used -= (n - )

					}
					currentCharge = actor.Item1 * used;

					// add to used:
					actor.Item3.Add(new Tuple<int, int>(m.Index, m.Length));

					Trace.WriteLine($"Match: {m.Value} ({currentCharge})");

					break;
				}
			}
			return currentCharge;
		}

		class Options
		{
			public string S { get; set; }

			public SortedSet<Tuple<int, string, List<Tuple<int, int>>>> Actors { get; set; }
		}
	}
}