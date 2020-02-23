#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

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
    private bool IsPs(string a, string b)
    {
        for (int i = 0; i < a.Length; i++)
        {
            if (a[i] != b[b.Length - 1 - i])
                return false;
        }
        return true;
    }

    private bool IsP(string a)
    {
        for (int i = 0; i < a.Length / 2; i++)
        {
            if (a[i] != a[a.Length - 1 - i])
                return false;
        }
        return true;
    }

    public void Solve()
    {
        int n = ReadInt();
        int m = ReadInt();
        string[] arr = new string[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = ReadToken();
        }

        int[] taken = new int[n];
        for (int i = 0; i < n; i++)
        {
            taken[i] = -1;
        }

        int count = 0;
        string some = null;
        for (int i = 0; i < n; i++)
        {
            if (taken[i] != -1)
                continue;
            bool found = false;
            for (int j = i+1; !found && j < n; j++)
            {
                if (taken[j] == -1)
                {
                    if (IsPs(arr[i], arr[j]))
                    {
                        taken[i] = j;
                        taken[j] = i;
                        count += 1;
                        found = true;
                    }
                }
            }
            if (!found && some == null && IsP(arr[i]))
                some = arr[i];
        }

        if (count == 0 && some == null)
        {
            Write(0);
        }
        else
        {
            Write(count * 2 * m + (some != null? some.Length : 0));
            var left = new StringBuilder();
            var right = new StringBuilder();
            bool[] took = new bool[n];
            for (int i = 0; i < n; i++)
            {
                if (taken[i] != -1 && !took[i])
                {
                    took[i] = true;
                    took[taken[i]] = true;
                    left.Append(arr[i]);
                    right.Append(string.Concat(arr[taken[i]].Reverse()));
                }
            }
            if (some != null)
                left.Append(some);
            left.Append(string.Concat(right.ToString().Reverse()));
            Write(left.ToString());
        }

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
