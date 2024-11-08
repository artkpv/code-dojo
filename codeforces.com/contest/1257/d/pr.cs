#undef DEBUG
/*
 RUN2!
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

best:
0 100
1 3    
2 -1   maxS

0 0   deadM days
 0 2  i mPower
 1 3 
 2 11 break
2 1
 0 11


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
        const int MAXN = 200009;
        int[] mA = new int[MAXN];
        int[] powers = new int[MAXN];
        int[] stamina = new int[MAXN];
        for (int test = 0; test < tests; test++)
        {
            int mNum = ReadInt();
            for (int i = 0; i < mNum; i++)
                mA[i] = ReadInt();
            int hNum = ReadInt();
            int[] best = new int[mNum+1];
            for (int i = 0; i < hNum; i++)
            {
                powers[i] = ReadInt();
                stamina[i] = ReadInt();
                best[stamina[i]] = Math.Max(best[stamina[i]], powers[i]);
            }
            for (int i = mNum-1; i > 0; i--)
                best[i] = Math.Max(best[i], best[i+1]);

            Debug.WriteLine(string.Join(" ", powers.Take(hNum)));
            Debug.WriteLine(string.Join(" ", stamina.Take(hNum)));
            int deadM = 0;
            int days = 0;
            Debug.WriteLine($"deadM={deadM} days={days}");
            while (deadM < mNum) 
            {
                int i = 0;
                int mPower = mA[deadM];
                // There are more monsters. There is a powerful hero.
                while (deadM + i < mNum)
                {
                    mPower = Math.Max(mPower, mA[deadM + i]);
                    if (mPower > best[i+1])
                        break;
                    else
                        i++;
                }
                Debug.WriteLine($" days={days} i={i}");
                if (i == 0)
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
