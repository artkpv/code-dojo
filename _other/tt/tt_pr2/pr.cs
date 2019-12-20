/*
 * Given a n by m matrix with a_{i,j} = 0..9, find 
 * max number got by moving by adj cells.
 *
 * Example
 *
 * 2 4
 * 1 0 0 0 
 * 0 5 9 0
 * Ans: 9501
 *
 *
 * I 1 Bf.
 * For each cell  n*m
 *  for each direction  // 4
 *    for each 2nd cell  // 4
 *      for each 3rd cell // 4
 *
 * Time: O(n*m * 64)
 *        
 */
#define TRACE
#define DEBUG

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
    private List<(int x, int y)> _path = new List<(int x, int y)>();
    private int maxPath = 0;
    private int n;
    private int m;
    private int[][] board;
    private const int LENGTH = 4;

    private void Paths() 
    {
        if (_path.Count() == LENGTH)
        {
            int path = 0;
            int k = 0;
            foreach ((int c, int r) in _path)
                path += board[r][c] * (int)Math.Pow(10, (k++)); 

            maxPath = Math.Max(maxPath, path);
            return;
        }

        (int x, int y) = _path[_path.Count() - 1];
        (int lx, int ly) = _path.Count() > 1 ? _path[_path.Count() - 2] : (x, y);

        foreach ((int h, int v) in new[] { 
            (-1, 0), (0, 1), (1, 0), (-1, 0) }) 
        {
            int xx = x + h;
            int yy = y + v;
            if (lx == xx && ly == yy)
                continue;
            if (! ( 0 <= xx && xx < m ))
                continue;
            if (! (0 <= yy && yy < n))
                continue;
            _path.Add((xx, yy));
            Paths();
            _path.RemoveAt(_path.Count()-1);
        }
    }

    public void Solve() {
        n = ReadInt();
        m = ReadInt();
        board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = ReadIntArray();

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < m; c++)
            {
                _path.Add((c, r));
                Paths();
                _path.Clear();
            }
        }
        Write(maxPath);
    }

    private void PrintBoard(int[][] b) {
        var sb = new StringBuilder();
        for (int i = 0; i < b.Length; i++)
        {
            sb.Append(string.Join(" ", b[i]) + "\n");
        }
        Console.Write(sb.ToString());
    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    static void Main()
    {
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
