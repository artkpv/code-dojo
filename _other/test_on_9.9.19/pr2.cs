using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int[] T) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        if (T == null || T.Length < 2)
            throw new ApplicationException("Should be at least 2 days");
        int n = 1;
        int max = T[0];
        for (int i = 1; i < T.Length; i++) 
        {
            if (T[i] <= max)
                n = i + 1;
        }
        if (n == T.Length)
            throw new ApplicationException("Should be at least one summer day");
        return n;
    }
}
