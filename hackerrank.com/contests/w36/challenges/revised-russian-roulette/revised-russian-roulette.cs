
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution 
{
	static int[] revisedRussianRoulette(int[] doors) 
	{
		int max = 0, min = 0;
		for(int i = 0; i < doors.Length; i++) 
		{
			if(doors[i] == 1) // locked
			{  
				max++;
				min++;
				if(i + 1 < doors.Length && doors[i+1] == 1) 
				{
					max++;
					i++;
				}
			}
		}
		return new int[] { min, max };
	}

	static void Main(String[] args) 
	{
		int n = Convert.ToInt32(Console.ReadLine());
		string[] doors_temp = Console.ReadLine().Split(' ');
		int[] doors = Array.ConvertAll(doors_temp,Int32.Parse);
		int[] result = revisedRussianRoulette(doors);
		Console.WriteLine(String.Join(" ", result));
	}
}
