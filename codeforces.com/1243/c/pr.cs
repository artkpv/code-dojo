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
 
    /// <summary>
    /// Keep track of tree size and take steps to avoid having tall trees.
    /// Smaller tree will connect to the root of the larger tree.
    /// Java implementation on p. 228
    /// Depth of any node x is at most lg N (lg = base-2 logarithms)
    /// If N is 1,000 its 10 (2^10 = 1000)
    /// If N is 1,000,000 its 20 (2^20)
    /// If N is 1,000,000,000 its 30 (2^30)
    /// Can also add path compression: just after computing root of p, 
    /// set the id of each examined node to point to that root
    /// </summary>
    public class QuickUnionUF2 // Weighted Quick Union
    {
        private int[] id;
        private int[] sz;
        private int count; // number of components

        public QuickUnionUF2(int N)
        {
            id = new int[N];
            for (int i = 0; i < N; i++) id[i] = i;

            sz = new int[N];
            for (int i = 0; i < N; i++) sz[i] = 1;
            count = N;
        }

        public int Count() { return count;  }

        private int Root(int i)
        {
            // Chase parent ID until reach the root (depth of i array accesses)
            while (i != id[i])
            {
                // Halves path length. No reason not to, keeps tree almost completely flat.
                id[i] = id[id[i]]; // Only 1 extra line of code to do path compression improvement! 
                
                i = id[i];
            }
            return i;
        }

        public bool Connected(int p, int q) // Find
        {
            return Root(p) == Root(q);
        }

        public void Union(int p, int q)
        {
            int i = Root(p);
            int j = Root(q);

            if (i == j) return;

            // Make smaller root point to the larger root.
            if (sz[i] < sz[j]) // if i is smaller than j
            {
                id[i] = j; // point i to new root j
                sz[j] += sz[i]; // add the count of the smaller array to the count of the larger array
            }
            else // if j is smaller than i
            {
                id[j] = i;
                sz[i] += sz[j];
            }

            count--; // if we combine components, the count of components goes down by 1
        }
    }

public class Solver
{
    public IEnumerable<int> Factor(int number) {
        int max = (int)Math.Sqrt(number);  //round down
        for(int factor = 2; factor <= max; ++factor) { //test from 1 to the square root, or the int below it, inclusive.
            if(number % factor == 0) {
                yield return factor;
                if(factor != number/factor) { // Don't add the square root twice!  Thanks Jon
                    yield return number/factor;
                }
            }
        }
    }

    public void Solve()
    {
        /*
         * a - b = c    a = c + b
         * n % c == 0
         */
        long n = ReadLong();

        var primes = new Dictionary<long,int>();
        long nn = n;
        long x = 2;
        while (1 < nn && x * x <= n) 
        {
            while (nn % x == 0) 
            {
                if (!primes.ContainsKey(x))
                    primes[x] = 0;
                primes[x]++;
                nn /= x;
            }
            x++;
        }
        if (1 < nn)
            primes[nn] = 1;


        if (primes.Count() == 1)
            Write(primes.First().Key);
        else if (!primes.Any())
            Write(n);
        else
            Write(1);

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
