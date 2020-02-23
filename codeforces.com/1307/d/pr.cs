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

namespace CFcodeforces.com1307
{
    public class Solver
    {
        public void Solve()
        {
            int V = ReadInt();
            int E = ReadInt();
            int kkk = ReadInt();
            var unqVertexes = new HashSet<int>(ReadIntArray());
            

            List<int>[] adj = null;
            adj = new List<int>[V+1];
            for (int i = 0; i <= V; i++)
                adj[i] = new List<int>();

            for (int i = 0; i < E; i++)
            {
                int v = ReadInt();
                int u = ReadInt();
                adj[v].Add(u);            
                adj[u].Add(v);
            }

            Queue<int> q = new Queue<int>();
            q.Enqueue(1);
            int[] distto = new int[V+1];
            const int INF = int.MaxValue;
            for (int i = 1; i <= V; i++)
            {
                distto[i] = INF;
            }
            distto[1] = 0;
            var closest = new SortedDictionary<(int, int), int>();
            while (q.Any())
            {
                int v = q.Dequeue();
                foreach (int u in adj[v])
                {
                    if (distto[u] > distto[v] + 1)
                    {
                        distto[u] = distto[v] + 1;
                        if (unqVertexes.Contains(u))
                            closest.Add((distto[u], u), u);
                        q.Enqueue(u);
                    }
                }
            }

            int spToV = distto[V];

            q = new Queue<int>();
            q.Enqueue(V);
            int[] distto2 = new int[V+1];
            int best = int.MaxValue;
            for (int i = 1; i <= V; i++)
            {
                distto2[i] = INF;
            }
            distto2[V] = 0;
            while (q.Any())
            {
                int v = q.Dequeue();
                if (unqVertexes.Contains(v))
                {
                    closest.Remove((distto[v], v));
                    if (closest.Any())
                        best = Min(distto2[v] + 1 + closest.Last().Key.Item1, best);
                }
                foreach (int u in adj[v])
                {
                    if (distto2[u] > distto2[v] + 1)
                    {
                        distto2[u] = distto2[v] + 1;
                        q.Enqueue(u);
                    }
                }
            }

            Write(Min(best, spToV));
            
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
}
