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
            long[] bottom = new long[n];
            long[] top = new long[n];
            long[] tToB = new long[n]; // Top to bottom.
            for (int worker = 0; worker < n; worker++)
            {
                bottom[worker] = ReadInt();
                top[worker] = ReadInt();
                tToB[worker] = bottom[worker];
            }
            Array.Sort(bottom);
            Array.Sort(top, tToB);
            long[] leftOrderPay = new long[n];

            leftOrderPay[0] = bottom[0];
            for (int i = 1; i < n; i++)
                leftOrderPay[i] = leftOrderPay[i - 1] + bottom[i];

            long[] rightOrderPay = new long[n];
            rightOrderPay[n - 1] = tToB[n - 1];
            for (int i = n - 2; 0 <= i; i--)
                rightOrderPay[i] = rightOrderPay[i + 1] + tToB[i];

            Debug.WriteLine("bottom="+ string.Join(" ", bottom));
            Debug.WriteLine("top="+string.Join(" ", top));
            Debug.WriteLine("leftOrderPay="+string.Join(" ", leftOrderPay));
            Debug.WriteLine("rightOrderPay="+string.Join(" ", rightOrderPay));
            int half = (n+1) / 2;  // Always odd.

            Func<long, bool> IsPossible = (long median) => {
                int left = BinarySearchLeft(top, median);
                int right = n - BinarySearchLeft(bottom, median);
                int middle = n - left - right;

                //Debug.WriteLine(
                        //$" IsPossible median={median} {half} left={left} top={right} m={middle}");
                if (half <= left)
                    return false;
                if (half <= right)
                    return true;

                long rightPay = right > 0 ? rightOrderPay[n - right] : 0;
                int middleRight = half - right;
                Debug.Assert(middleRight > 0);
                int middleLeft = middle - middleRight;
                long minMoney = 
                    (middleLeft > 0 ? leftOrderPay[left + middleLeft - 1] : 0) 
                    + (middleRight * median) 
                    + rightPay;
                Debug.WriteLine($" mm={minMoney} mp={middleRight} rp={rightPay} l={left} m={middle} r={right}");
                return minMoney <= money;
            };

            long lo = bottom[0];
            long hi = top[n-1];
            long x = -1;
            while (lo <= hi) 
            {
                x = (lo + hi) / 2;
                bool isPos = IsPossible(x);
                Debug.WriteLine($" x={x} lo={lo} hi={hi} isp={isPos}");
                if (isPos)
                    lo = x + 1;
                else
                    hi = x - 1;
            }

            Write(hi);
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
