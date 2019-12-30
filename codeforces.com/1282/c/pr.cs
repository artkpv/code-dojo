#define TRACE
#undef DEBUG
/*
 * Author: Artyom K. < w1ld [dog] inbox [dot] ru
6 20 2 5
1 1 0 1 0 0
0 8 2 9 11 6


1 0 0 1 1 0
0 2 6 8 9 11   
   
6 17  2 6
1 0 0 0 0 1
3 6 7 7 10 12

2



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
            int prNum = ReadInt();
            int timeLimit = ReadInt();
            int easyT = ReadInt();
            int hardT = ReadInt();
            bool[] types = ReadIntArray().Select(el => el == 1).ToArray();
            int[] starts = ReadIntArray();
            long countA = 0;
            long countB = 0;
            for (int i = 0; i < prNum; i++)
            {
                if (types[i])
                    countB += 1;
                else
                    countA += 1;
            }
            
            Array.Sort(starts, types);

            long max = 0; 
            long spent = 0;
            long count = 0;
            for (int i = starts[0] == 0 ? 1 : 0; i <= prNum; i++)
            {
                if (i > 0)
                {
                    if (types[i-1])
                    {
                        spent += hardT;
                        countB -= 1;
                    }
                    else
                    {
                        spent += easyT;
                        countA -= 1;
                    }
                    count += 1;
                }
                long has = i == prNum ? timeLimit : starts[i] - 1;
                has -= spent;

                if (has >= 0)
                {
                    long total = Min(countA, has / easyT);
                    total += Min(countB, (has - total * easyT) / hardT);
                    total += count;
                    max = Max(max, total);
                }
            }

            Write(max);
        }
        
    }
    /*
*/

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
