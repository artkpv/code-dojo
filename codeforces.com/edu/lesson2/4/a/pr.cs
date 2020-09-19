#define TRACE
#undef DEBUG
/*

   Sorts suffixes for a string.
https://codeforces.com/edu/course/2/lesson/2/1/practice/contest/269100/problem/A

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

namespace Lesson3Step2
{
    public class Solver
    {
        string text;
        int sLen;
        int[] sInx; // Sorted suffix index.
        int[] isInx; // Inverted suffix index (suffix index to sorted suffix index).
        int[] ec;  // ec[i] - equivalency class for suffix at i-th index.
        int[] auxSInx;
        int[] nextEc;
        int[] lcp;
        int radix = 'z' - 'a' + 2;

        public void Solve()
        {
            text = ReadToken();
            sLen = text.Length + 1;
            sInx = new int[sLen];
            ec = new int[sLen];
            auxSInx = new int[sLen];
            nextEc = new int[sLen];
            for (int i = 0; i < sLen; i++)
            {
                sInx[i] = i;
                ec[i] = i < text.Length ? text[i] - 'a' + 1 : 0;
            }

            //WriteArray(sInx);
            RadixSort();

            int k = 0;
            while ((1 << k) < sLen)
            {
                //WriteArray(sInx);
                for (int i = 0; i < sLen; i++)
                {
                    sInx[i] = (sLen + sInx[i] - (1 << k)) % sLen;
                }
                RadixSort();
                nextEc[sInx[0]] = 0;
                for (int i = 1; i < sLen; i++)
                {
                    int prev = sInx[i-1];
                    int cur = sInx[i];
                    int prevA = ec[prev];
                    int prevB = ec[(prev + (1 << k)) % sLen];
                    int a = ec[cur];
                    int b = ec[(cur + (1 << k)) % sLen];
                    if (prevA == a && prevB == b)
                        nextEc[cur] = nextEc[prev];
                    else
                        nextEc[cur] = nextEc[prev] + 1;
                }
                int[] t = ec;
                ec = nextEc;
                nextEc = t;

                radix = ec[sInx[sLen-1]] + 1;
                k += 1;
            }

            WriteArray(sInx);

            BuildLCP();

            WriteArray(lcp);
        }

        private void RadixSort()
        {
            int[] index = new int[radix + 1];
            for (int i = 0; i < sLen; i++)
            {
                index[ec[sInx[i]] + 1] += 1;              
            }

            for (int i = 2; i < radix + 1; i++)
            {
                index[i] += index[i - 1];                
            }

            for (int i = 0; i < sLen; i++)
            {
                auxSInx[i] = sInx[i];                
            }

            for (int i = 0; i < sLen; i++)
            {
                int pos = index[ec[auxSInx[i]]];
                index[ec[auxSInx[i]]] += 1;
                sInx[pos] = auxSInx[i];
            }
        }

        private void BuildLCP()
        {
            lcp = new int[sLen - 1];
            isInx = new int[sLen];
            for (int i = 0; i < sLen; i++)
                isInx[sInx[i]] = i;

            int k = 0;
            for (int i = 0; i < sLen-1; i++)
            {
                if (isInx[i] == 0)
                    continue;
                int j = sInx[isInx[i] - 1];
                k = GetSameNum(i, j, k);
                lcp[isInx[i] - 1] = k;
                k = Max(0, k - 1);
            }
        }

        private int GetSameNum(int i, int j, int p)
        {
            while (i + p < text.Length && j + p < text.Length && text[i + p] == text[j + p])
            {
                p += 1;
            }
            return p;
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
