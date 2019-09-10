using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public const int MAX = 1000000;

    // Add to total current interval periods.
    public int AddPeriodInterval(int total, int n) 
    {
        if (n < 3)
            return total;
        try 
        {
            checked 
            { 
                int x = (n*n - 3*n + 2) / 2;
            }
        }
        catch (OverflowException) 
        {
            // Discard large periods (see pr. requirements).
            return -1;
        }
        if (x > MAX || total + x > MAX)
            return -1;
        return total + x;
    }

    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int periods = 0;
        if (A == null || A.Length < 3)
            return periods;
        int count = 2;
        int velocity = A[1] - A[0];
        for (int i = 2; i < A.Length; i++)
        {
            if (A[i] - A[i-1] == velocity)
                count++;
            else
            {
                periods = AddPeriodInterval(periods, count);
                if (periods == -1)
                    break;
                velocity = A[i] - A[i-1];
                count = 2;
            }
        }
        periods = AddPeriodInterval(periods, count);
        return periods;
    }
}
