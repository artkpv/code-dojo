using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Numerics;

namespace YandexBlitz2017
{
	public class PrA
	{
		public static string Game(IEnumerable<int> cards)
		{
			var q = new Queue<int>(cards);
			int petya = 0; 
			int vasya = 0;
			while (q.Count > 0)
			{
				var c1 = q.Dequeue();
				petya += c1;

				if (q.Count > 0)
				{
					var c2 = q.Dequeue();
					vasya += c2;
					if (q.Count > 0)
					{
						if (c1 < c2)
							petya += q.Dequeue();
						else 
							vasya += q.Dequeue();
					}
				}
			}

			if (petya > vasya)
				return "Petya";
			else if (vasya > petya)
				return "Vasya";
			throw new Exception("invalid");
		}
	}

	public class Program
	{
		public static void Main(string[] args)
		{
			var n = int.Parse(Console.ReadLine());
			var a = Console.ReadLine().Trim().Split(' ').Select(int.Parse);
			Console.WriteLine(PrA.Game(a));
		}
	}
}