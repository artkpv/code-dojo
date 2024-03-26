using System;
using System.Collections.Generic;

public static class A
{
    public static int Main() 
    {
        var n = new List<int>();
        n.Add(1);

        var start = DateTime.Now;
        int count = 0;
        var cache = new Dictionary<int, bool>();
        while(n.Count <= 8)
        {
            bool is_r = IsR(n);
            if (is_r)
                count++;
            Inc(n);
            Console.Write($"\r {DateTime.Now - start}, n.Count {n.Count}, last {n[n.Count - 1]}, count {count}");
        }
        return 1;
    }

    static void Inc(List<int> n)
    {
        for(int i = 0; i < n.Count; i++) 
        {
            if (n[i] < 9)
            {
                n[i] += 1;
                return;
            }
            n[i] = 0;
        }
        n.Add(1);
    }

    static bool IsR(List<int> n)
    {
        if (n[0] == 0)
            return false;
        var rem = 0;
        for(int i = 0; i < n.Count; i++) 
        {
            var d = n[i] + n[n.Count - i - 1] + rem;
            if (d % 2 == 0)
                return false;
            rem = d / 10;
        }
        return true;
    }
}
