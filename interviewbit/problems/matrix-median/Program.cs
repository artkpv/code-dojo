using System;
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

/*
1 3 5
2 6 9 
3 6 9 

3 6 6
3



 */

public class Solution {
    public static void Debug(String msg)
    {
        // Console.WriteLine(msg);
    }
    // Where n will be inserted to maintain order.
    // Left most.
    public int BisectLeft(List<int> array, int  n) 
    {
        int lo = 0;
        int hi = array.Count-1;
        while (lo < hi) 
        {
            int mid = (lo+hi)/2;
            if (array[mid] < n)
                lo = mid+1;
            else 
                hi = mid;
        }
        if (array[lo] < n)
            lo++;
        // Debug(String.Join(" ", array) + " - " + n + ": " + lo);
        return lo;
    }

    public int GetMin(List<List<int>> A, int previous) 
    {
        int min = int.MaxValue;
        for (int i = 0; i < A.Count; i++)
        {
            int bisectInx = BisectLeft(A[i], previous + 1);
            if (bisectInx >= A[i].Count)
                continue;
            if (A[i][bisectInx] < min)
                min = A[i][bisectInx];
        }
        return min;
    }

    public int BisectSum(List<List<int>> A, int n) 
    {
        int count = 0;
        for (int i = 0; i < A.Count; i++)
        {
            int bisectInx = BisectLeft(A[i], n);
            count += bisectInx;
        }
        // Debug("Count " + n + " " + count);
        return count;
    }

    public int findMedian(List<List<int>> A) {
        int min = int.MaxValue;
        for (int i = 0; i < A.Count; i++)
        {
            int x = A[i][A[i].Count/2];
            if (x < min)
                min = x;
        }

        int expected = (A.Count*A[0].Count)/2;
        while (true) 
        {
            int lt = BisectSum(A, min);
            int le = BisectSum(A, min+1);
            // Debug("Median " + min + ": " + lt + " " + le);
            if (lt <= expected && expected < le)
                return min;
            min = GetMin(A, min);
        }
    }
}


public static class Prog
{
    public static void Main() 
    {
        List<List<int>> A = new List<List<int>>();
        int N = int.Parse(Console.ReadLine().Trim());
        for (int i = 0; i < N; i++)
        {
            List<int> row = Console.ReadLine().Trim().Split(' ')
                .Select(int.Parse).ToList();
            A.Add(row);
        }
        var solution = new Solution();
        int answer = solution.findMedian(A);
        Console.WriteLine(answer);
    }
}
