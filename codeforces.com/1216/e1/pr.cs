/*
s = 1e9

n*(n+1)/2 = 1e9
n^2 + n - 2e9 = 0

n^2 + n + 1/4 = 2e9 + 1/4
(n + 1/2) (n + 1/2) = (2e9 + 1/4)

n + 1/2 = +- (2e9 + 1/4)^.5
n ~= 45 000 


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
    public void Solve()
    {
        const int TMAX = 1000000000;
        const int AMAX = 100000;
        byte[] a = Init<byte>(AMAX);
        int[] alen = Init<int>(AMAX);
        int alenn = 0;
        int x = 1;
        int ai = 0;
        int counter = TMAX;
        int digitlen = 1;
        int digitleninc = 10;
        while (counter > 0 && ai + 100 < AMAX) 
        {
            int y = x;
            int xlen = digitlen;
            while (y > 0)
            {
                a[ai+xlen-1] = (byte) (y % 10);
                y /= 10;
                xlen--;
            }
            ai += digitlen;
            alen[alenn++] = ai;
            counter -= ai;
            x++;
            if (x == digitleninc) 
            {
                digitlen++;
                digitleninc *= 10;
            }
        }
        //for (int i = 0; i < 100; i++)
        //{
            //Console.Write(alen[i] + " ");
        //}
        //Console.Write("\n");
        //for (int i = 0; i < 100; i++)
        //{
            //Console.Write(a[i] + " ");
        //}
        //Console.Write("\n");
        //Console.WriteLine(alenn);
        //Console.WriteLine(x);

        int queries = ReadInt();
        for (int qi = 0; qi < queries; qi++)
        {
            int k = ReadInt();
            int aleni = 0; 
            while (aleni < alenn)
            {
                if (k - 1 < alen[aleni])
                {
                    Write(a[k-1]);
                    break;
                }
                k -= alen[aleni++];
            }
        }

    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    static void Main()
    {
        //Debug.Listeners.Clear();
        //Debug.Listeners.Add(new ConsoleTraceListener());
        //Trace.Listeners.Clear();
        //Trace.Listeners.Add(new ConsoleTraceListener());

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
