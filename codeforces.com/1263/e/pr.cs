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


(RaRbR)L)L(
-1 -1 -1 -1 -1 -1 1 1 -1 -1 2 

L:
,
,
0

R:
( 0, 
,
-1




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
        for (int inputInx = 0; inputInx < n; inputInx++)
        {
            char c = input[inputInx];
            // Change state:
            switch (c)
            {
                case 'R':
                    if (rB.Any() && rB.Peek().i == cI)
                    {
                        (bool t, int i) b = rB.Pop();
                        lB.Push(b);
                        if (b.t) // '('
                        {
                            lO.Push(lO.TryPeek(out var lONum) ? lONum + 1 : 1);
                            lD.Push(lD.TryPeek(out var lDNum) ? lDNum : 0);
                            rC.Pop();
                            rD.Pop();
                        }
                        else // ')'
                        {
                            if (!lO.TryPeek(out var lONum))
                               lONum = 0;
                            var rCNum = rC.Pop();
                            lD.Push(Max(
                                lD.TryPeek(out var lDNum) ? lDNum : 0,
                                lONum == rCNum ? lONum : INF
                            ));
                            lO.Push(lONum);
                            rD.Pop();
                        }
                    }
                    cI++;
                    break;
                case 'L':
                    cI--;
                    if (lB.Any() && lB.Peek().i == cI)
                    {
                        (bool t, int i) b = lB.Pop();
                        rB.Push(b);
                        if (b.t) // ')'
                        {
                            rO.Push(rO.TryPeek(out var rONum) ? rONum + 1 : 1);
                            rD.Push(rD.TryPeek(out var rDNum) ? rDNum : 0);
                            lC.Pop();
                            lD.Pop();
                        }
                        else // '('
                        {
                            if(!lO.TryPop(out var lONum))
                                lONum = 0;
                            if(rC.TryPeek(out var rCNum))
                                rCNum = 0;
                            rD.Push(Max(
                                !rD.TryPeek(out var rDNum) ? rDNum : 0,
                                lONum == rCNum ? lONum : INF
                            ));
                            rC.Push(rCNum);
                        }
                    }
                    break;
                case '(' || ')':
                    if (rB.TryPeek(out var rBb) && rBb.i == cI)
                    {
                        // Rewrite right stack.
                        rB.Pop();
                        rC.Pop();
                        rD.Pop();
                        rB.Push((c == '(', cI));
                        if (rBb.t && (c == ')')) 
                        { 
                            // From '(' to ')'.
                            var rDNum = rD.Pop();
                            rD.Push(rD.TryPeek(out var rDPrevNum) ? rDPrevNum : 0);
                            var rCNum = rC.Pop();
                            rC.Push(rCNum + 1);
                        }
                        else if (!rBb.t && (c == '(')) 
                        { 
                            // From ')' to '('.
                            var rCNum = rC.Pop();
                            rCNum--;
                            rC.Push(rCNum);
                            if(!lO.TryPop(out var lONum))
                                lONum = 0;
                            rD.Pop();
                            rD.Push(Max(
                                rD.TryPeek(out var rDPrevNum) ? rDPrevNum : 0,
                                lONum == rCNum ? lONum : INF
                            ));
                        }
                        // Else the same braket.
                    }
                    else 
                    {
                        // Add to right stack.
                        rB.Push((c == '(', cI));
                        if (c == '(')
                        {
                            if(!lO.TryPop(out var lONum))
                                lONum = 0;
                            lONum++;
                            if(rC.TryPeek(out var rCNum))
                                rCNum = 0;
                            if (!rD.TryPeek(out var rDNum))
                                rDNum = 0;
                            rD.Push(Max(
                                rDNum,
                                lONum == rCNum ? lONum : INF
                            ));
                            rC.Push(rCNum);
                        }
                        else // ')'
                        {
                            rD.Push(rD.TryPeek(out var rDNum) ? rDNum : 0);
                            rC.Push(rC.TryPeek(out var rCNum) ? rCNum + 1 : 1);
                        }
                        
                    }
                    break;
                default:
                    // Rewrite if on a braket.
                    if (cI == (rB.TryPeek(out var rBb) ? rBb.i : -1))
                    {
                        // Delete braket at right stack.
                        rB.Pop();
                        rD.Pop();
                        rC.Pop();
                    }
                    break;
            }
            // Get max:
            {
                int localMax = lD.TryPeek(out var lDNum) ? lDNum : 0;
                localMax = Max(localMax, rD.TryPeek(out var rDNum) ? rDNum : 0);
                if (lO.TryPeek(out var lONum))
                    lONum = 0;
                if (rC.TryPeek(out var rCNum))
                    rCNum = 0;
                localMax = Max(localMax, lONum == rCNum ? lONum : INF);

                Write(localMax == INF ? -1 : localMax);
            }
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
