#define TRACE
#undef DEBUG
/*
Author: w1ld [dog] inbox [dot] ru

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
        // f3 = f2 - f1
        // f4 = f3 - f2
        // f5 = f4 - f3
        // ...
        // fn = f{n-1} - f{n-2}
        // fn = f{n-2} - f{n-3} - (f{n-3} - f{n-4}) 
        // fn = f{n-2} - 2*f{n-3} + f{n-4}
        // fn = f{n-3} - fn-4 - 2*(f{n-4} - fn-5) + f{n-5} - f(n-6)
        // fn = f{n-3} - fn-4 - 2*(f{n-4} - fn-5) + f{n-5} - f(n-6)
        //
        // f1 
        // f2 
        // f3 = f2 - f1
        // f4 = -f1
        // f5 = -f2
        // f6 = -f2 + f1
        // f7 = f1
        // f8 = f2
        // f9 = f2 - f1
        // ... 
        // 
        // n%6
        // 1 = f1
        // 2 = f2
        // ... 
        //
        //

        const long MOD = (int)(1e9 + 7);

        long x = ReadInt();
        long y = ReadInt();
        int n = ReadInt();
        Action<long> MWrite = (a) => Write((a%MOD) < 0 ? (a%MOD)+MOD : a%MOD);
        switch (n % 6)
        {
            case 1:
                MWrite(x);
                break;
            case 2:
                MWrite(y);
                break;
            case 3:
                MWrite(y - x);
                break;
            case 4:
                MWrite(-x);
                break;
            case 5:
                MWrite(-y);
                break;
            case 0:
                MWrite(-y + x);
                break;
            default:
                throw new Exception();
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
