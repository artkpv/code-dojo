using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Yandex2016Algo
{
	class Program
	{
		static void Main (string[] args)
		{
			List<int[]> coordinates = new List<int[]>();
			for (int i = 0; i < 5; i++)
			{
				var numbers = Console.ReadLine().Split(' ');
				coordinates.Add(new int[2] { int.Parse(numbers[0]), int.Parse(numbers[1]) });
			}

			foreach (var v in coordinates)
			{
				// find nearest:
				int[] w = null;
				double minDistance = Double.MaxValue;
				foreach (var x in coordinates)
				{
					var distance = Math.Sqrt(Math.Pow(Math.Abs(v[0] - x[0]), 2) + Math.Pow(Math.Abs(v[1] - x[1]), 2));
					if (distance < minDistance)
					{
						minDistance = distance;
						w = x;
					}
				}

				// check all other points on one side:
				bool? isLeft = null;
				foreach (var x in coordinates)
				{
					if (x != v && x != w)
					{
						var x1Dif = x[0] - v[0];
						var x2Dif = x[0] - w[0];
						var y1Dif = x[1] - v[1];
						var y2Dif = x[1] - w[1];

						// todo? 


					}
				}
			}

			return;
		}
	}
}
