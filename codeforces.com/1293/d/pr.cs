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
    long Add(long a, long b) =>
        a + b < a || a + b < b ? long.MaxValue : a + b;  

    long Mul(long a, long b) => 
        a * b < a || a * b < b ? long.MaxValue : a * b;  

    public void Solve()
    {
        long x0 = ReadLong();
        long y0 = ReadLong();
        long ax = ReadLong();
        long ay = ReadLong();
        long bx = ReadLong();
        long by = ReadLong();
        long xs = ReadLong();
        long ys = ReadLong();
        long t = ReadLong();
        long x = x0;
        long y = y0;
        Func<(long x, long y), (long x, long y), long> Dist = (p1, p2) =>
            Add(Abs(p1.x - p2.x), Abs(p1.y - p2.y));
        while (true)
        {
            long xyD = Dist((x, y), (xs, ys));
            if (xyD <= t)
                break;
            long xNext = Add(Mul(ax, x), bx);
            long yNext = Add(Mul(ay, y), by);
            if (Dist((xNext, yNext), (xs, ys)) > xyD)
                break;
            x = xNext;
            y = yNext;
        }
        var points = new List<(long, long)>();
        long zd = long.MaxValue;
        int zInx = -1;
        while (true)
        {
            long d = Dist((x, y), (xs, ys));
            if (d > t)
                break;
            if (zd > d)
            {
                zd = d;
                zInx = points.Count();
            }
            points.Add((x, y));
            x = Add(Mul(ax, x), bx);
            y = Add(Mul(ay, y), by);
        }

        if (zInx == -1)
        {
            Write(0);
            return;
        }

        long tt = t - zd;
        long maxCount = 0;
        for (int l = zInx; l >= 0; l--)
        {
            long count = 0;
            for (int r = zInx; r < points.Count(); r++)
            {
                long time = Add(Dist(points[l], points[r]),
                    Min(Dist(points[zInx], points[l]), Dist(points[zInx], points[r])));
                if (time <= tt)
                    maxCount = Max(maxCount, r - l + 1);
            }
        }
        Write(maxCount);
        //Debug.WriteLine($"{string.Join(' ', points)} {zInx} {tt}");
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
