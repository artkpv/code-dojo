#define DEBUG
/*
n salaries with r_i, l_i
Find max median salary

 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;

public class Solver
{
    public int BinarySearchLeft<T>(IList<T> array, T element) 
        where T : IComparable
    {
        int lo = 0;
        int hi = array.Count() - 1;
        while (lo < hi)
        {
            int mid = (lo+hi) / 2;
            if (array[mid].CompareTo(element) < 0)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }

    public void Solve()
    {
        int tests = ReadInt();
        for (int test = 0; test < tests; test++)
        {
            int n = ReadInt();
            long money = ReadLong();
            long[] l = new long[n];
            long[] r = new long[n];
            long[] rToL = new long[n];
            for (int worker = 0; worker < n; worker++)
            {
                l[worker] = ReadInt();
                r[worker] = ReadInt();
                rToL[worker] = l[worker];
            }
            Array.Sort(l);
            Array.Sort(r, rToL);
            long[] lPay = new long[n];

            lPay[0] = l[0];
            for (int i = 1; i < n; i++)
                lPay[i] = lPay[i - 1] + l[i];

            long[] rPay = new long[n];
            rPay[n - 1] = rToL[n - 1];
            for (int i = n - 2; 0 <= i; i--)
                rPay[i] = rPay[i + 1] + rToL[i];

            Debug.WriteLine(string.Join(" ", l));
            Debug.WriteLine(string.Join(" ", r));
            Debug.WriteLine(string.Join(" ", lPay));
            Debug.WriteLine(string.Join(" ", rPay));
            int half = (n+1) / 2;  // Always odd.

            Func<long, long> F = (long mid) => {
                // Get minimal money amount so that median salary is equal or higher than mid and number of those.
                // 1. r_i < mid
                int leftNum = BinarySearchLeft(r, mid);
                // 2. mid <= l_i included.
                int rightNum = n - BinarySearchLeft(l, mid);
                // 3. l_i <= mid < r_i: make l_i or mid for them. 
                int middleNum = n - leftNum - rightNum;

                if (half <= leftNum)
                    return -1; // Not possible.
                if (half <= rightNum)
                    return money;

                long rightPay = rightNum > 0 ? rPay[n - rightNum] : 0;
                long middleMidPay = half - rightNum;
                long minMoney = lPay[half - 2] + (middleMidPay * mid) + rightPay;
                return minMoney;
            };

            long lo = l[0];
            long hi = r[n-1];
            while (lo < hi) 
            {
                long median = (lo + hi) / 2;
                long minMoney = F(median);
                Debug.Write($" {lo} {hi} {median} {minMoney}\n");
                if (minMoney == -1)
                    hi = median;
                else
                    lo = median + 1;
            }

            Write(lo - 1);
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
    private static string[] ReadAndSplitLine() { return reader.ReadLine().Split(new[] { ' ', '\t', }, StringSplitOptions.RemoveEmptyEntries); }
    public static string ReadToken() { while (currentLineTokens.Count == 0) currentLineTokens = new Queue<string>(ReadAndSplitLine()); return currentLineTokens.Dequeue(); }
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
