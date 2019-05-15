using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace _7_royal_gardeners
{
    class Program
    {
        static void Main(string[] args)
        {
			TextReader input;
	#if JUDGE
			input = new StreamReader("input.txt");
	#else
			input = Console.In;
	#endif
            int B = int.Parse(input.ReadLine());
            int N = int.Parse(input.ReadLine());
			var garderners = new (int d, int l, int r)[N];
			for (int i = 0; i < N; i++)
			{
				int[] d_l_r = input.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
				garderners[i] = (d_l_r[0], d_l_r[1], d_l_r[2]);
			}

            int M = int.Parse(input.ReadLine());
			int[] outSums = new int[M];
			var inspectors = new (int l, int r, int inx)[M];
			for (int i = 0; i < M; i++)
			{
				int[] l_r = input.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
				inspectors[i] = (l_r[0], l_r[1], i);
				outSums[i] = 0;
			}
			input.Close();

			Calculate(garderners, inspectors, outSums);

			TextWriter output;
	#if JUDGE
			output = new StreamWriter("output.txt");
	#else
			output = Console.Out;
	#endif
			output.WriteLine(string.Join("\n", outSums));
			output.Close();

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
			if (garderners.Length == 0 || inspectors.Length == 0)
				return;
			Array.Sort(garderners, ((int d, int l, int r) a, (int d, int l, int r) b)  => a.l.CompareTo(b.l));
			Array.Sort(inspectors, ((int l, int r, int inx) a, (int l, int r, int inx) b)  => a.l.CompareTo(b.l));
			int gInx = 0;
			int iInx = 0;
			var currentInspectors = new SortedSet<(int l, int r, int inx)>(
				Comparer<(int l, int r, int inx)>.Create(
					((int l, int r, int inx) a, (int l, int r, int inx) b)  => a.r.CompareTo(b.r))
				);
			var currentGarderners = new SortedSet<(int d, int l, int r)>(
				Comparer<(int d, int l, int r)>.Create(
					((int d, int l, int r) a, (int d, int l, int r) b)  => a.r.CompareTo(b.r)));
			int sum = 0; // Previous period sum of seeds per a flower bed.
			int bed = -1;
			int prev = -1;

            (int bed, int sum) MoveNext() 
            {
				// Remove just finished inspectors / garderners.
				while (currentGarderners.Any() && currentGarderners.Min().r < bed)
				{
					sum -= currentGarderners.Min().d;
					currentGarderners.Remove(currentGarderners.Min);
				}

				while (currentInspectors.Any() && currentInspectors.Min.r < bed)
					currentInspectors.Remove(currentInspectors.Min);

                // Add just started inspectors / garderners.
				while (gInx < garderners.Length && garderners[gInx].l == bed)
				{
					currentGarderners.Add(garderners[gInx]);
					sum += garderners[gInx].d;
					gInx++;
				}
				while (iInx < inspectors.Length && inspectors[iInx].l == bed)
					currentInspectors.Add(inspectors[iInx++]);  // BUG ! It drops all except first: (1, 1, 0), (1, 1, 1), (1, 1, 2), etc. See input4.txt

                // Get next bed: the closest start / end of inspector / garderner.
				int nextBed  = gInx < garderners.Length ? garderners[gInx].l : int.MaxValue;
				nextBed = Math.Min(nextBed, iInx < inspectors.Length ? inspectors[iInx].l : int.MaxValue);
				nextBed = Math.Min(nextBed, currentGarderners.Any() ? currentGarderners.Min().r + 1 : int.MaxValue);
				nextBed = Math.Min(nextBed, currentInspectors.Any() ? currentInspectors.Min().r + 1 : int.MaxValue);
				return (nextBed, sum);
            }
			(bed, sum) = MoveNext();
			while (bed != int.MaxValue)
			{
                // Count for previous period, [prev..bed-1] inclusive
                if (sum > 0 && prev >= 0) 
                {
                    int seeds = (bed - prev) * sum;
                    foreach ((int l, int r, int inx) inspector in currentInspectors) 
                    {
                        outSums[inspector.inx] += seeds;
                    }
                }

                prev = bed;
                (bed, sum) = MoveNext();
			}
		}
	}
}
