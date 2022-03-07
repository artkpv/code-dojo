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

bl    tr
x1 y1 x2 y2
0 0 1 1
2 3 4 6
0 3 5 9


I2 BS.

For one axis (x or y), for intervals there. For a(x) - number of intervals that ends before x and not at x, b(x) for intervals that start after x and not at x.
Then x is optimal iif a+b is min?

minimaze a+b
can be

8 9 0 1 2 3  x
4 3 3 3 3 4  a+b
0 0 0 3 3 4  a
4 3 3 0 0 0  b
0 6 3 3 6 0  dist to nearest
ans is 10 or 11

9-10
8-10
8-10
11-12
11-13
11-13



1-2 3-4, x = 3
1-2 4-5, 3
1-2 -10-2 ..-2  3-4, x=2, a-b = 1
1-10 11-12,   10 or 11 but 11



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
                int n  = ReadInt();
                Assert(n > 0);
                long[] x1 = new long[n];
                long[] x2 = new long[n];
                long[] y1 = new long[n];
                long[] y2 = new long[n];
                for(int i = 0; i < n; i++)
                {
                    var coordinates = ReadIntArray();
                    x1[i] = coordinates[0];
                    y1[i] = coordinates[1];
                    x2[i] = coordinates[2];
                    y2[i] = coordinates[3];
                }
                Array.Sort(x1);
                Array.Sort(x2);
                Array.Sort(y1);
                Array.Sort(y2);
                long minx = Find(x1, x2);
                long miny = Find(y1, y2);
                Write($"Case #{test}: {minx} {miny}");
            }
        }

        long Find(long[] starts, long[] ends)
        {
            int n = starts.Length;
            Assert(n > 0);
            if (n == 1)
                return starts[0];
            long l = starts[0];
            long r = ends[0];
            //Console.WriteLine($"{string.Join(' ', starts)}");
            //Console.WriteLine($"{string.Join(' ', ends)}");
            long x = r;
            while (l < r)
            {
                x = (r+l) / 2;
                int a = n - BSLeft(starts, x+1);
                int b = BSLeft(ends, x+1);
                if (a - b > 1)
                    l = starts[n - a];
                else if (a - b <= -1)
                    r = ends[b];
                else 
                    break;
            }
            return l;
        }

        int BSLeft(long[] arr, long x)
        {
            int n = arr.Length;
            int l = 0;
            int r = n;
            if (arr[l] == x)
                return l;
            if (arr[n-1] < x)
                return n;
            // Invariant: arr[l] <= x < arr[r]
            while (r - l > 1)
            {
                //Console.WriteLine($"bsleft: {x} {l} {r}");
                int m = (l+r) / 2;
                if (arr[m] < x)
                    l = m;
                else
                    r = m;
            }
            return r;
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
        private static void Assert(bool condition, string msg=null) { if (!condition) throw new Exception(msg); }
        #endregion
    }
}
