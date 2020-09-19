#undef DEBUG
/*
n salaries with r_i, l_i
Find max median salary

3
3 26
10 12
1 4
10 11
1 1337
1 1000000000
5 26
4 4
2 4
6 8
5 6
2 7


26
10 12
1 4
10 11

1 10 10
 1 11 21

4 11 12  1 10 10
 1 11 21

Is possible with m median?

Possible iif, cnt >= n+1/2

 r_i < m          always less than median
 l_i <= m <= r_i  median cross
 m < l_i          always greater than median

num in 2nd >= max(0, (n+1)/2 - num in 3rd)


 

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
        int hi = array.Count();
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
            long[] wl = new long[n]; // Worker bottom possible salary, left.
            long[] wr = new long[n]; // Worker top possible salary, right.
            for (int worker = 0; worker < n; worker++)
            {
                wl[worker] = ReadInt();
                wr[worker] = ReadInt();
            }
            Array.Sort(wl, wr);

            int half = (n+1) / 2;
            Func<long, bool> IsPossible = (long m) => {
                var middleW = new List<int>();
                long spent = 0;
                int count = 0;
                for (int i = 0; i < n; i++)
                {
                    if (wr[i] < m)
                    {
                        spent += wl[i];
                    }
                    else if (wl[i] >= m)
                    {
                        count++;
                        spent += wl[i];
                    }
                    else // Middle.
                    {
                        middleW.Add(i);
                    }
                }

                if (count + middleW.Count() < half)
                    return false;

                int rem = Math.Max(0, half - count);

                spent += rem * m;
                for (int i = 0; i < middleW.Count() - rem; i++)
                    spent += wl[middleW[i]];
                return spent <= money;
            };

            const int MAX = (int) 1e9+1;
            long lo = 0;
            long hi = MAX;
            while (lo < hi) 
            {
                long mid = (lo + hi) / 2;
                bool isPos = IsPossible(mid);
                Debug.WriteLine($" mid={mid} isPos={isPos} lo={lo} hi={hi}");
                if (isPos)
                    lo = mid+1;
                else
                    hi = mid;
            }

            Write(lo-1);
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
