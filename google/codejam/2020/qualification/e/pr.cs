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

namespace CFqualificatione
{
    public class Solver
    {
        private int N = 0;
        private int K = 0;
        private bool found = false;
        private int[][] LS;
        private bool[][] rowA;
        private bool[][] colA;

        public void Solve()
        {
            int tests = ReadInt();
            for (int test = 0; test < tests; test++)
            {
                N = ReadInt();
                K = ReadInt();
                LS = new int[N][];
                int rem = K % N;
                int div = K / N;
                rowA = new bool[N][];
                colA = new bool[N][];
                for (int i = 0; i < N; i++)
                {
                    LS[i] = new int[N];

                    LS[i][i] = div;
                    if (N - rem < i + 1)
                        LS[i][i] += 1;

                    rowA[i] = Enumerable.Repeat(true, N).ToArray();
                    colA[i] = Enumerable.Repeat(true, N).ToArray();
                    rowA[i][LS[i][i]] = false;
                    colA[i][LS[i][i]] = false;
                }

                found = true;
                
                Fill();

                if (found)
                {
                    Write($"Case #{test+1}: POSSIBLE");
                    for (int i = 0; i < N; i++)
                    {
                        WriteArray(LS[i]);
                    }
                }
                else
                {
                    Write($"Case #{test+1}: IMPOSSIBLE");
                }
            }
        }

        private void Fill()
        {
        }

        private bool IsValid()
        {
            bool[][] rowV = new bool[N][];
            bool[][] colV = new bool[N][];
            for (int i = 0; i < 10; i++)
            {
                
            }
        }


        private bool NextDiag()
        {
            int i = N-1;
            while (i >= 0)
            {
                if (LS[i][i] == 1)
                    i -= 1;
                else
                {
                    LS[i][i] -= 1;
                    int j = i - 1;
                    while (j >= 0)
                    {
                        if (LS[j][j] < N)
                        {
                            LS[j][j] += 1;
                            break;
                        }
                        j -= 1;
                    }
                    if (j < 0)
                        break;
                    return true;
                }
            }
            return false;
        }
        
        void Check(int i, int j)
        {
            if (found)
                return;
            else if (j == N) // Base case, found
            {
                found = true;
            }
            else if (i == j)
            {
                if (i + 1 < N)
                    Check(i + 1, j);
                else
                    Check(0, j + 1);
            }
            else 
            {
                for (int val = 1; val <= N; val++)
                {
                    bool can = true;
                    for (int k = 0; can && k < N; k++)
                    {
                        if (LS[i][k] == val || LS[k][j] == val)
                            can = false;

                    }

                    if (can)
                    {
                        LS[i][j] = val;
                        if (i + 1 < N)
                            Check(i + 1, j);
                        else
                            Check(0, j + 1);
                        if (found)
                            break;
                        LS[i][j] = -1;
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
