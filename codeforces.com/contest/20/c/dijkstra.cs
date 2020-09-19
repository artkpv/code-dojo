#define TRACE
#define DEBUG
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
    List<int>[] adj = null;
    Dictionary<(int, int), int> weights = new Dictionary<(int, int), int>();
    int verticesNum = -1;
    int edgesNum = -1;

    private IEnumerable<int> SP(int source, int target)
    {
        var pq = new SortedDictionary<(long dist, int v), int>();
        var v2pq = new Dictionary<int, (long, int)>();
        var distTo = new long[verticesNum+1];
        for (int i = 0; i <= verticesNum; i++)
            distTo[i] = long.MaxValue;
        var edgeTo = new Dictionary<int, int>();

        distTo[source] = 0;
        pq.Add((0, source), 0);
        v2pq[source] = (0, source);

        while (pq.Any())
        {
            (long distToV, int v) d_v = pq.Keys.First();
            pq.Remove(d_v);
            int v = d_v.v;
            if (v == target)
                break;
            // Debug.WriteLine($" pq pop: {v}. PQ: {string.Join(' ', pq)}");
            if (adj[v] == null)
                continue;
            foreach (int w in adj[v])
            {
                int ew = weights[(Min(v, w), Max(v, w))];
                if (distTo[w] > distTo[v] + ew)
                {
                    distTo[w] = distTo[v] + ew;
                    edgeTo[w] = v;

                    if (v2pq.ContainsKey(w))
                    {
                        Debug.Assert(pq.ContainsKey(v2pq[w]));
                        pq.Remove(v2pq[w]);
                    }
                    pq.Add((distTo[w], w), w);
                    v2pq[w] = (distTo[w], w);
                }
            }
        }

        if (edgeTo.ContainsKey(target))
        {
            var path = new Stack<int>();
            int x = target;
            while (x != source)
            {
                path.Push(x);
                x = edgeTo[x];
            }
            path.Push(source);
            return path;
        }
        return new int[0];
    }

    public void Solve()
    {
        verticesNum = ReadInt();
        edgesNum = ReadInt();
        adj = new List<int>[verticesNum+1];
        for (int i = 0; i < edgesNum; i++)
        {
            int v = ReadInt();
            int w = ReadInt();
            int eweight = ReadInt();
            if (adj[v] == null)
                adj[v] = new List<int>();           
            if (adj[w] == null)
                adj[w] = new List<int>();           
            adj[v].Add(w);
            adj[w].Add(v);
            weights[(Min(v, w), Max(v, w))] = eweight;
        }
        
        IEnumerable<int> path = SP(1, verticesNum);
        if (!path.Any())
            Write("-1");
        else
            Write(string.Join(" ", path));
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
