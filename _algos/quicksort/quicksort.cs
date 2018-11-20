using System;
using System.Linq;
using System.Collections.Generic;

public class A {
	public static void Main() {
		int n = 100;
		int[] a = new int[n];
		for(int i = 0; i < n; i++)
			a[i] = (n-i)%(n/2);
		
		sort(a, 0, n-1);
		foreach (int i in a)
			System.Console.Write(i + " ");
		System.Console.Write("\n");
	}

	private static void sort(int[] a, int lo, int hi)
	{
		if (hi <= lo) return;
		int j = partition(a, lo, hi); // Partition (see page 291).
		sort(a, lo, j-1); // Sort left part a[lo .. j-1].
		sort(a, j+1, hi); // Sort right part a[j+1 .. hi].
	}

	private static int partition(int[] a, int lo, int hi)
	{ 
		// Partition into a[lo..i-1], a[i], a[i+1..hi].
		int i = lo, j = hi+1; // left and right scan indices
		int v = a[lo]; // partitioning item
		while (true)
		{ // Scan right, scan left, check for scan complete, and exchange.
			while (a[++i] < v) if (i == hi) break;
			while (v < a[--j]) if (j == lo) break;
			if (i >= j) break;
			exch(a, i, j);
		}
		exch(a, lo, j); // Put v = a[j] into position
		return j; // with a[lo..j-1] <= a[j] <= a[j+1..hi].
	}

	private static void exch(int[] a, int i, int j) {
		int t = a[i];
		a[i] = a[j];
		a[j] = t;
	}
}

