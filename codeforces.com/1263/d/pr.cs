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

public class Solver
{
    private class UF
    {
        private int[] _p;
        private int[] _sz;
        public int CC {get; private set;}
        public UF(int n)
        {
            _p = new int[n];
            _sz = new int[n];
            for (int i = 0; i < n; i++)
            {
                _p[i] = i;
                _sz[i] = 1;
            }
            CC = n;
        }

        public int Find(int id)
        {
            if (_p[id] != _p[_p[id]])
                _p[id] = Find(_p[id]);
            return _p[id];
        }

        public void Union(int a, int b)
        {
            int pa = Find(a);
            int pb = Find(b);
            if (pa == pb)
                return;
            if (_sz[pa] > _sz[pb])
            {
                _p[pb] = pa;
                _sz[pa] += _sz[pb];
            }
            else
            {
                _p[pa] = pb;
                _sz[pb] += _sz[pa];
            }
            CC--;
        }
    }

    public void Solve()
    {
        int n = ReadInt();
        var uf = new UF(n);
        const int R = 26;
        var d = new HashSet<int>[R];
        for (int i = 0; i < R; i++)
            d[i] = new HashSet<int>();
        var symbols = new HashSet<char>();
        for (int i = 0; i < n; i++)
        {
            symbols.Clear();

            foreach(char s in ReadToken())
            {
                if (symbols.Contains(s))
                    continue;
                symbols.Add(s);
                foreach (int other in d[s - 'a'])
                    uf.Union(i, other);
                d[s - 'a'].Add(uf.Find(i));
            }
        }
        Write(uf.CC);
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
