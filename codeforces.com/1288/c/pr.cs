#define TRACE
#undef DEBUG
/*
Author: w1ld [dog] inbox [dot] ru

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
    public void Solve()
    {
        const int MOD = (int)1e9 + 7;
        int n = ReadInt();
        int m = ReadInt();

        int[][] le = new int[m+1][];
        for (int i = 0; i <= m; i++)
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
        for (int i = 2; i <= m; i++)
            for (int j = 2; j <= n; j++)
                le[i][j] = (le[i][j-1] + le[i-1][j]) % MOD; 
        // le
        // 2 2 
        // 0 0 0 
        // 0 1 2 
        // 0 1 3 

        int[][] ge = new int[m+1][];
        for (int i = 0; i <= m; i++)
        {
            ge[i] = new int[n+1];
            ge[i][n] = 1;
        }
        for (int j = n; j >= 1; j--)
            ge[1][j] = (n - j + 1);
        for (int i = 2; i <= m; i++)
            for (int j = n-1; j >= 1; j--)
                ge[i][j] = (ge[i][j+1] + ge[i-1][j]) % MOD;

        // ge
        // 2 2 
        // 0 0 1 
        // 0 2 1 
        // 0 3 1 

        int ans = 0;
        for (int j = 1; j <= n; j++)
            ans = (ans + le[m-1][j] * ge[m][j] % MOD) % MOD;

        // 

        Write(ans);
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
