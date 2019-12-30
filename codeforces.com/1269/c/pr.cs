#define TRACE
#undef DEBUG
/*



wrong answer 2nd lines differ - expected: '763451441322205312208507561197...3303779887610009510217518595697', found: '763451441322205312208507561197...3037798876100095102175185956107'
3303779887610009510217518595697
 3037798876100095102175185956107

   1234 2
   1313

   7654321 2
   7676767 x
   77

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
        int numL = ReadInt();
        int k = ReadInt();
        byte[] num = ReadToken().Select(c => (byte)(c - '0')).ToArray();
        Trace.Assert(num.Length == numL);
        byte[] original = new byte[numL];
        Array.Copy(num, original, numL);

        int i;
        for (i = k-1; i >= 0; i--)
            for (int j = i; j + k < numL; j += k)
                num[j + k] = num[j];

        i = 0;
        while (i < numL && original[i] == num[i])
            i += 1;
        if (i == numL || original[i] < num[i])
        {
            Write(numL);
            Write(string.Concat(num));
        }
        else
        {
            int p = k-1;
            while (p >= 0 && num[p] == 9)
                p -= 1;
            Trace.Assert(p >= 0);
            num[p] += 1;
            bool first = true;
            while (p < k)
            {
                if (first)
                    first = false;
                else
                    num[p] = 0;
                for (int j = p; j + k < numL; j += k)
                    num[j + k] = num[j];
                p += 1;
            }
            Write(numL);
            Write(string.Concat(num));
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
