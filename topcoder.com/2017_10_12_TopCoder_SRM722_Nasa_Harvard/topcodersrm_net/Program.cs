using System;

namespace topcoder_srm
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine( new MulticoreProcessingEasy().fastestTime( 10000, 5, new[] {39, 37, 44}, new[] {8, 16, 6}));
			Console.WriteLine( new MulticoreProcessingEasy().fastestTime( 2000, 5, new[] {40,20}, new[] {2,4}));
			Console.WriteLine( new MulticoreProcessingEasy().fastestTime( 1000, 0, new[] {10}, new[] {3}));

			Console.WriteLine( new MulticoreProcessingEasy().fastestTime( 1000000000, 5, new[] {40,20}, new[] {2,4}));
			Console.Read();
		}
	}

	public class MulticoreProcessingEasy
	{
		public int fastestTime(int jobLength, int corePenalty, int[] speed, int[] cores)
		{
			int min_ms = int.MaxValue;
			int n = speed.Length;
			for (int i = 0; i < n; i++)
			{
				int machine_speed =
					(int) Math.Ceiling((double) jobLength / (speed[i] * cores[i]))
					+ (cores[i] - 1) * corePenalty;
				if (min_ms > machine_speed)
					min_ms = machine_speed;
			}
			return min_ms;
		}
	}

public class TCPhoneHomeEasy
{
	public int validNumbers(int digits, string[] specialPrefixes)
	{
		int full = (int) Math.Pow(10, digits);
		foreach (string p in specialPrefixes)
			full -= (int) Math.Pow(10, digits - p.Length);
		return full;
	}
}

public class HillClimber
{
	public int longest(int[] height)
	{
		int start = 0;
		int end = 0;
		int length = 0;
		for (int i = 1; i < height.Length; i++)
		{
			if (!(height[i] - height[i - 1] > 0))
				start = i;
			end = i;
			if (end - start > length)
				length = end - start;
		}
		return length;
	}
}
}

