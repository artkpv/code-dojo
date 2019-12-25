/*
Pancake sorting

https://en.wikipedia.org/wiki/Pancake_sorting

How to sort arr if only flip available. 'Flip' is reverse k elements from left.

I1
for i in n..1:
  find max 1..i
  flip 0..max
  flip 0..i

Time: 
n*(n+n+n) = ~(n^2)

n*(n+6*n)

E1
1 5 4 3 2
2 3 4 5 1
5 4 3 2 1
1 2 3 4 5

E2
1 4 5 3 2
2 3 5 4 1
5 3 2 4 1
1 4 2 3 5


E3
5 4 3 1 2
2 1 3 4 5
1 2 3 4 5


E4
7 6 5 3 4
4 3 5 6 7 
3 4 5 6 7

E5



*/

using System;
using System.Linq;

public static class Solution
{
    public static void Flip(int[] arr, int k)
    {
        for (int i = 0; i < k / 2; i++)
        {
            int t = arr[i];
            arr[i] = arr[k - 1 - i];
            arr[k - 1 - i] = t;
        }
    }

    public static void PancakeSort(int[] a)
    {
        int num = a.Length;
        for (int i = num-1; i >= 0; i--) 
        {
          // Find max:
          int maxInx = i;
          for (int j = 0; j < i; j++) 
          {
            if (a[j] > a[maxInx]) 
              maxInx = j;
          }

          // Put max at its place:
          if (maxInx != i) 
          {
            Flip(a, maxInx + 1);
            Flip(a, i+1);
          }
        }
    }

    public static void Main(string[] args)
    {
        string line = Console.ReadLine().Trim();
        int[] arr = line.Split(' ').Select(int.Parse).ToArray();
        PancakeSort(arr);
        Console.WriteLine(string.Join(' ', arr));
    }
}


