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

namespace CFr_cb
{
    public class Solver
    {

        Queue<int> queue = new Queue<int>();
        HashSet<int> onstack = new HashSet<int>();
        HashSet<int> marked = new HashSet<int>();
        HashSet<int>[] adj = null;

        bool hascycle = false;

        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                int rows = ReadInt();
                int cols = ReadInt();
                string[] field = new string[rows];
                for (int row = 0; row < rows; row++)
                {
                    field[row] = ReadToken();                    
                }

                adj = new HashSet<int>['Z' - 'A' + 2];
                for (int i = 0; i < 'Z' - 'A' + 2; i++)
                    adj[i] = new HashSet<int>();
                for (int row = 0; row < rows-1; row++)
                {
                    for (int col = 0; col < cols; col++)
                    {
                        int a = field[row][col] - 'A' + 1;
                        int b = field[row+1][col] - 'A' + 1;
                        if (a != b && !adj[b].Contains(a))
                            adj[b].Add(a);
                    }
                }
                for (int col = 0; col < cols; col++)
                {
                    int a = field[rows-1][col] - 'A' + 1;
                    if (!adj[0].Contains(a))
                        adj[0].Add(a);
                }
                //for (int i = 0; i < adj.Length; i++)
                //{
                    //if (adj[i].Any())
                        //Trace.WriteLine(string.Join(' ', adj[i]));
                //}
                hascycle = false;
                onstack.Clear();
                queue.Clear();
                marked.Clear();
                DFS(0);

                if (hascycle)
                    Write($"Case #{test+1}: -1");
                else
                {
                    var ans = new StringBuilder();
                    while (queue.Count > 1)
                        ans.Append((char)(queue.Dequeue() - 1 + 'A'));
                    
                    string anss = new string(ans.ToString().Reverse().ToArray());
                    Write($"Case #{test+1}: {anss}");

                }
            }
        }

        void DFS(int v)
        {
            //Trace.WriteLine($" {v} {hascycle} {string.Join(' ', marked)}");
            if (hascycle)
                return;
            if (marked.Contains(v))
                return;
            marked.Add(v);
            onstack.Add(v);
            foreach (int u in adj[v])
            {
                if (onstack.Contains(u))
                    hascycle = true;
                if (!marked.Contains(u))
                    DFS(u);
            }
            queue.Enqueue(v);
            onstack.Remove(v);
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
