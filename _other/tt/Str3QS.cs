// #undef TRACE

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using System.Linq.Expressions;

public class Str3QS
{

    public void Sort(string[] arr, int lo, int hi, int d) 
    {
        // Trace.Assert(false);
        Trace.WriteLine("Trace.WriteLine"); 
        Debug.WriteLine("Debug.WriteLine"); 
        Debug.Assert(false);

        Func<int, char?> CharAt = k => (k < arr.Count() && d < arr[k].Length) ? arr[k][d] : (char?) null;
        Func<char?, char?, int> Compare = (left, right) =>
            right == null ? 1 : (left?.CompareTo(right) ?? -1);

        Action<int, int> Exch = (k, j) =>
        {
            string t = arr[k];
            arr[k] = arr[j];
            arr[j] = t;
        };
        Console.Write

        if (lo >= hi)
            return;
        int mid = (lo + hi) / 2;
        char? p = CharAt(mid);
        int lt = lo-1;
        int gt = hi+1;
        int i = lo;
        while (i < gt) 
        {
            int cmp = Compare(CharAt(i), p);
            if (cmp < 0)
            {
                lt++;
                Exch(lt, i);
                i++;
            }
            else if (cmp == 0) 
            {
                i++;
            }
            else // if (cmp > 0)
            {
                gt--;
                Exch(i, gt);
            }
        }
        // Inv: [ <p, lt| =p, i|gt, >p ]
        Sort(arr, lo, lt, d);
        if (gt - lt - 1 > 0)
            Sort(arr, lt + 1, gt - 1, d+1);
        Sort(arr, gt, hi, d);
    }

    public void Test()
    {
        string[] arr = new[] {
            "abb",
            "bb",
            "aabb",
            "aaabb",
            "cccaa",
            "ccaa",
            "ab"
        };
        Sort(arr, 0, arr.Count() - 1, 0);
        
        Console.Write(string.Join("\n", arr));
    }
}
