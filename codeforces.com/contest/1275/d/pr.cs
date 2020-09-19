#undef DEBUG
/*
0
0 0
1
0 0
2
0 0
3
0 0
4
0 0
5
0 0
6
0.000557413600891862 0.00179168657429527
7
0.00390189520624303 0.0125418060200669
8
0.0154048849701024 0.0495880930663539
9
0.045444410661802 0.147537245363332
10
0.111876376864935 0.371796395823856
11
0.240321539635041 0.834454447154676
12
0.454975822400779 1.69522172537383
13
0.748337595907928 3.11006816914409
14
1 4.90650940009871
15
1 6.24139472722727
16
1 7.31877401550305
17
1 8.23983663171306
18
1 9.05411064907632
19
1 9.78923250662381
20
1 10.4654765524331
21
1 11.0985481909395
22
1 11.700071667463
23
1 12.2783882783883
24
1 12.8395604395604
25
1 13.3882783882784
26
1 13.9285714285714
27
1 14.4642857142857
28
1 15
 */
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Diagnostics;
using static System.Math;

public class Solver
{
    long total;
    const int VROWS = 3;
    const int ROWS = 4;
    const int VCOLS = 5;
    const int COLS = 7;

    private long CombinationsNum(int k)
    {
        //  5 4 3 
        //  1 2 3
        int n = ROWS*COLS;

        long y = 1;
        for (long i = 2; i <= Min(n-k, k); i++)
            y *= i;
        long x = 1;
        for (long i = ROWS*COLS; i > Max(n - k, k); i--)
            x *= i;            
        return x / y;
    }

    private IEnumerable<List<int>> Combinations(int n)
    {
        List<int> field = new List<int>();
        for (int i = 0; i < n; i++)
        {
            field.Add(i);
        }

        var copy = new List<int>(field);
        yield return copy;
        // Generate all combinations in loop:
        while (true)
        {
            // Find which field[i] to increase.
            int incInx = n-1;
            int lastPos = ROWS*COLS - (n - incInx);
            while (incInx >= 0 && field[incInx] >= lastPos)
            {
                incInx--;
                lastPos = ROWS*COLS - (n - incInx);
            }
            if (incInx < 0) // All combinations.
                break;

            field[incInx]++;
            // All to the right in increasing order
            for (int i = incInx + 1; i < n; i++)
                field[i] = field[i-1] + 1;

            // Debug.WriteLine($"incInx={incInx} lastPos={lastPos} field={string.Join(" ", field)}");
            copy = new List<int>(field);
            yield return copy;
        }
    }

    private void Restore(List<int> field)
    {
        int count;
        do
        {
            count = 0;
            // Try restore.
            for (int row = 0; row < ROWS; row++)
            {
                int[] onOne = field.Where(inx => inx / COLS == row).ToArray();
                if (onOne.Length <= COLS - VCOLS)
                {
                    foreach (int i in onOne)
                    {
                        field.Remove(i);
                        count++;
                    }
                }
            }

            for (int col = 0; col < COLS; col++)
            {
                int[] onOne = field.Where(inx => inx % COLS == col).ToArray();
                if (onOne.Length <= ROWS - VROWS)
                {
                    foreach (int i in onOne)
                    {
                        field.Remove(i);
                        count++;
                    }
                }
            }
        } while (count > 0);
    }

    public void Solve(int remNum)
    {
        total = CombinationsNum(remNum);
        Debug.WriteLine($"total={total}");

        var brokenCount = new ConcurrentDictionary<int, int>();

        List<List<int>> allCombinations = Combinations(remNum).ToList();;
        Parallel.ForEach(allCombinations, field => 
        {
            Debug.WriteLine($"combination={string.Join(" ", field)}");
            Restore(field);
            Debug.WriteLine($" field={string.Join(" ", field)}");
            int count = 0;
            foreach (int brokenInx in field) 
            {
                if (brokenInx / COLS < VROWS && brokenInx % COLS < VCOLS)
                    count++;
            }
            Debug.WriteLine($" count={count}");
            if (count > 0)
            {
                brokenCount.AddOrUpdate(count, 1, (k, v) => v + 1);
            }
            Debug.WriteLine($" brokenCount={string.Join(" ", brokenCount)}");
            Debug.Flush();
            // Console.ReadLine();
        });

        //Console.WriteLine($" brokenCount={string.Join(" ", brokenCount)}");
        Console.Write((double)brokenCount.Sum(keyValue => brokenCount[keyValue.Key]) / total);
        Console.Write(" ");
        double expectedValue = 0;
        foreach (KeyValuePair<int, int> keyValue in brokenCount)
        {
            expectedValue += keyValue.Key * ((double)keyValue.Value / total);
        }
        Console.WriteLine(expectedValue);
    }

    static void Main()
    {
        Debug.Listeners.Clear();
        Debug.Listeners.Add(new ConsoleTraceListener());
        Trace.Listeners.Clear();
        Trace.Listeners.Add(new ConsoleTraceListener());
        Debug.AutoFlush = true;
        Trace.AutoFlush = true;

        int n = int.Parse(Console.ReadLine());
        string[] answers = {
            "0 0",
            "0 0",
            "0 0",
            "0 0",
            "0 0",
            "0 0",
            "0.000557413600891862 0.00179168657429527",
            "0.00390189520624303 0.0125418060200669",
            "0.0154048849701024 0.0495880930663539",
            "0.045444410661802 0.147537245363332",
            "0.111876376864935 0.371796395823856",
            "0.240321539635041 0.834454447154676",
            "0.454975822400779 1.69522172537383",
            "0.748337595907928 3.11006816914409",
            "1 4.90650940009871",
            "1 6.24139472722727",
            "1 7.31877401550305",
            "1 8.23983663171306",
            "1 9.05411064907632",
            "1 9.78923250662381",
            "1 10.4654765524331",
            "1 11.0985481909395",
            "1 11.700071667463",
            "1 12.2783882783883",
            "1 12.8395604395604",
            "1 13.3882783882784",
            "1 13.9285714285714",
            "1 14.4642857142857",
            "1 15"};
        Console.WriteLine(answers[n]);
        // new Solver().Solve(n);
        // new Solver().Solve(28);
        //reader.Close();
        //writer.Close();
    }

}

