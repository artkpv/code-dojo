using System;
using System.Collections.Generic;
using System.Linq;

namespace _7_royal_gardeners
{
    class Program
    {
        static void Main(string[] args)
        {
            int B = int.Parse(Console.ReadLine());
            int N = int.Parse(Console.ReadLine());
			var garderners = new (int d, int l, int r)[N];
			for (int i = 0; i < N; i++)
			{
				int[] d_l_r = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
				garderners[i] = (d_l_r[0], d_l_r[1], d_l_r[2]);
			}

            int M = int.Parse(Console.ReadLine());
			int[] outSums = new int[M];
			var inspectors = new (int l, int r, int inx)[M];
			for (int i = 0; i < M; i++)
			{
				int[] l_r = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
				inspectors[i] = (l_r[0], l_r[1], i);
				outSums[i] = 0;
			}

			Calculate(garderners, inspectors, outSums);
			Console.WriteLine(string.Join('\n', outSums));
        }

		private static void Calculate(
			(int d, int l, int r)[] garderners, 
			(int l, int r, int inx)[] inspectors,
			int[] outSums)
		{
/* 
Iterate all lines in asc order and calculate seeds sums for each tax inspector.

1. 
  ----   10  1 garderner
   ---   20  2 garderner
  ===        1 tax insp.
   ===       2 tax insp.
  1234  beds

      Sum  TI        Prev bed
At 1: 10   1,0       0
At 2: 30   1,10 2,0  1
At 4: 30   1,70 2,60 2
At 5: 

2. 
  ----   10  1 garderner
    --   20  2 garderner
  ==         1 tax insp.
    ==       2 tax insp.


 */
			if (garderners.Length == 0 || inspectors.Length == 0)
				return;
			Array.Sort(garderners, ((int d, int l, int r) a, (int d, int l, int r) b)  => a.l.CompareTo(b.l));
			Array.Sort(inspectors, ((int l, int r, int inx) a, (int l, int r, int inx) b)  => a.l.CompareTo(b.l));
			int gInx = 0;
			int iInx = 0;
			var currentInspectors = new HashSet<int>();
			var currentGarderners = new HashSet<int>();
			int sum = 0;
			int bed = Math.Min(garderners[gInx].l, inspectors[iInx].l);
			int prev = -1;
			while (true)
			{
				if (gInx >= garderners.Length || iInx >= inspectors.Length)
					break;
				// Stop at: start of TI or G, end+1 of TI or G

				// 1 Calc for all TIs at [prev..bed-1] inclusive: (bed-prev) * sum

				// 2  


				// Add to TIs: for each sum * (bed - previousBed)
				
				// Add to sum all G started at bed 

				// Add to TIs that end at bed:  + 1*sum
				// and remove them from current TIs

				// 
			}
		}
	}
}
