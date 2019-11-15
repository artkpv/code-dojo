#undef DEBUG
/*
 RUN!
t <= 10^5
for all t, sum n+m <= 10^5

I1
BF
For each monsters set iter over heroes.
O(n^3)

I2
Precomp p s: max power for i. 
(p, i)

E1
2 3 11 14 1 8
3 2
100 1


 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using M = System.Math;

public class Solver
{
    public void Solve()
    {
        int tests = ReadInt();
        const int MAXN = 200000;
        int[] mA = new int[MAXN];
        int[] powers = new int[MAXN];
        int[] stamina = new int[MAXN];
        for (int test = 0; test < tests; test++)
        {
            int mNum = ReadInt();
            for (int i = 0; i < mNum; i++)
                mA[i] = ReadInt();
            int hNum = ReadInt();
            for (int i = 0; i < hNum; i++)
            {
                powers[i] = ReadInt();
                stamina[i] = ReadInt();
            }
            Array.Sort(stamina, powers, 0, hNum);
            for (int i = hNum-2; i >= 0; i--)
            {
                if (powers[i+1] > powers[i])
                    powers[i] = powers[i+1];
            }
            Debug.WriteLine(string.Join(" ", powers.Take(hNum)));
            Debug.WriteLine(string.Join(" ", stamina.Take(hNum)));
            int deadM = 0;
            int days = 0;
            Debug.WriteLine($"deadM={deadM} days={days}");
            while (deadM < mNum) 
            {
                // Two pointers: h for heroes, i for monsters.
                int i = 0;
                int h = 0;
                int minPower = mA[deadM];
                while (true) 
                {
                    if (deadM + i >= mNum) // No more monsters.
                        break;
                    if (h >= hNum)  // No more heroes.
                        break;
                    minPower = Math.Max(minPower, mA[deadM + i]);
                    if (minPower > powers[h])  // Too powerful.
                        break;

                    if (i + 1 > stamina[h])  // Not enough stamina.
                        h++;
                    else  // Can kill more.
                        i++;
                }
                Debug.WriteLine($" days={days} i={i} h={h}");
                // Now h <= hNum, 0 <= i <= mNum.
                if (i == 0) // Too powerful.
                {
                    days = -1;
                    break;
                }
                days++;
                deadM += i;
            }
            Write(days);
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
}
    #endregion
