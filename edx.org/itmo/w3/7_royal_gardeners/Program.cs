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
		private static void Calculate(
			(int d, int l, int r)[] garderners, 
			(int l, int r, int inx)[] inspectors,
			int[] outSums)
		{
			// TODO. Next. Can optimize by using heap. Collect seeds from garderners and dont update inspectors 
			// each time a garderner start/ends. Only update when inspector ends. 
			// Thus time: n*log(n) to sort, n+m to calc?
			if (garderners.Length == 0 || inspectors.Length == 0)
				return;
			Array.Sort(garderners, ((int d, int l, int r) a, (int d, int l, int r) b)  => a.l.CompareTo(b.l));
			Array.Sort(inspectors, ((int l, int r, int inx) a, (int l, int r, int inx) b)  => a.l.CompareTo(b.l));
			int gInx = 0;
			int iInx = 0;
			var currentInspectors = new HashSet<(int l, int r, int inx)>();
			var currentGarderners = new HashSet<(int d, int l, int r)>();
			int sum = 0;
			int bed = -1;
			int prev = -1;

            int MoveNext() 
            {
                // Remove just finished inspectors / garderners.
                currentGarderners.RemoveWhere(g => g.r < bed);
                currentInspectors.RemoveWhere(ins => ins.r < bed);

                // Add just started inspectors / garderners.
				while (garderners.Any() && garderners[gInx].l == bed)
					currentGarderners.Add(garderners[gInx++]);
				while (inspectors.Any() && inspectors[iInx].l == bed)
					currentInspectors.Add(inspectors[iInx++]);

                // Get next bed: the closest start / end of inspector / garderner.
				int nextBed  = gInx < garderners.Length ? garderners[gInx].l : int.MaxValue;
				nextBed = Math.Min(nextBed, iInx < inspectors.Length ? inspectors[iInx].l : int.MaxValue);
				nextBed = Math.Min(nextBed, currentGarderners.Any() ? currentGarderners.AsEnumerable().Min(g => g.r-1) : int.MaxValue);
				nextBed = Math.Min(nextBed, currentInspectors.Any() ? currentInspectors.AsEnumerable().Min(i => i.r-1) : int.MaxValue);
				return nextBed;
            }
			bed = MoveNext();
			while (bed != int.MaxValue)
			{
                // Count for passed period, [prev..bed-1] inclusive
                if (sum > 0 && prev >= 0) 
                {
                    int seeds = (bed - prev) * sum;
                    foreach ((int l, int r, int inx) inspector in currentInspectors) 
                    {
                        outSums[inspector.inx] += seeds;
                    }
                }

                prev = bed;
                bed = MoveNext();
			}
		}
	}
}
