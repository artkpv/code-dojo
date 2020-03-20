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

namespace CFlesson5a
{
    public class SuffixArray
    {
        private string text;
        private int sLen;
        private int[] sInx; // Sorted suffix index.
        private int[] ec;  // ec[i] - equivalency class for suffix at i-th index.
        private int[] auxSInx;
        private int[] nextEc;
        private int radix;

        public SuffixArray(string text) 
            : this(text, (char c) => c - 'a', 'z' - 'a' + 1)
        { }

        public SuffixArray(string text, Func<char, int> charMap, int radix)
        {
            this.text = text; 
            this.radix = radix + 1; // Extra for end string.
            sLen = text.Length + 1;
            sInx = new int[sLen];
            ec = new int[sLen];
            auxSInx = new int[sLen];
            nextEc = new int[sLen];
            for (int i = 0; i < sLen; i++)
            {
                sInx[i] = i;
                if (i < text.Length)
                {
                    int map = charMap(text[i]);
                    Trace.Assert(0 <= map && map < radix);
                    ec[i] = map + 1; // Extra for end string.
                }
                else
                {
                    ec[i] = 0;  // End string.
                }
            }

            RadixSort();

            int k = 0;
            while ((1 << k) < sLen)
            {
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

        public int[] Array 
        {
            get => sInx;
        }

    }

    public class LCP
    {
        private int sAL; // Suffix array length.
        private int[] sA; // Sorted suffix array.
        private string text;
        private int[] lcp; // lcp[i] - longest common prefix length of suffixes at i-th and i+1 positions in the sorted suffix array.
        private int[] sP; // sP[i] - position of i-th suffix in the sorted suffix array.

        public LCP(string text) : this(text, new SuffixArray(text))
        { } 

        public LCP(string text, SuffixArray suffixArray)
        {
            this.text = text;
            this.sA = suffixArray.Array;
            this.sAL = suffixArray.Array.Length;

            lcp = new int[sAL - 1];
            sP = new int[sAL];
            for (int i = 0; i < sAL; i++)
                sP[sA[i]] = i;

            int skip = 0;
            for (int i = 0; i < text.Length; i++)
            {
                if (sP[i] == 0)
                    continue;
                int j = sA[sP[i] - 1];
                skip = GetLCP(i, j, skip);
                lcp[sP[i] - 1] = skip;
                skip = Max(0, skip - 1);
            }
        }

        private int GetLCP(int i, int j, int k)
        {
            while (i + k < text.Length && j + k < text.Length && text[i + k] == text[j + k])
            {
                k += 1;
            }
            return k;
        }

        public int[] Array
        {
            get => lcp;
        }

        public int[] SuffixPosition
        {
            get => sP;
        }
    }

    public class Solver
    {

        public void Solve()
        {
            string sA = ReadToken().Trim();
            string sB = ReadToken().Trim();
            if (string.IsNullOrWhiteSpace(sA) || string.IsNullOrWhiteSpace(sB))
            {
                Write("");
                return;
            }
            string sC = sA + "#" + sB;
            int n = sC.Length;
            Trace.Assert(n > 2);
            var sArr = new SuffixArray(
                sC,
                (c) => c == '#' ? 0 : c - 'a' + 1,
                'z' - 'a' + 2);
            var lcp = new LCP(sC, sArr);
            var lcpa = lcp.Array;
            int max = 0;
            int maxInx = -1;
            Func<int, int> getClass = (int i) => i < sA.Length ? 1 : 2;
            for (int i = 0; i < lcpa.Length; i++)
            {
                int iA = sArr.Array[i];
                int iB = sArr.Array[i + 1];
                if (lcpa[i] > max && getClass(iA) != getClass(iB))
                {
                    maxInx = iA;
                    max = lcpa[i];
                }
            }

            if (maxInx == -1)
                Write("");
            else 
                Write(sC.Substring(maxInx, max));
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
