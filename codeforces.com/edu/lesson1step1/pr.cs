#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

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

namespace EduLesson1Step1
{
    public class Solver
    {
        public void Solve()
        {
            // https://source.dot.net/#System.Private.CoreLib/Array.cs,2230
            string s = ReadToken();
            int n = s.Length;
            int[] ids = new int[n+1];
            int[] eq = new int[n+1];
            int[] eqAux = new int[n+1];
            for (int i = 0; i < n+1; i++)
            {
                ids[i] = i;
                eq[i] = i < n ? s[i] - '$' : 0;
            }
            WriteArray(ids);
            WriteArray(eq);
            Array.Sort(ids, eq, Comparer<int>.Create((x, y) => 
            {
                Write($"x={x}, y={y}, {string.Join(" ", ids)}, {string.Join(" ", eq)}");
                return eq[x] - eq[y];
            }));

            int k = 0;
            while ((1 << k) < n)
            {
                k += 1;
                WriteArray(ids);
                WriteArray(eq);
                Array.Sort(ids, eq, Comparer<int>.Create((x, y) => {
                    if (eq[x] != eq[y])
                        return eq[x] - eq[y];

                    int xx = (x + (1 << k)) % (n+1);
                    int yy = (y + (1 << k)) % (n+1);
                    return eq[xx] - eq[yy];
                }));
                int eqId = 0;
                eqAux[0] = eqId;
                for (int i = 1; i < n+1; i++)
                {
                    int previi = (ids[i-1] + (1 << k)) % (n+1);
                    int ii = (ids[i] + (1 << k)) % (n+1);
                    if (!(eq[i-1] == eq[i] && eq[previi] == eq[ii]))
                        eqId += 1;
                    eqAux[i] = eqId;
                }
                int[] t = eq;
                eq = eqAux;
                eqAux = t;
            }

            WriteArray(ids);
        }

        #region Main

        protected static TextReader reader;
        protected static TextWriter writer;
        static void Main()
        {
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
