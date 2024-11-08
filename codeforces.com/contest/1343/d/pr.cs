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

namespace CF1343d
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            const int MAX = (int)(2*1e6);
            int[] cnt = new int[MAX*2+1];
            int[] pref = new int[MAX*2+1];
            //System.Diagnostics.Trace.WriteLine($"MAX={MAX} cnt len={cnt.Length} pref len={pref.Length} ");
            for (int test = 0; test < tests; test++)
            {
                int n = ReadInt();
                int k = ReadInt();
                int[] arr = ReadIntArray();
                for (int i = 0; i <= k*2; i++)
                {
                    cnt[i] = 0;
                    pref[i] = 0;
                }
                for (int i = 0; i < n/2; i++)
                {
                    int l = arr[i];
                    int r = arr[n-i-1];
                    int min = Min(l, r) + 1;
                    int max = Max(l, r) + k;
                    cnt[l + r] += 1;
                    pref[min] += 1;
                    pref[max+1] -= 1;
                }
                for (int i = 1; i <= k*2; i++)
                {
                    pref[i] = pref[i-1] + pref[i];
                }
                int ans = int.MaxValue;
                for (int x = 2; x <= 2*k; x++)
                {
                    int a = cnt[x];
                    int b = pref[x];
                    int c = n/2 - b;
                    ans = Min(ans, 2*c + b - a);
                }
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
