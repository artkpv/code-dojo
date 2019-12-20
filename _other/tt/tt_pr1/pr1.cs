
#define TRACE
#define DEBUG

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using System.Linq.Expressions;

// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    const int COLS = 10;
    private Dictionary<int, int> Parse(string s) {
        string[] split = s.Split(' ');
        var occupied = new Dictionary<int, int>();
        if (split.Length == 0)
            return occupied;
        foreach (var seat in split) {
            if (string.IsNullOrEmpty(seat))
                continue;
            int row = int.Parse(seat.Substring(0, seat.Length - 1));
            char colC = seat[seat.Length - 1];
            int col = colC - 'A';
            col -= ('J' <= colC ? 1 : 0);
            int colOccupied = 1 << (COLS - 1 - col);

            if (!occupied.ContainsKey(row))
                occupied[row] = 0;
            occupied[row] |= colOccupied;
            Debug.WriteLine($" seat {seat}: {row} {colOccupied} {occupied[row]}");
        }
        return occupied;
    }

    private int CalculateMaxOnRow(int row, int occupied) {
        if ((510 & occupied) == 0) // 0111111110
            return 2;
        if ((480 & occupied) == 0) // 0111100000
            return 1;
        if ((30 & occupied) == 0)  // 0000011110
            return 1;
        if ((120 & occupied) == 0) // 0001111000
            return 1;
        return 0;
    }

    public int solution(int N, string S) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        Dictionary<int, int> occupied = Parse(S);
        int max = 0;
        for (int row = 1; row <= N; row++) {
            max += CalculateMaxOnRow(row, occupied.ContainsKey(row) ? occupied[row] : 0);
        }
        return max;
    }
}


class Tests { 
    private static void Main() {
        Trace.Listeners.Add(new ConsoleTraceListener());

        AssertEquals(new Solution().solution(2, "1A 2F 1C"), 2);
        AssertEquals(new Solution().solution(2, ""), 4);
        AssertEquals(new Solution().solution(2, "1C 1G 2D 2H"), 0);
    }
        AssertEquals(new Solution().solution(2, "2F 1C "), 2);

    public static void AssertEquals<T>(T left, T right) {
        Trace.WriteLine("Asserting");
        Trace.Assert(object.Equals(left, right), $"Failed assert equals. {left} != {right}");
        Trace.WriteLine("done");
    }
}
