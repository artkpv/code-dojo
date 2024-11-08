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

public class Solver
{
    public void Solve()
    {
        int tests = ReadInt();
        for (int test = 0; test < tests; test++)
        {
            long n = ReadLong();
            int m = ReadInt();
            int[] bags = ReadIntArray();
            const int MAX = 61;
            int[] powers = new int[MAX+1];
            long sum = 0;
            for (int i = 0; i < m; i++)
            {
                sum += bags[i];
                int power = -1;
                while (bags[i] > 0)
                {
                    bags[i] >>= 1;
                    power += 1;
                }
                powers[power] += 1;
            }

            if (sum < n)
                Write(-1);
            else
            {
                int[] nPowers = new int[MAX+1];
                int power = 0;
                while (n > 0)
                {
                    if ((n & 1) == 1)
                        nPowers[power] = 1;
                    power += 1;
                    n >>= 1;
                }

                long count = 0;
                //Debug.WriteLine($"nPowers={string.Join(' ', nPowers)}");
                for (int i = 0; i < MAX; i++)
                {
                    //Debug.WriteLine($"i={i} count={count} powers={string.Join(' ', powers)}");
                    if (powers[i] > nPowers[i])
                    {
                        powers[i] -= nPowers[i];
                        powers[i+1] += powers[i] / 2;
                        powers[i] = powers[i] % 2;
                    }
                    else if (nPowers[i] > 0 && powers[i] == 0)
                    {
                        while (powers[i] == 0)
                        {
                            int j = i + 1;
                            while (j < MAX && powers[j] == 0)
                                j += 1;
                            Trace.Assert(j < MAX);
                            
                            powers[j] -= 1;
                            powers[j-1] += 2;
                            count += 1;
                        }
                    }
                }
                Write(count);
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
