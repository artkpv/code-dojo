/*
Дан массив чисел длинны N. Нужно найти любые два числа РАЗНИЦА,
которых не превосходит значение t и не отстоящие друг от друга на k.


1) 
k-BST balanced. 
on each: add log(k) + delete log(k) + search log(k) 
Time O(log(k)*n)

 */
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace nearest_neighbors
{
    class Program
    {
        static void Main(string[] args)
        {
            Trace.Assert(GetTwoNeighbors(new[] {1,2}, 1, 1) == new[] {1,2});
            Trace.Assert(GetTwoNeighbors(new[] {1,100,2}, 1, 2) == new[] {1,2});
            Trace.Assert(GetTwoNeighbors(new[] {1,100,2}, 1, 1) == new int[0] );
	        Trace.Assert(GetTwoNeighbors( 
	                                      new[] {901, 99, 798, 201, 900, 100, 799, 200}, 
	                                      100, 2)
	                     == new[] {100,200});
			Console.WriteLine("Tests pass");
        }

	    private static int[] GetTwoNeighbors(int[] a, int t, int k)
	    {
		    var neighbors = new SortedSet<int>();
		    for (int i = 0; i < a.Length; i++)
		    {
			    if (i > k)
				    neighbors.Remove(a[i - k - 1]);

			    var found = neighbors.GetViewBetween(a[i] - t, a[i] + t);
			    if (found.Any())
				    return new[] {a[i], found.First()};
			    neighbors.Add(a[i]);
		    }
			return new int[0];
	    }
    }
}
