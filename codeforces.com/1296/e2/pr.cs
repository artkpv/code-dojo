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
    public void Solve()
    {
        int n = ReadInt();
        string arr = ReadToken();
        const int R = 'z' - 'a' + 1;
        int[] count = new int[R];
        for (int i = 0; i < n; i++)
        {
            count[arr[i] - 'a'] += 1;
        }
        int[] index = new int[R + 1];
        for (int i = 0; i < R; i++)
        {
            index[i + 1] = index[i] + count[i];            
        }
        int[] strinx = new int[R + 1];
        for (int i = 0; i < R; i++)
            strinx[i] = index[i];

        //int[] sorted = new int[n];
        //for (int i = 0; i < R; i++)
        //{
            //for (int j = index[i]; j < index[i+1]; j++)
            //{
                //sorted[j] = i;                
            //}
        //}

        int[] colors = new int[n];
        for (int i = 0; i < n; i++)
            colors[i] = 1;

        int sinx = 0;
        var next = new SortedDictionary<int, int>();
        int counter = 1;
        int maxcol = 1;
        while (sinx < n)
        {
            colors[sinx] = counter;
            if (sinx != index[arr[sinx] - 'a'])
            {
                counter += 1;
                index[arr[sinx] - 'a'] += 1;
                next.Add(index[arr[sinx] - 'a'], 0);
            }
            if (next.Any() && sinx == next.First().Key)
            {
                counter -= 1;
                next.Remove(next.First().Key);
            }
            maxcol = Max(maxcol, counter);
            sinx += 1;
        }
        Write(maxcol);
        WriteArray(colors);
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
