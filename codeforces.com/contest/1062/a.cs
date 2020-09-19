using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
1<= n <=100
1 <= a_i <= 1000
.. a1 < a2 .. 

largest consecutive elements

1) BF. O(n)


 */

namespace _1062
{
	class A
	{
		static void Main(string[] args)
		{
			int n = int.Parse(Console.ReadLine().Trim());
			int[] a = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();

			int max = 0;
			int m = a[0] == 1 ? 2 : 1;
			for (int i = 1; i < a.Length; i++)
			{
				if (a[i] - a[i-1] == 1)
					m++;
				else
				{
					m -= 2;
					if (m > max)
						max = m;
					m = 1;
				}
			}

			if (a[a.Length - 1] == 1000)
				m += 1;
			m -= 2;
			if (m > max)
				max = m;
			Console.WriteLine(max);
		}
	}
}
