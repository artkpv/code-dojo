#define TRACE
#define DEBUG
/*
Author: Artyom K. <www.artkpv.net>

X = a1*2^0 + a2*2^1 + a3*2^2 ... , a1 a2 a3 .. is {1,-1,0}
Y = ...  other

{X} and {Y} are unique
Find out a1 a2 a3 .. if possible
X = -1e9..1e9
N = log(2e9) = 31

1 2 4 8 16 32 64 128 

odd ? 1 should be there
Sum: (2**8 - 1)

X + Y = a1*2^0 + a2*2^1 + a3*2^2 + ...


(1) BF
O(2^N)

(2)
X Y
   
7,10
W  8,10->4,5
S  4,6->2,3
S  2,4->1,2
E  0,2  0,1
N  0,0


-2 -3
N  -1 -2
W  0 -1
S




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

namespace CFround_bpr1
{
    public class Solver
    {

        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int x = ReadInt();
                int y = ReadInt();

                if (x == 0 && y == 0)
                    Write($"Case #{test + 1}: ");
                else if ((x + y) % 2 == 0)
                    Write($"Case #{test + 1}: IMPOSSIBLE");
                else
                {
                    int dirx = 1;
                    int diry = 1;
                    if (x < 0)
                    {
                        x *= -1;
                        dirx = -1;
                    }
                    if (y < 0)
                    {
                        y *= -1;
                        diry = -1;
                    }
                    var sb = new StringBuilder();
                    while (x != 0 || y != 0)
                    {
                        if (Abs(x + y) <= 1)
                        {
                            if (x == 1)
                                sb.Append("E");
                            else if (x == -1)
                                sb.Append("W");
                            else if (y == 1)
                                sb.Append("N");
                            else
                                sb.Append("S");
                            x = 0;
                            y = 0;
                        }
                        else if (x % 2 != 0)
                        {
                            if ((x + 1 + y) / 2 % 2 != 0)
                            {
                                sb.Append("W");
                                x = (x + 1) / 2;
                            }
                            else
                            {
                                sb.Append("E");
                                x = (x - 1) / 2;
                            }
                            y /= 2;
                        }
                        else
                        {
                            if ((y + 1 + x) / 2 % 2 != 0)
                            {
                                sb.Append("S");
                                y = (y + 1) / 2;
                            }
                            else
                            {
                                sb.Append("N");
                                y = (y - 1) / 2;
                            }
                            x /= 2;
                        }
                    }
                    string NS = "NS";
                    string EW = "EW";
                    string path = new string(sb.ToString().Select(c => {
                        if (dirx == -1 && NS.Contains(c))
                            return NS[(NS.IndexOf(c) + 1) % 2];
                        else if (diry == -1 && EW.Contains(c))
                            return EW[(EW.IndexOf(c) + 1) % 2];
                        return c;
                    }).ToArray());
                    Write($"Case #{test + 1}: {path}");
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
