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

namespace PrB
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 1; test <= tests; test++)
            {
                int W = ReadInt();
                int N = ReadInt();
                long[] X = ReadLongArray();
                Array.Sort(X);
                long sum = X.Sum();
                long avg = (long) Round(sum * 1.0 / W);
                long moves = 0;
                for (int i = 0; i < W; i++)
                    moves += Abs(X[i] - avg);
                int avgI = Array.BinarySearch(X, avg);
                if (avgI < 0)
                    avgI = ~avgI;
                long ans = moves;
                for (int i = 1; i < W; i++)
                {
                    long sum2 = sum - X[i] + X[i] + N;  // TODO. А как же учитывать смещенные?!
                    long avg2 = (long) Round(sum2 * 1.0 / W);
                    int avgI2 = Array.BinarySearch(X, avg2);
                    if (avgI2 < 0)
                        avgI2 = ~avgI2;
                    long delta = Abs(avg2 - avg);
                    long moves2 = moves;
                    if (avgI <= avgI2)
                    {
                        moves += delta * avgI;
                        moves += -delta * (W - avgI2);
                        for (int k = avgI; k < avgI2; k++)
                        {
                            moves = moves - Abs(X[k] - avg) + Abs(X[k] - avg2);
                        }
                    }
                    else // avgI > avgI2
                    {
                        moves += -delta * avgI2;
                        moves += delta * (W - avgI);
                        for (int k = avgI2; k < avgI; k++)
                        {
                            moves = moves - Abs(X[k] - avg) + Abs(X[k] - avg2);
                        }
                    }
                    ans = Min(ans, moves2);
                    avg = avg2;
                    sum = sum2;
                    avgI = avgI2;
                    moves = moves2;
                }
                
                Write("Case #" + test + ": " + ans);
            }
        }

        private bool IsEqual(string s, int i, string other)
        {
            for (int j = 0; j < other.Length; j++)
            {
                if (s[i + j] != other[j])
                    return false;
            }
            return true;
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
