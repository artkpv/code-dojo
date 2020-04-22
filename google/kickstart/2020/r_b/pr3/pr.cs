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

namespace CFr_bpr3
{
    public class Solver
    {
        string S;
        long x = 0;
        long y = 0;
        int MAX = (int)1e9;
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                x = 0;
                y = 0;
                S = ReadToken();
                Run(1, 0);

                Write($"Case #{test + 1}: {x+1} {y+1}");
            }
        }

        private int Run(int n, int start)
        {
            int i = start;
            long startx = x;
            long starty = y;
            long vx = 0;
            long vy = 0;
            while (i < S.Length && S[i] != ')')
            {
                if ('0' <= S[i] && S[i] <= '9')
                {
                    long beforex = x;
                    long beforey = y;
                    i = Run(S[i] - '0', i + 2);
                    vx += x - beforex;
                    vy += y - beforey;
                    i += 1;
                }
                else
                {
                    if (S[i] == 'S')
                    {
                        y = (y + 1) % MAX;
                        vy += 1;
                    }
                    else if (S[i] == 'N')
                    {
                        y = (MAX + y - 1) % MAX;
                        vy -= 1;
                    }
                    else if (S[i] == 'E')
                    {
                        x = (x + 1) % MAX;
                        vx += 1;
                    }
                    else if (S[i] == 'W')
                    {
                        x = (MAX + x - 1) % MAX;
                        vx -= 1;
                    }
                    i += 1;
                }
            }
            x = (startx + vx * n) % MAX;
            x = x < 0 ? x + MAX : x;
            y = (starty + vy * n) % MAX;
            y = y < 0 ? y + MAX : y;

            return i;
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
