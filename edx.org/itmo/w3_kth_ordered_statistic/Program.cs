using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace w3_kth_ordered_statistic
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadLines(args.Count() > 0 ? args[0] : "input.txt").ToArray();
            int[] n_k1_k2 = lines[0].Split(' ').Select(int.Parse).ToArray();
            int[] A_B_C_a1_a2 = lines[1].Split(' ').Select(int.Parse).ToArray();
            int n = n_k1_k2[0],
                k1 = n_k1_k2[1],
                k2 = n_k1_k2[2],
                A = A_B_C_a1_a2[0],
                B = A_B_C_a1_a2[1],
                C = A_B_C_a1_a2[2],
                a1 = A_B_C_a1_a2[3],
                a2 = A_B_C_a1_a2[4];

            int[] array = new int[n];
            array[0] = a1;
            array[1] = a2;
            for(int i = 2; i < n; i++)
            {
                array[i] = A*array[i-2] + B*array[i-1] + C;
            }

            PartialSort(array, k1-1, k2-1, 0, array.Length - 1);

            using(var writer = new StreamWriter(File.Open("output.txt", FileMode.Create, FileAccess.Write)))
            {
                for (int i = k1-1; i < k2; i++)
                {
                    writer.Write(array[i]);
                    writer.Write(' ');
                }
            }
        }

        private static void Swap(int[] a, int left, int right)
        {
            int t = a[left];
            a[left] = a[right];
            a[right] = t;
        }

        private static void PartialSort(int[] a, int k1, int k2, int l, int r)
        {
            if (l >= r)
                return;
            int m = (l+r)/2;
            int pivot = a[m];
            Swap(a, r, m);
            int i = l, j = r-1;
            while (i <= j) 
            {
                while (a[i] <= pivot) 
                {
                    if (i == r) break;
                    i++;
                }
                while (pivot <= a[j]) 
                {
                    if (j == l) break;
                    j--;
                }
                if (i >= j) break;
                Swap(a, i, j);
                i++;
                j--;
            }
            Swap(a, r, i);
            // Now it is: a[l..i-1] <= pivot <= a[i+1..r]
            if (k1 < i) 
                PartialSort(a, k1, k2, l, i-1);
            if (i < k2)
                PartialSort(a, k1, k2, i+1, r);
        }

    }
}
