#define TRACE
#undef DEBUG
/*
Author: Artyom K. <www.artkpv.net>


A*C*E
*B*D

A * C * E

*AB*
*BA*
*ABBA*

 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading;
using System.Diagnostics;
using static System.Math;

namespace CFround_apr1
{
    public class Solver
    {
        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int n = ReadInt();
                string[] strs = new string[n];
                for (int i = 0; i < n; i++)
                {
                    strs[i] = ReadToken();
                }

                List<char> pref = new List<char>();
                List<char> suffix = new List<char>();
                List<char> mid = new List<char>();
                bool possible = true;
                for (int i = 0; possible && i < n; i++)
                {
                    int l = strs[i].Length;
                    int j = 0;
                    for (; possible && j < l && strs[i][j] != '*'; j++)
                    {
                        if (j < pref.Count)
                            possible = strs[i][j] == pref[j];
                        else
                            pref.Add(strs[i][j]);
                    }
                    int jj = 0;
                    for(; possible && 0 <= l - 1 - jj && strs[i][l - 1 - jj] != '*'; jj += 1)
                    {
                        if (jj < suffix.Count)
                            possible = strs[i][l - 1 - jj] == suffix[jj];
                        else
                            suffix.Add(strs[i][l - 1 - jj]);
                    }
                    for (; possible && j < l - 1 - jj; j += 1)
                        if (strs[i][j] != '*')
                            mid.Add(strs[i][j]);
                }

                if (possible)
                {
                    suffix.Reverse();
                    string ans = 
                        new string(pref.Concat(mid).Concat(suffix).ToArray());
                    Write($"Case #{test + 1}: {ans}");
                }
                else
                    Write($"Case #{test + 1}: *");
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
