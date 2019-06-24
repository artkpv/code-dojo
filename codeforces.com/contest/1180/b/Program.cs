using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
/*

3 -1 -4 1 

I1 
2^n

I2
Greedy

a1 a2 a3 a4 a5

all 0 -> -1
minuses

m
z
mo
m` = m+z

p = n-m+z+mo

3 -1 -4 1

-4 -1 -4 -2 = 32

-1 1


 */

public class Solver
{
    public int[] Maximize(int[] a, int i, int j)
    {
        int x = a[i-1], y = a[i];
        int max_ = int.MinValue;
        int[] b = new int[2];
        foreach (var v in new [] { 0, 1, 2, 3 })
        {
            int xx = v & 1 == 1 ? -x-1 : x;
            int yy = v & 2 == 1 ? -y-1 : y;
            if (xx*yy > max_)
            {
                b[0] = xx;
                b[1] = yy;
            }
        }
        return b;
    }

    public void Solve()
    {
		int n = ReadInt();
		int[] a = ReadIntArray();
        if (n == 1)
        {
            Write(Math.Max(a[0], -a[0]-1));
            return;
        }
        int i = 1;
        int end = n;
        if (n > 2 && n % 2 == 1)
        {
            int[] b = Maximize(a[0], a[1]);
            int[] bb = Maximize(a[n-2], a[n-1]);
            if (b[0]*b[1] > bb[0]*b[1])
            {
                a[0] = b[0];
                a[1] = b[1];
                i = 3;
            }
            else 
            {
                a[0] = 
            }
        }
        for (; i < end i += 2)
        {
            int[] b = Maximize(a, i-1, i);
            a[i-1] = b[0];
            a[i] = b[1];
        }
    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    static void Main()
    {
#if DEBUG
        // reader = new StreamReader("..\\..\\input.txt");
        reader = new StreamReader(Console.OpenStandardInput());
        writer = Console.Out;
        //writer = new StreamWriter("..\\..\\output.txt");
#else
        reader = new StreamReader(Console.OpenStandardInput());
        writer = new StreamWriter(Console.OpenStandardOutput());
        //reader = new StreamReader("input.txt");
        //writer = new StreamWriter("output.txt");
#endif
        try
        {
            new Solver().Solve();
            //var thread = new Thread(new Solver().Solve, 1024 * 1024 * 128);
            //thread.Start();
            //thread.Join();
        }
        catch (Exception ex)
        {
#if DEBUG
            Console.WriteLine(ex);
#else
            throw;
#endif
        }
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
