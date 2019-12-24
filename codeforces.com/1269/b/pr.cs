#define TRACE
#undef DEBUG
/*

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

public static class Ext 
{
    public static T GetValueOrDefault<T>(this Dictionary<T, T> d, T k, T def)
    {
        if (d.ContainsKey(k))
            return d[k];
        else
            return def;
    }
}

public class Solver
{
    public void Solve()
    {
        int n = ReadInt();
        int m = ReadInt();
        int[] aArr = ReadIntArray();
        int[] bArr = ReadIntArray();
        var aCount = new Dictionary<int, int>();
        var bCount = new Dictionary<int, int>();
        for (int i = 0; i < n; i++)
            aCount[aArr[i]] = aCount.GetValueOrDefault(aArr[i], 0) + 1;
        for (int i = 0; i < n; i++)
            bCount[bArr[i]] = bCount.GetValueOrDefault(bArr[i], 0) + 1;

        int[] aCountKeys = aCount.Keys.ToArray();
        int[] aCountVal = aCount.Values.ToArray();
        Array.Sort(aCountVal, aCountKeys);
        int[] bCountKeys = bCount.Keys.ToArray();
        int[] bCountVal = bCount.Values.ToArray();
        Array.Sort(bCountVal, bCountKeys);

        int groupNum = 1;
        while (groupNum < aCountVal.Count() && aCountVal[groupNum - 1] == aCountVal[groupNum])
            groupNum++;
        
        Array.Sort(bCountKeys, 0, groupNum);
        Array.Sort(aCountKeys, 0, groupNum);

        long ans = long.MaxValue;
        Func<long, long, long> Diff = (a, b) =>
            a <= b ? b - a : b + m - a;
        for (int i = 0; i < groupNum; i++)
        {
            long diff = Diff(aCountKeys[0], bCountKeys[i]);
            bool found = true;
            for (int j = 0; j < groupNum; j++)
            {
                if (Diff(aCountKeys[j], bCountKeys[(i+j)%groupNum]) != diff)
                {
                    found = false;
                    break;
                }
            }
            if (found)
                ans = Min(ans, diff);
        }
        Debug.WriteLine(groupNum);
        Debug.WriteLine(string.Join(" " ,aCountKeys));
        Debug.WriteLine(string.Join(" " ,bCountKeys));
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
