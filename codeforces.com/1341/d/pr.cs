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

namespace CF1341d
{
    public class Solver
    {
        int[] valid = new[] {
            0b1110111,
            0b0010010,
            0b1011101,
            0b1011011,
            0b0111010,
            0b1101011,
            0b1101111,
            0b1010010, // 7
            0b1111111, // 8
            0b1111011, // 9
        };

        const int LEN = 7;

        int[][] possible = new int[(1 << LEN)][];

        public Solver()
        {
            for (int from_ = 0; from_ < (1 << LEN); from_++)
            {
                const int ChangesNumber = 8;
                possible[from_] = new int[ChangesNumber];
                for (int jj = 0; jj < ChangesNumber; jj++)
                {
                    possible[from_][jj] = -1;
                }

                for (int toInx = 0; toInx < valid.Length; toInx++)
                {
                    int to_ = valid[toInx];
                    int count = 0;
                    for (int i = 0; count >= 0 && i < LEN; i++)
                    {
                        if (((from_ >> i) & 1) == 1 && ((to_ >> i) & 1) == 0)
                            count = -1;
                        else
                        {
                            if ((((from_ >> i) & 1) != ((to_ >> i) & 1)))
                                count += 1;
                        }
                    }
                    if (count >= 0)
                    {
                        if (possible[from_][count] == -1 || Array.IndexOf(valid, possible[from_][count]) < toInx)
                            possible[from_][count] = to_;
                    }
                }
            }
        }

        private int ToD(string d)
        {
            int dig = 0;
            for (int i = 0; i < LEN; i++)
            {
                dig |= (d[i] == '1' ? (1 << (LEN - i - 1)) : 0);
            }
            return dig;
        }

        private int GetD(int d, int p)
        {
            return possible[d][p];
        }

        public void Solve()
        {
            int N = ReadInt();
            int K = ReadInt();
            int[] D = new int[N];
            for (int i = 0; i < N; i++)
                D[i] = ToD(ReadToken());

            bool[][] dp = new bool[N + 1][];
            dp[0] = new bool[K + 1];
            dp[0][0] = true;
            for (int i = 1; i < N + 1; i++)
            {
                dp[i] = new bool[K + 1];
                for (int j = 0; j < K + 1; j++)
                {
                    for (int p = 0; !dp[i][j] && p <= Min(j, LEN); p++)
                    {
                        int d = GetD(D[N - i], p);
                        //System.Diagnostics.Trace.WriteLine($"D[N-i]={D[N-i]} p={p} d={d} dp[i-1][j-p]={dp[i-1][j-p]}");
                        dp[i][j] = d != -1 && dp[i - 1][j - p];
                    }
                }
                //System.Diagnostics.Trace.WriteLine($"dp[i]={string.Join(' ', dp[i])} D[i]={D[N-i]} ");
            }

            if (!dp[N][K])
                Write(-1);
            else
            {
                int[] ans = new int[N];
                int i = 0;
                while (i < N)
                {
                    int max = -1;
                    int used = 0;
                    for (int p = 0; p <= Min(LEN, K); p++)
                    {
                        if (!dp[N - i - 1][K - p])
                            continue;
                        int digit = GetD(D[i], p);
                        int digitValue = Array.IndexOf(valid, digit);
                        if (max < digitValue)
                        {
                            used = p;
                            max = digitValue;
                        }
                    }
                    K -= used;
                    ans[i] = max;
                    i += 1;
                }
                Write(string.Concat(ans));
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
        public static string ReadToken() { while (currentLineTokens.Count == 0) currentLineTokens = new Queue<string>(ReadAndSplitLine() ?? new[] { "" }); return currentLineTokens.Dequeue(); }
        public static int ReadInt() { return int.Parse(ReadToken()); }
        public static long ReadLong() { return long.Parse(ReadToken()); }
        public static double ReadDouble() { return double.Parse(ReadToken(), CultureInfo.InvariantCulture); }
        public static int[] ReadIntArray() { return ReadAndSplitLine().Select(int.Parse).ToArray(); }
        public static long[] ReadLongArray() { return ReadAndSplitLine().Select(long.Parse).ToArray(); }
        public static double[] ReadDoubleArray() { return ReadAndSplitLine().Select(s => double.Parse(s, CultureInfo.InvariantCulture)).ToArray(); }
        public static int[][] ReadIntMatrix(int numberOfRows) { int[][] matrix = new int[numberOfRows][]; for (int i = 0; i < numberOfRows; i++) matrix[i] = ReadIntArray(); return matrix; }
        public static int[][] ReadAndTransposeIntMatrix(int numberOfRows)
        {
            int[][] matrix = ReadIntMatrix(numberOfRows); int[][] ret = new int[matrix[0].Length][];
            for (int i = 0; i < ret.Length; i++) { ret[i] = new int[numberOfRows]; for (int j = 0; j < numberOfRows; j++) ret[i][j] = matrix[j][i]; }
            return ret;
        }
        public static string[] ReadLines(int quantity) { string[] lines = new string[quantity]; for (int i = 0; i < quantity; i++) lines[i] = reader.ReadLine().Trim(); return lines; }
        public static void WriteArray<T>(IEnumerable<T> array) { writer.WriteLine(string.Join(" ", array)); }
        public static void Write(params object[] array) { WriteArray(array); }
        public static void WriteLines<T>(IEnumerable<T> array) { foreach (var a in array) writer.WriteLine(a); }
        private class SDictionary<TKey, TValue> : Dictionary<TKey, TValue>
        {
            public new TValue this[TKey key]
            {
                get { return ContainsKey(key) ? base[key] : default(TValue); }
                set { base[key] = value; }
            }
        }
        private static T[] Init<T>(int size) where T : new() { var ret = new T[size]; for (int i = 0; i < size; i++) ret[i] = new T(); return ret; }
        #endregion
    }
}
