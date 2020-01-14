
#define TRACE
#define DEBUG
/*
Author: w1ld [dog] inbox [dot] ru

2 1
1 

1 2 1
1 2 2
1 1 1
1 1 2
2 1 1
2 1 2

5 correct, 1 non-correct

5 / 6 


for each gift
 correct += with this gift * with this gift

Time: n

all = num of pr * ppl

pr = correct / all


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

public class Solver
{
    const long MOD = 998244353;

    private Dictionary<(long, long), long> _cache = new Dictionary<(long, long), long>();

    // бинарное возведение в степень
    long BP (long a, long n) {
        //if (_cache.ContainsKey((a, n)))
            //return _cache[(a, n)];
        long res = 1;
        while (n > 0) {
            if ((n & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            n >>= 1;
        }
        //_cache[(a, n)] = res;
        return res;
    }

    public void Solve()
    {
        int n = ReadInt();
        const int MAX = 1_000_000;
        int[] counter = new int[MAX+1];
        int[][] gifts = new int[n][];

        for (int i = 0; i < n; i++)
        {
            int[] a = ReadIntArray();
            gifts[i] = new int[a[0]];
            for (int j = 0; j < a[0]; j++)
            {
                gifts[i][j] = a[j+1];
                counter[a[j+1]] += 1;                
            }
        }

        long ans = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < gifts[i].Length; j++)
            {
                // Chosen probability.
                long cp = BP(n, MOD-2) * BP(gifts[i].Length, MOD-2) % MOD; 
                // Right p.
                long rp = (long)counter[gifts[i][j]] * BP(n, MOD-2) % MOD;
                ans = (ans + cp * rp % MOD) % MOD;
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
}
