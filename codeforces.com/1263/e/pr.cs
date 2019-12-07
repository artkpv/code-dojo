#undef DEBUG
/*
 *

I1 BF.
Iterate all chars. Count depth and validity. Each time.
n^2


I2 ?
DP?
Store number of open / close brackets and update?
O(n^2) .. bad

I3
Stacks for left and right:
- remaining open / close
- max depth or -1 if wrong
O(N)


TODO:
- Problem. How to detect that left is invalid? Eq ))(()) 


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

public static class StackExtensions
{
    public static bool TryPeek<T>(this Stack<T> stack, out T res) 
    {
        if (stack.Any())
        {
            res = stack.Peek();
            return true;
        }
        res = default (T);
        return false;
    }
}

public class Solver
{
    public void Solve()
    {
        int n = ReadInt();
        var lB = new Stack<(bool t, int i)>(); // Left brackets type (1 - '(', 0 - ')') and index.
        var rB = new Stack<(bool t, int i)>(); // Right brackets.
        var lO = new Stack<int>(); // Left remaining open brackets num.
        var lD = new Stack<int>(); // Left max depth for ')' or -1 if invalid for any ')'.
        var rC = new Stack<int>(); // Right rem. cl. br. num.
        var rD = new Stack<int>(); // Right max depth for '(' or -1.
        string input = ReadToken();
        int cI = 0; // Cursor index.
        const int INF = int.MaxValue;
        var ans = new List<int>();

        Action<(bool t, int i)> PushLeft = (br) =>
        {
            lB.Push(br);
            if (br.t) // '('
            {
                lD.Push(lD.TryPeek(out var lDNum) ? lDNum : 0);
                lO.Push(lO.TryPeek(out var lONum) ? lONum + 1 : 1);
            }
            else // ')'
            {
                if(!lO.TryPeek(out var lONum))
                    lONum = 0;
                if(!rC.TryPeek(out var rCNum))
                    rCNum = 0;
                rCNum++;
                lD.Push(Max(Max(
                    lD.TryPeek(out var lDNum) ? lDNum : 0,
                    lONum),
                    lONum - 1 < 0 ? INF : 0  // To signal left stack is invalid.
                ));
                lO.Push(Max(0, lONum - 1));  // Only opened without pair.
            }
        };

        Action<(bool t, int i)> PushRight = (br) =>
        {
            rB.Push(br);
            if (br.t) // '('
            {
                if(!lO.TryPeek(out var lONum))
                    lONum = 0;
                lONum++;
                if(!rC.TryPeek(out var rCNum))
                    rCNum = 0;
                rD.Push(Max(Max(
                    rD.TryPeek(out var rDNum) ? rDNum : 0,
                    rCNum),
                    rCNum - 1 < 0 ? INF : 0  // To signal right stack is invalid.
                ));
                rC.Push(Max(0, rCNum - 1)); // Only closed w/o pair.
            }
            else // ')'
            {
                rD.Push(rD.TryPeek(out var rDNum) ? rDNum : 0);
                rC.Push(rC.TryPeek(out var rCNum) ? rCNum + 1 : 1);
            }
        };

        for (int inputInx = 0; inputInx < n; inputInx++)
        {
            char c = input[inputInx];
            // Change state:
            switch (c)
            {
                case 'R':
                    if ( rB.Any() && rB.Peek().i == cI)
                    {
                        rD.Pop();
                        rC.Pop();
                        (bool t, int i) b = rB.Pop();
                        PushLeft(b);
                    }
                    cI++;
                    break;
                case 'L':
                    if (0 < cI)
                    {
                        cI--;
                        if (lB.Any() && lB.Peek().i == cI)
                        {
                            lD.Pop();
                            lO.Pop();
                            (bool t, int i) b = lB.Pop();
                            PushRight(b);
                        }
                    }
                    break;
                default:
                    {
                        Trace.Assert(c == '(' || c == ')' || ('a' <= c && c <= 'z'));
                        if (rB.TryPeek(out var rBb) && rBb.i == cI)
                        {
                            // Rewrite right stack.
                            rB.Pop();
                            rC.Pop();
                            rD.Pop();
                        }
                        if (c == '(' || c == ')')
                            PushRight((c == '(', cI));
                        break;
                    }
            }
            // Get max:
            {
                int max = lD.TryPeek(out var lDNum) ? lDNum : 0;
                max = Max(max, rD.TryPeek(out var rDNum) ? rDNum : 0);
                if (!lO.TryPeek(out int lONum))
                    lONum = 0;
                if (!rC.TryPeek(out int rCNum))
                    rCNum = 0;

                max = Max(max, lONum == rCNum ? lONum : INF);

                Debug.WriteLine($@" '{c}' {inputInx} cI={cI} max={max} lONum={lONum} rCNum={rCNum}
  L:{ToString(lB, reverse:true)}, de={string.Join(" ", lD)}, op={string.Join(" ", lO)}
  R:{ToString(rB)}, de={string.Join(" ", rD)}, cl={string.Join(" ", rC)}");
                ans.Add(max == INF ? -1 : max);
            }
        }
        Write(string.Join(" ", ans));
    }

    private string ToString(Stack<(bool t, int i)> s, bool reverse=false)
    {
        var sb = new StringBuilder();

        foreach((bool t, int i) b in reverse ? s.Reverse() : s)
        {
            char c = b.t ? '(' : ')';
            sb.Append($"{c}-{b.i} ");
        }
        return sb.ToString();
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
