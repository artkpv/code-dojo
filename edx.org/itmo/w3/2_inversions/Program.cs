
using System;
using System.Linq;
using System.Linq.Expressions;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Diagnostics;

public static class A
{
    public static void Main()
    {
        string[] lines = File.ReadLines("input.txt").ToList().ToArray();
        int n = int.Parse(lines[0].Trim());
        var a = lines[1].Trim().Split(' ').Select(int.Parse).ToArray();
        File.WriteAllText("output.txt", Inversions(a).ToString());
        // Console.WriteLine(String.Join(" ", a.Select(i=>i.ToString())));
    }

    private static UInt64 Inversions(int[] a)
    {
        int[] aux = new int[a.Length];
        return Inversions(a, 0, a.Length - 1, aux);
    }

    private static UInt64 Inversions(int[] a, int l, int r, int[] aux)
    {
/*
10
1 8 2 1 4 7 3 2 3 6

1 8
2
1 2 8 
1 4

1 2 8   1 4


1 8 2 1 4
7 3 2 3 6

*/
        if (l >= r) return 0;
        int m = (l + r) / 2;
        UInt64 count = 0;
        count += Inversions(a, l, m, aux);
        count += Inversions(a, m + 1, r, aux);

        // merge:
        for (int ii = l; ii <= r; ii++)
            aux[ii] = a[ii];

        int i = l, j = m + 1;
        for (int k = l; k <= r; k++) {
            if (j > r || (i <= m && aux[i] <= aux[j]))
                a[k] = aux[i++];
            else {
                if (i <= m)
                    count += (uint)(m - i + 1);
                a[k] = aux[j++];
            }
        }
        return count;
    }
}