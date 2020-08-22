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

namespace CFyandex_shad_2020l
{
    public class Solver
    {
        public void Solve()
        {
            int W = ReadInt();
            int H = ReadInt();
            int a = ReadInt();
            int b = ReadInt();
            int n = ReadInt();
            int[] lX = new int[n];
            int[] lY = new int[n];
            int[] rX = new int[n];
            int[] rY = new int[n];
            int[] byRx = new int[n];
            int[] byRy = new int[n];
            int[] byLx = new int[n];
            int[] byLy = new int[n];
            for (int i = 0; i < n; i++)
            {
                byLx[i] = i;
                byLy[i] = i;
                byRx[i] = i;
                byRy[i] = i;
                lX[i] = ReadInt();
                lY[i] = ReadInt();
                rX[i] = ReadInt();
                rY[i] = ReadInt();
            }
            Array.Sort(byLx, Comparer.Create<int>((i, j) => lX[i].CompareTo(lX[j])));
            Array.Sort(byLy, Comparer.Create<int>((i, j) => lY[i].CompareTo(lY[j])));
            Array.Sort(byRx, Comparer.Create<int>((i, j) => rX[i].CompareTo(rX[j])));
            Array.Sort(byRy, Comparer.Create<int>((i, j) => rY[i].CompareTo(rY[j])));

            int ans = int.MinValue;
            int ansXl = 0;
            int ansYl = 0;
            int ansXr = 0;
            int ansYr = 0;
            for (int i = 0; i < n + 1; i++)
            {
                for (int j = 0; j < n + 1; j++)
                {
                    int ly = i == 0 ? 0 : byRy[i-1]; 
                    int lx = j == 0 ? 0 : byRx[j-1];
                    int rx = W;
                    int ry = H;
                    for (int ii = 0; ii < n + 1; ii++)
                    {
                        if (byLy[ii] < 

                        for (int jj = 0; jj < n + 1; jj++)
                        {

                        }
                    }
                }
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
