#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

)()(()))
 . .....
) )

)))((((

(())()()()
..  .. . .

()()(()))
. . . ...
 ) ) (




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

namespace CF1305b
{
    public class Solver
    {
        public void Solve()
        {
            char[] s = ReadToken().ToCharArray();
            int n = s.Length;
            if (n == 1)
            {
                Write(0);
                return;
            }
            int count = 0;
            var sb = new StringBuilder();
            while (true)
            {
                int[] left = new int[n];
                int[] right = new int[n];
                left[0] = s[0] == '(' ? 1 : 0;
                for (int i = 1; i < n; i++)
                    left[i] = left[i-1] + (s[i] == '(' ? 1 : 0);
                right[n-1] = s[n-1] == ')' ? 1 : 0;
                for (int i = n-2; i >= 0; i--)
                    right[i] = right[i+1] + (s[i] == ')' ? 1 : 0);

                int center = 0;
                for (int i = 1; i < n-1; i++)
                {
                    if (left[center] + right[center + 1] < left[i] + right[i+1])
                        center = i;
                }
                int goodC = Min(left[center], right[center+1]);
                if (goodC == 0)
                    break;
                count += 1;
                var ans1 = new List<int>();
                int rightC = goodC;
                for (int i = n-1; i > center && rightC > 0; i--)
                {
                    if (s[i] == ')')
                    {
                        ans1.Add(i+1);
                        s[i] = '-';
                        rightC -= 1;
                    }
                }
                ans1.Reverse();
                var ans2 = new List<int>();
                int leftC = goodC;
                for (int i = 0; i <= center && leftC > 0; i++)
                {
                    if (s[i] == '(')
                    {
                        ans2.Add(i+1);
                        s[i] = '-';
                        leftC -= 1;
                    }
                }
                sb.AppendLine((goodC * 2).ToString());
                sb.AppendLine(string.Join(" ", ans2) + " " + string.Join(" ", ans1));
            }
            Write(count);
            Write(sb.ToString());
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
