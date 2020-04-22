#define TRACE
#define DEBUG
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

namespace CFround_bpr1
{
    public class Solver
    {
        int[] dirs = new[] {0,1, 1,0, 0,-1, -1,0};
        const int MAX = 2000;
        byte[][] field;

        private bool InField(int x, int y)
        {
            return 0 <= x && x < MAX && 0 <= y && y < MAX;
        }

        public void Solve()
        {
            field = new byte[MAX][];
            for (int i = 0; i < MAX; i++)
            {
                field[i] = new byte[MAX];
            }

            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                for (int i = 0; i < MAX; i++)
                {
                    for (int j = 0; j < MAX; j++)
                    {
                        field[i][j] = 0;
                    }
                }
                int sourcex = MAX/2;
                int sourcey = MAX/2;
                int tarx = ReadInt();
                int tary = ReadInt();
                tarx = tarx + MAX/2;
                tary = tary + MAX/2;
                //int md = Abs(tarx) + Abs(tary);
                //if (md % 2 == 0)
                //{
                    //Write($"Case #{test+1}: IMPOSSIBLE");
                    //continue;
                //}
                if (!InField(tarx, tary))
                {
                    // TODO
                    Write($"Case #{test+1}: IMPOSSIBLE");
                    continue;
                }


                var q = new Queue<Tuple<int, int>>();
                var source = Tuple.Create(MAX/2, MAX/2);
                q.Enqueue(source);
                field[sourcex][sourcey] = 1;

                while (field[tarx][tary] == 0 && q.Any())
                {
                    var t = q.Dequeue();
                    int x = t.Item1;
                    int y = t.Item2;
                    for(int dInx = 0; dInx < dirs.Length; dInx += 2)
                    {
                        int xx = x + dirs[dInx] * (1 << (field[x][y] - 1));
                        int yy = y + dirs[dInx+1] * (1 << (field[x][y] - 1));
                        if (!InField(xx, yy))
                            continue;
                        if (field[xx][yy] != 0)
                            continue;
                        field[xx][yy] = (byte)(field[x][y] + 1);
                        q.Enqueue(Tuple.Create(xx, yy));
                    }
                }

                //for (int i = 0; i < MAX; i++)
                //{
                    //WriteArray(field[i]);
                //}
                //continue;

                if (field[tarx][tary] == 0)
                {
                    Write($"Case #{test+1}: IMPOSSIBLE");
                }
                else
                {
                    var sb = new StringBuilder();
                    int x = tarx;
                    int y = tary;
                    while (field[x][y] != 1)
                    {
                        int xx = int.MaxValue, yy = int.MaxValue;
                        for(int dInx = 0; dInx < dirs.Length; dInx += 2)
                        {
                            int pow = field[x][y] - 1;
                            xx = x + dirs[dInx] * (1 << (pow -1));
                            yy = y + dirs[dInx+1] * (1 << (pow - 1));
                            if (!InField(xx, yy))
                                continue;
                            if (field[xx][yy] + 1 == field[x][y])
                                break;
                        }
                        if (xx == int.MaxValue || yy == int.MaxValue)
                            break;
                        char d;
                        if (x - xx > 0)
                            d = 'E';
                        else if (x - xx < 0)
                            d = 'W';
                        else if (y - yy > 0)
                            d = 'N';
                        else if (y - yy < 0)
                            d = 'S';
                        else 
                            break;
                        sb.Append(d);
                        x = xx;
                        y = yy;
                    }
                    Write($"Case #{test+1}: {new String(sb.ToString().Reverse().ToArray())}");
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
