/*

 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;

public class Solver
{
    const int CASES = 3;
    const ulong INF = System.Int64.MaxValue; 

    public ulong MinOC(ulong[] oc, ulong h)
    {
        return Enumerable
            .Range(0, CASES)
            .Where(c => oc[c*2] != h)
            .Select(c => oc[c*2 + 1])
            .Min();
    }

    public ulong SumCheck(ulong a, ulong b)
    {
        if (a >= INF || b >= INF || a+b >= INF)
            return INF;
        return a + b; 
    }

    public void Solve()
    {
        int queries = ReadInt();
        foreach(var query in Enumerable.Range(0, queries))
        {
            int n = ReadInt();
            uint[] A = Init<uint>(n*2);
            for (int i = 0; i < n; i++)
            {
                A[i*2] = (uint)ReadInt();
                A[i*2 + 1] = (uint) ReadInt();
            }

            ulong[] oc = Init<ulong>(CASES*2);
            for (uint i = 0; i < CASES; i++)
            {
                oc[i*2] = A[0] + i;
                oc[i*2+1] = A[1] * i;
            }
            ulong[] nextoc = Init<ulong>(CASES*2);
            for (int i = 1; i < n; i++)
            {
                ulong a = A[i*2];
                ulong b = A[i*2+1];
                for (uint c = 0; c < CASES; c++)
                {
                    nextoc[c*2] = a + c;
                    nextoc[c*2 + 1] = SumCheck(MinOC(oc, a + c), c*b);
                }
                ulong[] t = oc;
                oc = nextoc;
                nextoc = t;
            }
            ulong ans = Enumerable.Range(0, CASES).Select(c => oc[c*2 + 1]).Min();
            Write(ans);
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
