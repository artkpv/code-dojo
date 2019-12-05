#undef DEBUG
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

public class Solution
{
    List<int> _A;
    List<Tuple<int, int>> _dpf;
    List<int> _dpf_index;
    Dictionary<int, int> _dProductCache = new Dictionary<int, int>();
    const long MOD = (long)(1e9 + 7);

    private int DProduct(int n)
    {
        if (!_dProductCache.ContainsKey(n))
        {
            int ans;
            if (n == 1)
            {
                ans = 1;
            }
            else 
            {
                ans = n;
                int d = 2;
                while (d * d <= n)
                {
                    if (n % d == 0)
                    {
                        ans = (int) (((long) ans * (long) d) % MOD);
                        if (d * d != n)
                            ans = (int) (((long) ans * (long) (n/d)) % MOD);
                    }
                    d++;
                }
                //long d = 2;
                //long count = 2;
                //while (d * d <= n)
                //{
                    //if (n % d == 0) 
                    //{
                        //count += 2;
                        //if (d * d == n) 
                            //count--;
                    //}
                    //d++;
                //}
                //ans = (int)(Math.Pow(n, (double)count / 2.0) % MOD);
            }
            _dProductCache[n] = ans;
            //Debug.WriteLine($" Dproduct {n} = {ans}");
        }
        return _dProductCache[n]; 
    }

    private void AddMax(int lo, int hi)
    {
        //Debug.WriteLine($"AddMax({lo} {hi})");
        if (lo > hi)
            return;
        int inx = -1;
        int inxMax = int.MinValue;
        for (int i = lo; i <= hi; i++)
        {
            if (_A[i] > inxMax)
            {
                inxMax = _A[i];
                inx = i;
            }
        }
        //Debug.WriteLine($" inx={inx}");
        int freq = (inx - lo + 1) * (hi - inx + 1);
        int dp = DProduct(inxMax);

        var newT = Tuple.Create(dp, freq);
        if (_dpf.Any() && _dpf.Last().Item1 == dp)
        {
            newT = Tuple.Create(dp, newT.Item2 + _dpf.Last().Item2);
            _dpf.RemoveAt(_dpf.Count() - 1);
        }
        _dpf.Add(newT);
        //Debug.WriteLine($" > {newT}");
        AddMax(lo, inx-1);
        AddMax(inx+1, hi);
    }

    private int Query(int inx)
    {
        int lo = 0;
        int hi = _dpf_index.Count() - 1;
        while (lo < hi)
        {
            int mid = (lo + hi) /2;
            if (_dpf_index[mid] <= inx && inx < _dpf_index[mid+1])
            {
                lo = mid;
                hi = mid;
            }
            else if (inx < _dpf_index[mid])
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        return _dpf[lo].Item1;
    }

    public List<int> solve(List<int> A, List<int> B) {
        _A = A;
        _dpf = new List<Tuple<int, int>>();
        int n = A.Count();
        AddMax(0, n-1);
        _dpf.Sort();
        Debug.WriteLine(string.Join(" ", _dpf));
        _dpf_index = new List<int>();
        _dpf_index.Add(0);
        for (int i = 0; i < _dpf.Count() - 1; i++)
        {
            _dpf_index.Add(_dpf_index.Last() + _dpf[i].Item2);
        }
        _dpf_index.Add(_dpf_index.Last() + _dpf.Last().Item2);
        Debug.WriteLine(string.Join(" ", _dpf_index));
        int inum = n * (n+1) / 2;
        var ans = new List<int>();
        foreach (int b in B)
        {
            ans.Add(Query(inum - b));            
        }
        return ans;
    }

    #region Main

    protected static TextReader reader;
    protected static TextWriter writer;
    public static void Main()
    {
        Trace.Listeners.Clear();
        Trace.Listeners.Add(new ConsoleTraceListener());

        reader = new StreamReader(Console.OpenStandardInput());
        writer = new StreamWriter(Console.OpenStandardOutput());

        var A = ReadIntArray().ToList();
        var B = ReadIntArray().ToList();
        Debug.WriteLine(string.Join(" ", A));
        Debug.WriteLine(string.Join(" ", B));
        var ans = new Solution().solve(A, B);
        Write(string.Join(" ", ans));

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


public class Tuple<T1, T2>
{
    private readonly T1 m_Item1; // Do not rename (binary serialization)
    private readonly T2 m_Item2; // Do not rename (binary serialization)

    public T1 Item1 { get { return m_Item1; }} 
    public T2 Item2 { get { return m_Item2; }}

    public static Tuple<T1, T2> Create<T1, T2>(T1 item1, T2 item2)
    {
        return new Tuple(item1, item2);
    }

    public Tuple(T1 item1, T2 item2)
    {
        m_Item1 = item1;
        m_Item2 = item2;
    }

    public override bool Equals(object other)
    {
        if (other == null) return false;

        if (!(other is Tuple<T1, T2>))
        {
            return false;
        }
        Tuple<T1, T2> objTuple = (Tuple<T1, T2>) other;
        return m_Item1.Equals(objTuple.m_Item1) && m_Item2.Equals(objTuple.m_Item2);
    }

    public override int GetHashCode()
    {
        return m_Item1.GetHashCode();
    }

}
