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
        Console.WriteLine(String.Join(' ', a));
    }

    private static int Inversions(int[] a)
    {
        int inversions = 0;
        int[] aux = new int[a.Length];
        Mergesort(a, 0, a.Length - 1, aux, ref inversions);
        return inversions;
    }

    private static void Mergesort(int[] a, int l, int r, int[] aux, ref int inversions)
    {
        if (l >= r) return;
        int m = (l + r) / 2;
        Mergesort(a, l, m, aux, ref inversions);
        Mergesort(a, m + 1, r, aux, ref inversions);

        for (int ii = l; ii <= r; ii++)
            aux[ii] = a[ii];

        int i = l, j = m + 1;
        for (int k = l; k <= r; k++) {
            if (j > r || (i <= m && aux[i] < aux[j]))
                a[k] = aux[i++];
            else {
                if (i <= m)
                    inversions += m - i + 1;
                a[k] = aux[j++];
            }
        }
    }
}