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

/*

I1. BF.
T: O(N^5)

for each int1:
    for each other int2 not intersec with int1 where int2 < int1:
        if bananas sum on int1 and int2 == capacity
            cost = int1 + int2
            keep optimal cost

I2. 

c(i, s) - optimal cost to get s banas before at 0..i-1 trees.

for each int1:
    cost is bananas on these trees plus optimal cost before that int1
    keep optimal


 */

namespace PrA
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 1; test <= tests; test++)
            {
                int n = ReadInt();
                int k = ReadInt();
                int[] ban = ReadIntArray();
                int res = int.MaxValue;
                if (ban.Contains(k))
                {
                    res = 1;
                }
                else
                {
                    var left = new Dictionary<int, int>[n];
                    for (int i = 0; i < n; i++) 
                    {
                        left[i] = new Dictionary<int, int>();
                    }
                    for (int i = 0; i < n; i++) 
                    {
                        int sum = 0;
                        for (int j = i; j < n; j++) 
                        {
                            //Console.WriteLine($"{i} {j} {sum} {left[i].Count}");
                            if (j - 1 >= 0)
                            {
                                foreach(var key in left[j-1].Keys)
                                {
                                    if (!left[j].ContainsKey(key))
                                        left[j].Add(key, int.MaxValue);
                                    left[j][key] = Math.Min(left[j][key], left[j-1][key]);
                                }
                            }
                            //Console.WriteLine("Check");
                            if (sum + ban[j] <= k)
                            {
                                // 1. Check if optimal found.
                                sum += ban[j];
                                if (i - 2 >= 0 && left[i-2].ContainsKey(k - sum))
                                {
                                    res = Math.Min(res, j - i + 1 + left[i-2][k - sum]);
                                }
                                else if (sum == k)
                                    res = Math.Min(res, j - i + 1);
                                // 2. Store for future checks.
                                if (0 < sum && sum < k)
                                {
                                    if (!left[j].ContainsKey(sum))
                                        left[j].Add(sum, int.MaxValue);
                                    left[j][sum] = Math.Min(left[j][sum], j - i + 1);
                                }
                            }
                        }
                    }
                }

                Write("Case #" + test + ": " + (res != int.MaxValue ? res : -1));
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
