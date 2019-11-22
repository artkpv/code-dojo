/*

   n <= 2* 10^5

9 2
6 19 3 4 4 2 6 7 8

19 8 7 6 6 4 4 3 2
                 2  2 
               3 2  5
             4 3 4  11
           4 4 6 4  18
           ... 



1 - 2
2 - 2 + 3
3 - 4+3 + 2*2 = 11
4 - 4+4 + 2*(3+2) = 18
5 - 6+4 + 2*(4+3) + 3*(2) = 30



I 1
BF
n intervals * n 
N^2
Time: _4e10_

I 2
sum[k] = sum A[k..n]

x[k] = x[k-m] + sum[k]


 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;

public class Solver
{
    public void Solve()
    {
        int n = ReadInt();
        int m = ReadInt();
        int[] arr = ReadIntArray();
        Array.Sort(arr, Comparer<int>.Create((a, b) => -a.CompareTo(b)));
        long[] right = new long[n];
        right[n-1] = arr[n-1];
        for (int i = n-2; i >= 0; i--)
            right[i] = arr[i] + right[i+1];
        long[] x = new long[n];
        for (int i = n-1; i >= 0; i--)
            x[i] = right[i] + (i + m < n ? x[i+m] : 0);
        Array.Reverse(x);
        WriteArray(x);
        /*
         *   19 8 7 6 6 4 4 3 2
         *
         *   0  1  2  3  4  5  6 7 8
         *   59 40 32 25 19 13 9 5 2   right
         *                     11 5 2
         */
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
