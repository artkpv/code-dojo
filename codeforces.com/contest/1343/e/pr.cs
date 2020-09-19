#define TRACE
#undef DEBUG
/*
Author: Artyom K. <www.artkpv.net>

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

namespace CF1343e
{
    public class Solver
    {
        List<int>[] adj;
        const int MAXV = (int)(2*1e5);

        int[] disttoA = new int[MAXV+1];
        int[] disttoB = new int[MAXV+1];
        int[] disttoC = new int[MAXV+1];
        long[] Psum = new long[MAXV+1];

        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int V = ReadInt();
                int E = ReadInt();
                int A = ReadInt();
                int B = ReadInt();
                int C = ReadInt();
                int[] P = ReadIntArray();
                adj = new List<int>[V+1];
                for (int i = 0; i < E; i++)
                {
                    int v = ReadInt();
                    int u = ReadInt();
                    if (adj[v] == null)
                        adj[v] = new List<int>();
                    if (adj[u] == null)
                        adj[u] = new List<int>();
                    adj[v].Add(u);
                    adj[u].Add(v);
                }

                Array.Sort(P);
                Psum[0] = 0;
                for (int i = 1; i <= E; i++)
                {
                    Psum[i] = P[i-1] + Psum[i-1];
                }

                for (int i = 0; i < V+1; i++)
                {
                    disttoA[i] = int.MaxValue;
                    disttoB[i] = int.MaxValue;
                    disttoC[i] = int.MaxValue;
                }

                var Q = new Queue<int>();
                Q.Enqueue(A);
                disttoA[A] = 0;
                while (Q.Any())
                {
                    int v = Q.Dequeue();
                    foreach (int u in adj[v])
                    {
                        if (disttoA[u] > disttoA[v] + 1)
                        {
                            disttoA[u] = disttoA[v] + 1;
                            Q.Enqueue(u);
                        }
                    }
                }
                Q.Enqueue(C);
                disttoC[C] = 0;
                while (Q.Any())
                {
                    int v = Q.Dequeue();
                    foreach (int u in adj[v])
                    {
                        if (disttoC[u] > disttoC[v] + 1)
                        {
                            disttoC[u] = disttoC[v] + 1;
                            Q.Enqueue(u);
                        }
                    }
                }
                Q.Enqueue(B);
                disttoB[B] = 0;
                long min = long.MaxValue;
                while (Q.Any())
                {
                    int v = Q.Dequeue();

                    int a = disttoA[v];
                    int b = disttoB[v];
                    int c = disttoC[v];

                    if (c+b+a <= E)
                        min = Min(min, Psum[c+b+a] + Psum[b]);
                    //System.Diagnostics.Trace.WriteLine($"a={a} b={b} c={c} min={min} Psum[c b a]={Psum[c+b+a]} Psum b={Psum[b]}");
                    foreach (int u in adj[v])
                    {
                        if (disttoB[u] > disttoB[v] + 1)
                        {
                            disttoB[u] = disttoB[v] + 1;
                            Q.Enqueue(u);
                        }
                    }
                }
                Write(min);
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
        private static string[] ReadAndSplitLine() { return reader.ReadLine()?.Split(new[] { ' ', '\t', }, StringSplitOptions.RemoveEmptyEntries); }
        public static string ReadToken() { while (currentLineTokens.Count == 0)currentLineTokens = new Queue<string>(ReadAndSplitLine() ?? new[] {""}); return currentLineTokens.Dequeue(); }
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
