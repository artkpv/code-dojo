#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

3 7 7 8 9 
5 2 7 5 5 

BF

j = from lowest cnt to highest 
    while num of categories with j > 1
        take lowest cost from those categories
        find best place to increase this cat  <- 
        increase to that
        decrease at this
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

namespace CF1310a
{
    public class Solver
    {
        public void Solve()
        {
            int n = ReadInt();
            int[] aIn = ReadIntArray();
            int[] tIn = ReadIntArray();
            var a_t = new (int a, int t)[n];
            for (int j = 0; j < n; j++)
            {
                a_t[j] = (aIn[j], tIn[j]);                
            }
            Array.Sort(a_t);
            var cnt = new List<(int, int)>();
            var heaper = new MinHeaper<(int, int)>();

            cnt.Add((-a_t[0].t, 0));
            int i = 1;
            long cntValue = a_t[0].a;
            long ans = 0;
            while (cnt.Any() || i < n)
            {
                if (i < n && a_t[i].a == cntValue)
                {
                    heaper.Push(cnt, (-a_t[i].t, i));
                    i += 1;
                }
                else if (cnt.Any())
                {
                    (int ti, int inx) = heaper.Pop(cnt);
                    ti = -ti;

                    ans += (cntValue - a_t[inx].a) * ti;
                    cntValue += 1;                    
                }
                else
                {
                    cntValue = a_t[i].a;
                }
            }
            Write(ans);

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

    public class MinHeaper<T> 
        where T : IComparable
    {
        private readonly IComparer<T> comparer;

        public MinHeaper(IComparer<T> comparer=null)
        {
            this.comparer = comparer ?? Comparer<T>.Default;
        }

        public void Heapify(IList<T> arr) 
        {
            for (int i = arr.Count()/2; i >= 0; i--)
                SiftDown(arr, i);                
        }

        public void Push(IList<T> arr, T el)  
        {
            arr.Add(el);
            SiftUp(arr, arr.Count() - 1);
        }

        public T Pop(IList<T> arr) 
        {
            if (!arr.Any())
                throw new ArgumentOutOfRangeException("Empty array");
            T el = arr.First();
            int n = arr.Count();
            arr[0] = arr[n-1];
            arr.RemoveAt(n-1);
            SiftDown(arr, 0);
            return el;
        }

        private void SiftUp(IList<T> arr, int i) 
        {
            while (Parent(i) >= 0 && arr[Parent(i)].CompareTo(arr[i]) > 0) 
            {
                Exch(arr, Parent(i), i);
                i = Parent(i);
            }
        }

        private int Parent(int i) => (i + 1) / 2 - 1;

        private void SiftDown(IList<T> arr, int i) 
        {
            int n = arr.Count();
            while ((i + 1) * 2 - 1 < n)
            {
                int k = (i + 1) * 2 - 1;
                if (k + 1 < n && arr[k+1].CompareTo(arr[k]) < 0)
                    k += 1;
                if (arr[i].CompareTo(arr[k]) <= 0)
                    break;
                Exch(arr, i, k);
                i = k;
            }
        }

        private void Exch(IList<T> arr, int i, int j)
        {
            T t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
        }
    }


    }
}

/*

5
3 7 7 8 9 
5 2 7 5 5 
0 1 2 3 4

cnt 5-0 
i 1
cntValue 3
ans 0 

cnt
i 1
cntvalue 4
ans 0

cnt
i 1
cntvalue 7
ans 0

cnt 2-1
i 2
cntvalue 7
ans 0

cnt 2-1 7-2
i 3
cntvalue 7
ans 0

cnt 7-2
i 3
cntvalue 8
ans 0

cnt 5-3 7-2




*/
