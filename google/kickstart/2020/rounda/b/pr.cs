#define TRACE
#undef DEBUG
/*
Author: Artyom K. <www.artkpv.net>

30 ^ 50

N K P
Take P plates from N stacks of K plates. Max beauty.
K <= 30, N <= 50

## Idea 1, BF
O(K^N)
Test set 1 - 30*30*30 = 27 000
Test set 2 - 30^50 ~= 3^50 * 10^50 = 9^25 * 10^50 ~= 10^75


## Idea 2
DP[i][j] - max sum for first i stacks when j plates in total.

DP[i][j] = 
    for t in 0..K:
        DP[i][j] = Max(DP[i][j], stack[i][t] + DP[i-1][j-t])

Ans = DP[N][K]

N * N * K * K <= 75 000 * 30 = 2 250 000



2 4 5
10 10 100 30
80 50 10 50


3 2 3 
80 80
15 50
20 10

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

namespace CFroundab
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int N = ReadInt();
                int K = ReadInt();
                int P = ReadInt();
                long[][] stacks = new long[N][];
                for (int i = 0; i < N; i++)
                    stacks[i] = 
                        new List<long> {0}.Concat(
                            ReadIntArray().Select(e => (long)e)
                        ).ToArray();
                for (int i = 0; i < N; i++)
                {
                    for (int j = 1; j < K+1; j++)
                    {
                        stacks[i][j] += stacks[i][j-1];
                    }
                }

                long[][] dp = new long[N][];
                for (int i = 0; i < N; i++)
                    dp[i] = new long[P+1];

                for (int j = 0; j < P+1; j++)
                {
                    dp[0][j] = j < K + 1 ? stacks[0][j] : dp[0][j-1];
                }

                for (int i = 1; i < N; i++)
                {
                    for (int j = 0; j < P+1; j++)
                    {
                        for (int t = 0; t <= Min(j, K); t++)
                        {
                            dp[i][j] = Max(dp[i][j], stacks[i][t] + dp[i-1][j-t]);
                        }
                    }
                }

                Write($"Case #{test+1}: {dp[N-1][P]}");
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

/*

   0 10 20 120 150
   0 80 130 140 190

   0 0 0


 */
