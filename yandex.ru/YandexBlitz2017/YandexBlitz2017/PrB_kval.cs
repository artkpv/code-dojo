using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Numerics;

namespace YandexBlitz2017
{
	public class ProgramB
	{
//		public static void Main()
//		{
//			Program.Solve();
//		}

		public static void Solve()
		{
			var N = 1000;
			for (var n = 1; n < N; n++)
			{
				var isFound = false;
				for (var k = 1; k < N*N; k++)
				{
					var s = k.ToString().ToCharArray().ToList().Select(d => int.Parse(d.ToString()))
						.Aggregate(0, (i, i1) => i + i1);
					if ((3 * k) % (s*s) == 0)
					{
						var right = (3 * k) / (s*s);
						if (right == n)
						{
							isFound = true;
							break;
						}
					}
				}

				if(!isFound)
					Console.WriteLine(n);
			}
		}
	}
}