/*

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
    private void Swap(List<(int, int)> swaps, char[] s, char[] t, int i, int j) 
    {
        char temp = s[i];
        s[i] = t[j];
        t[j] = temp;
        swaps.Add((i, j));
    }

    private IEnumerable<(int k, int p)> GetSwap(char[] s, char[] t, int i) 
    {
        int n = s.Length;
        int j = i+1;
        // For t[i].
        for (j = i+1; j < n; j++) 
        {
            if (t[i] == t[j]) // Found.
            {
                yield return (i, j);
                yield break;
            }
        }
        // For s[i].
        for (j = i+1; j < n; j++) 
        {
            if (s[i] == s[j]) // Found.
            {
                yield return (j, i);
                yield break;
            }
        }
        yield return (i, i);
        foreach(var swap in GetSwap(s, t, i))
            yield return swap;

        // Pair swap for i-th place.
        //int k = i + 1;
        //while (k < n && s[k] == t[i])
            //k++;
        //if (k == n)
            //throw new Exception("invalid");
        //int p = i + 1;
        //while (p < n && t[p] != s[k])
            //p++;
        //yield return (i, p);
        //yield return (k, i);
    }


    public void Solve()
    {
        
        int tests = ReadInt();
        int R = 'z' - 'a' + 1;
        for(int test = 0; test < tests; test++) 
        {
            int[] count = new int[R];
            int n = ReadInt();
            char[] s = ReadToken().ToCharArray();
            char[] t = ReadToken().ToCharArray();
            for (int i = 0; i < n; i++)
            {
                count[s[i] - 'a']++;                
                count[t[i] - 'a']++;                
            }
            bool isPossible = true;
            for (int i = 0; i < R && isPossible; i++)
            {
                isPossible = count[i] % 2 == 0;
            }
            var swaps = new List<(int, int)>();
            if (isPossible) 
            {
                for (int i = 0; i < n; i++)
                {
                    if (s[i] != t[i]) 
                    {
                        foreach (var swap in GetSwap(s, t, i)) 
                        {
                            Swap(swaps, s, t, swap.Item1, swap.Item2);
                        }
                    }
                }
            }
            if (isPossible) {
                Console.WriteLine("Yes");
                Console.WriteLine(swaps.Count());
                foreach(var tuple in swaps) {
                    Console.WriteLine((tuple.Item1 + 1) + " " + (tuple.Item2 + 1));
                }
            }
            else {
                Console.WriteLine("No");
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
