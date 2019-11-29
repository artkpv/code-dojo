#undef DEBUG
/*
 *
5 6 4 14
1 2 3 4 5
1 5 2
1 2 5
2 3 5
3 5 3


1 5 2
3 5 3
2 3 5
1 2 5

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
        int solNum = ReadInt();
        int points = ReadInt();
        int trNum = ReadInt();
        int time = ReadInt();
        int[] A = ReadIntArray();
        Array.Sort(A);
        var lL = new List<int>(trNum);
        var lR = new List<int>(trNum);
        var lD = new List<int>(trNum);
        var traps = new Dictionary<int, int>();
        for (int i = 0; i < trNum; i++)
        {
            int l = ReadInt();
            int r = ReadInt();
            int d = ReadInt();
            if (d > A[0])
            {
                lL.Add(l);
                lR.Add(r);
                lD.Add(d);
                if (!traps.ContainsKey(d))
                    traps[d] = 0;
                traps[d]++;
            }
        }
        var R = lR.ToArray();
        var D = lD.ToArray();
        Array.Sort(R, D);
        int rem = time - points;
        int r_i = 0;
        int x = 0;
        while (r_i < R.Count())
        {
            Debug.WriteLine($"traps={String.Join(" ", traps)} ({traps.Count()})");
            Debug.WriteLine($"D={String.Join(" ", D)} ({D.Count()})");
            int dist = R[r_i] - x;
            if (dist + R[r_i] > rem)
                break;
            traps[D[r_i]]--;
            if (traps[D[r_i]] == 0)
                traps.Remove(D[r_i]);
            x += dist;
            rem -= dist;
            r_i++;
        }
        int a_i = 0;
        int maxD = traps.Any() ? traps.Keys.Max() : 0;
        while (a_i < solNum && A[a_i] < maxD)
            a_i++;
        Write(solNum - a_i);
    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    static void Main()
    {
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
