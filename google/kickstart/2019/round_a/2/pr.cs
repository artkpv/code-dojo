#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

TODO: TLE. 
See editorial at https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/000000000006987d

1) Make multisource BFS to compute distances, ~N time.
2) Use Binary Search to answer if we set a new office will all locations be at most K distance. For this for each cell compute max and min location a new office can have (because any such location needs an office within K distance). This is O(Nlog(N)) time.

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

namespace CFround_a2
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int rows = ReadInt();
                int cols = ReadInt();
                string[] field = new string[rows];
                int[][] dist = new int[rows][];
                const int INF = int.MaxValue;
                var q = new Queue<Tuple<int, int>>();
                for (int i = 0; i < rows; i++)
                {
                    field[i] = ReadToken();
                    dist[i] = new int[cols];
                    for (int j = 0; j < cols; j++)
                    {
                        if (field[i][j] == '1')
                        {
                            dist[i][j] = 0;
                            q.Enqueue(Tuple.Create(i, j));
                        }
                        else
                            dist[i][j] = INF;
                    }
                }

                var dir = new[] { 
                    -1, 0,
                    0, 1,
                    1, 0,
                    0, -1
                };

                while (q.Any())
                {
                    Tuple<int, int> v = q.Dequeue();
                    int i = v.Item1;
                    int j = v.Item2;

                    for (int dirI = 0; dirI < 4; dirI++)
                    {
                        int ii = i + dir[dirI * 2];
                        int jj = j + dir[dirI * 2 + 1];
                        if (! (0 <= ii && ii < rows && 0 <= jj && jj < cols))
                            continue;
                        if (dist[ii][jj] == INF)
                        {
                            dist[ii][jj] = dist[i][j] + 1;
                            q.Enqueue(Tuple.Create(ii, jj));
                        }
                    }
                }


                Func<int, bool> atMostK = (k) =>
                {
                    int x2plusY2Max = int.MaxValue;
                    int x2plusY2Min = int.MinValue;
                    int x2minusY2Max = int.MaxValue;
                    int x2minusY2Min = int.MinValue;

                    for (int i = 0; i < rows; i++)
                    {
                        for (int j = 0; j < cols; j++)
                        {
                            if (dist[i][j] > k)
                            {
                                x2plusY2Min = Max(x2plusY2Min, i + j - k);
                                x2plusY2Max = Min(x2plusY2Max, i + j + k);
                                x2minusY2Min = Max(x2minusY2Min, j - i - k);
                                x2minusY2Max = Min(x2minusY2Max, j - i + k);
                            }
                        }
                    }
                    return x2plusY2Min <= x2plusY2Max && x2minusY2Min <= x2minusY2Max;
                };
                
                int lo = 0;
                int hi = cols+rows-1;
                while (lo < hi)
                {
                    int mid = (lo + hi) / 2;
                    //Write($" lo={lo} hi={hi}");
                    if (atMostK(mid))
                        hi = mid;
                    else
                        lo = mid + 1;
                }
                Write($"Case #{test+1}: {lo}");
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
}
