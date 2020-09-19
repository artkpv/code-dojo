#define TRACE
#define DEBUG
/*
Author: w1ld [dog] inbox [dot] ru

https://codeforces.com/contest/1288/problem/C

Idea 1

    sum (le[m,i] * ge[m,i]) for i in 1..n
    where 
      le[x, y] - num of arrays of len x which has 1 or more y elements and y is the greatest element.
      ge[x, y] - num of arrays of len x which has 0 or more y elements and y is the lowest element.
   
Idea 2

    a1 a2 a3 .. a{m} b{m} b{m-1} b{m-2} .. b2 b1

    ordered, not growing, 2m length

*/

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using static System.Math;

public class Solver
{
    private long Factorial(long x1, long x2,  long MOD)
    {
        Debug.Assert(x1 >= 0);
        long y = 1;
        while (x1 <= x2) 
        {
            y = y * x1 % MOD;
            x1 += 1;
        }
        return y;
    }

    public void Solve()
    {
        const int MOD = (int)1e9 + 7;
        int n = ReadInt();
        int m = ReadInt();

        //  1 approach
        //  Time: ~(n * 2m)
        //  Space: n*2m
        int[][] le = new int[2*m+1][];
        for (int i = 0; i <= 2*m; i++)
        {
            le[i] = new int[n+1];
            le[i][0] = 1;
            le[i][1] = 1;
        }
        for (int j = 1; j <= n; j++)
        {
            le[0][j] = 1;
            le[1][j] = j;
        }
        for (int i = 2; i <= 2*m; i++)
            for (int j = 2; j <= n; j++)
                le[i][j] = (le[i][j-1] + le[i-1][j]) % MOD; 

        Write(le[2*m][n]);

        // 2 approach
        // Time: ~ (n + m)
        // Space: 1
        
        //long nom = Factorial(n, n + 2 * m - 1, MOD);
        //long den = Factorial(1, 2*m, MOD);
        //if (den > nom)
            //nom += MOD;
        //Write( (nom / den) % MOD);  // ERROR. No sense to divide.
    }

    private void Print(int[][] tda)
    {
        Debug.WriteLine("");
        for (int i = 0; i < tda.Length; i++)
            Debug.WriteLine(string.Join(" ", tda[i]));
    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    static void Main()
    {
        Debug.Listeners.Clear();
        Debug.Listeners.Add(new ConsoleTraceListener());
        Trace.Listeners.Clear();
        Trace.Listeners.Add(new ConsoleTraceListener());

        reader = new StreamReader(Console.OpenStandardInput());
        writer = new StreamWriter(Console.OpenStandardOutput());
        new Solver().Solve();
        reader.Close();
        writer.Close();
    }

    #endregion

    #region Read / Write
    private static Queue<string> currentLineTokens = new Queue<string>();
    private static string[] ReadAndSplitLine() { return reader.ReadLine().Split(new[] { ' ', '\t', }, StringSplitOptions.RemoveEmptyEntries); }
    public static string ReadToken() { while (currentLineTokens.Count == 0)currentLineTokens = new Queue<string>(ReadAndSplitLine()); return currentLineTokens.Dequeue(); }
    public static int ReadInt() { return int.Parse(ReadToken()); }
    public static long ReadLong() { return long.Parse(ReadToken()); }
    public static double ReadDouble() { return double.Parse(ReadToken(), CultureInfo.InvariantCulture); }
    public static int[] ReadIntArray() { return ReadAndSplitLine().Select(int.Parse).ToArray(); }
    public static long[] ReadLongArray() { return ReadAndSplitLine().Select(long.Parse).ToArray(); }
    public static double[] ReadDoubleArray() { return ReadAndSplitLine().Select(s => double.Parse(s, CultureInfo.InvariantCulture)).ToArray(); }
    public static int[][] ReadIntMatrix(int numberOfRows) { int[][] matrix = new int[numberOfRows][]; for (int i = 0; i < numberOfRows; i++)matrix[i] = ReadIntArray(); return matrix; }
    public static int[][] ReadAndTransposeIntMatrix(int numberOfRows)
    {
        int[][] matrix = ReadIntMatrix(numberOfRows); int[][] ret = new int[matrix[0].Length][];
        for (int i = 0; i < ret.Length; i++) { ret[i] = new int[numberOfRows]; for (int j = 0; j < numberOfRows; j++)ret[i][j] = matrix[j][i]; } return ret;
    }
    public static string[] ReadLines(int quantity) { string[] lines = new string[quantity]; for (int i = 0; i < quantity; i++)lines[i] = reader.ReadLine().Trim(); return lines; }
    public static void WriteArray<T>(IEnumerable<T> array) { writer.WriteLine(string.Join(" ", array)); }
    public static void Write(params object[] array) { WriteArray(array); }
    public static void WriteLines<T>(IEnumerable<T> array) { foreach (var a in array)writer.WriteLine(a); }
    private class SDictionary<TKey, TValue> : Dictionary<TKey, TValue>
    {
        public new TValue this[TKey key]
        {
            get { return ContainsKey(key) ? base[key] : default(TValue); }
            set { base[key] = value; }
        }
    }
    private static T[] Init<T>(int size) where T : new() { var ret = new T[size]; for (int i = 0; i < size; i++)ret[i] = new T(); return ret; }
    #endregion
}
