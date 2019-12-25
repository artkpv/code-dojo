#define TRACE
#undef DEBUG
/*
6 20 2 5
1 1 0 1 0 0
0 8 2 9 11 6

5 13 4 14 13 8

3 1 6 2 5 4


s 2 7 9 
p 1 2 3
b 1
   

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
            int time = ReadInt();
            int easyT = ReadInt();
            int hardT = ReadInt();
            bool[] types = ReadIntArray().Select(el => el == 1).ToArray();
            int[] starts = ReadIntArray();
            int[] startsInx = new int[prNum];
            int[] ends = new int[prNum];
            int[] endsInx = new int[prNum];
            for (int i = 0; i < prNum; i++)
            {
                ends[i] = starts[i] + (types[i] ? hardT : easyT);
                endsInx[i] = i;
                startsInx[i] = i;
            }
            
            Array.Sort(starts, startsInx);
            Array.Sort(ends, endsInx);

            int stInx = 0;
            int endInx = 0;
            var solved = new HashSet<int>();
            int max = 0;
            int now = 0;
            while (now <= time && endInx < prNum)
            {
                int prI = endsInx[endInx++];
                now += types[prI] ? hardT : easyT;
                solved.Add(prI);
                while (stInx < prNum && solved.Contains(startsInx[stInx]))
                    stInx++;
                if (now <= time && (stInx >= prNum || now < starts[stInx]))
                    max = Max(max, solved.Count());
            }
            Write(max);
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
