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
    private List<int>[] _adj = null;

    private (int d, int a, int b) _diameter = (0, 0, 0);

    private bool[] _marked = null;

    private (int d, int v) Diameter(int v)
    {
        int d = 0;
        int fv = v;

        foreach (int w in _adj[v])
        {
            if (_marked[w])
                continue;
            _marked[w] = true;
            (int d2, int v2) = Diameter(w);
            d2 += 1;

            if (_diameter.d < d2 + d)
                _diameter = (d2 + d, fv, v2);

            if (d2 > d)
            {
                d = d2;
                fv = v2;
            }
        }

        return (d, fv);
    }

    public void Solve()
    {
        int n = ReadInt();
        _adj = new List<int>[n+1];
        for (int i = 1; i <= n; i++)
            _adj[i] = new List<int>();
        int v = 0; 

        for (int i = 0; i < n-1; i++)
        {
            v = ReadInt();
            int w = ReadInt();
            _adj[v].Add(w);
            _adj[w].Add(v);
        }

        _marked = new bool[n+1];
        _marked[1] = true;
        Diameter(1);
        Debug.Assert(_diameter.a != 0 && _diameter.b != 0, "invalid diam " + _diameter);
        Debug.WriteLine($"diam {_diameter}");

        for (int i = 0; i < n+1; i++)
            _marked[i] = false;
        var stack = new Stack<int>();
        stack.Push(_diameter.a);
        _marked[_diameter.a] = true;
        int[] edgeto = new int[n+1];
        bool found = false;
        while (stack.Any() && !found)
        {
            v = stack.Pop();
            Debug.Assert(1 <= v && v <= n, v + " should be in range");
            Debug.Assert(_adj[v] != null, v + " should be in adj");
            foreach (int w in _adj[v])
            {
                if (_marked[w])
                    continue;
                _marked[w] = true;
                stack.Push(w);
                edgeto[w] = v;
                if (w == _diameter.b)
                {
                    found = true;
                    break;
                }
            }
        }

        if (_diameter.d == n - 1)
        {
            Write(_diameter.d);
            int a = _diameter.a;
            int b = _diameter.b;
            int c = 1;
            while (c == a || c == b)
                c += 1;
            Write(a, b, c);
            return;
        }

        var q = new Queue<int>();
        int[] dist = new int[n+1];
        for (int i = 0; i < n+1; i++)
            dist[i] = -1;
        HashSet<int> ans = new HashSet<int>();
        v = _diameter.b;
        dist[v] = 0;
        q.Enqueue(v);
        ans.Add(v);
        while (edgeto[v] != 0)
        {
            v = edgeto[v];
            dist[v] = 0;
            q.Enqueue(v);
            ans.Add(v);
        }

        int maxVer = 0;
        int maxDist = 0;
        while (q.Any())
        {
            v = q.Dequeue();
            foreach (int w in _adj[v])
            {
                if (dist[w] == -1)
                {
                    dist[w] = dist[v] + 1;
                    if (maxDist < dist[w])
                    {
                        maxDist = dist[w];
                        maxVer = w;
                    }
                    q.Enqueue(w);
                }
            }
        }

        Write(ans.Count() - 1 + maxDist);
        Write(_diameter.a, _diameter.b, maxVer);
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
