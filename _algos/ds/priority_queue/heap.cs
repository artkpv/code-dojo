#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using static System.Math;

namespace Heap
{
    public class MinHeaper<T> 
        where T : IComparable
    {
        private readonly IComparer<T> comparer;

        public MinHeaper(IComparer<T> comparer=null)
        {
            this.comparer = comparer ?? Comparer<T>.Default;
        }

        public void Heapify(IList<T> arr) 
        {
            for (int i = arr.Count()/2; i >= 0; i--)
                SiftDown(arr, i);                
        }

        public void Push(IList<T> arr, T el)  
        {
            arr.Add(el);
            SiftUp(arr, arr.Count() - 1);
        }

        public T Pop(IList<T> arr) 
        {
            if (!arr.Any())
                throw new ArgumentOutOfRangeException("Empty array");
            T el = arr.First();
            int n = arr.Count();
            arr[0] = arr[n-1];
            arr.RemoveAt(n-1);
            SiftDown(arr, 0);
            return el;
        }

        private void SiftUp(IList<T> arr, int i) 
        {
            while (Parent(i) >= 0 && arr[Parent(i)].CompareTo(arr[i]) > 0) 
            {
                Exch(arr, Parent(i), i);
                i = Parent(i);
            }
        }

        private int Parent(int i) => (i + 1) / 2 - 1;

        private void SiftDown(IList<T> arr, int i) 
        {
            int n = arr.Count();
            while ((i + 1) * 2 - 1 < n)
            {
                int k = (i + 1) * 2 - 1;
                if (k + 1 < n && arr[k+1].CompareTo(arr[k]) < 0)
                    k += 1;
                if (arr[i].CompareTo(arr[k]) <= 0)
                    break;
                Exch(arr, i, k);
                i = k;
            }
        }

        private void Exch(IList<T> arr, int i, int j)
        {
            T t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
        }
    }

    public class Solver
    {
        public static void Main() 
        {
            var heaper = new MinHeaper<int>();

            { 
                List<int> a1 = new List<int> {1};
                heaper.Push(a1, 2);
                AssertEqual(a1, new List<int> {1, 2});
                Console.WriteLine("test 1 done");
            }

            { 
                List<int> a = new List<int>();
                heaper.Push(a, 10);
                Trace.Assert(a[0] == 10);
                heaper.Push(a, 1);
                Trace.Assert(a[0] == 1);
                heaper.Push(a, 9);
                Trace.Assert(a[0] == 1);
                heaper.Push(a, 2);
                Trace.Assert(a[0] == 1);
                heaper.Push(a, 8);
                Trace.Assert(a[0] == 1);
                Trace.Assert(heaper.Pop(a) == 1);
                Trace.Assert(a[0] == 2);
                Trace.Assert(heaper.Pop(a) == 2);
                Trace.Assert(a[0] == 8);
                Trace.Assert(heaper.Pop(a) == 8);
                Trace.Assert(a[0] == 9);
                Trace.Assert(heaper.Pop(a) == 9);
                Trace.Assert(a[0] == 10);
                Trace.Assert(heaper.Pop(a) == 10);
                Trace.Assert(a.Count() == 0);
                Console.WriteLine("test 2 done");
            }
            {
                var a = new List<int>();
                for (int i = 10; i >= 0; i--)
                {
                    a.Add(i);
                }
                heaper.Heapify(a);
                Trace.Assert(a[0] == 0);
                for (int i = 0; i < 11; i++)
                {
                    Trace.Assert(heaper.Pop(a) == i);
                }
                Console.WriteLine("test 3 done");
            }
        }

        private static void AssertEqual<T>(IList<T> left, IList<T> right)
            where T : IComparable
        {
            Trace.Assert(
                left.Count() == right.Count(),
                $"left {left.Count()} != right {right.Count()}");
            for (int i = 0; i < left.Count(); i++)
            {
                Trace.Assert(
                    left[i].CompareTo(right[i]) == 0, 
                    $"left[{i}] {left[i]} != right[{i}] {right[i]}");
            }
        }

    }
}
