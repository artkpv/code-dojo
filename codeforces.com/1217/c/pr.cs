using System;
using System.Collections.Generic;


public class Solution 
{
    const int MAXN = 18;
    static int MAX = (int)System.Math.Pow(2, MAXN)-1;

    public int f_old(int x, int xlen, int l, int r) 
    {
        int n = r - l + 1;
        return (x >> (xlen -r-1)) & (MAX >> (MAXN - n));
    }

    public int f(string s, int l, int r)
    {
        int res = 0;
        for (int i = 0; i < r - l + 1; i++)
        {
            int j = r - i;
            if (s[j] == '1')
                res += (1 << i);
        }
        return res;
    }

    public void Solve() 
    {
        int queries = int.Parse(Console.ReadLine().Trim());
        for (int q = 0; q < queries; q++) 
        {
            string s = Console.ReadLine().Trim();
            // int sint = Convert.ToInt32(s, 2);
            int n = s.Length;
            var nxt = new List<int>();
            nxt.Add(-1);
            for (int i = 0; i < n; i++) 
                nxt.Add(s[i] == '1' ? i : nxt[nxt.Count-1]);
            int count = 0;
            for (int r = n-1; r >= 0; r--)
            {
                int l = nxt[r+1];
                while (l > -1 && r - l + 1 <= MAXN)
                {
                    int f_lr = f(s, l, r);
                    if (f_lr <= r - nxt[l])
                        count += 1;
                    l = nxt[l];
                }
            }
            Console.WriteLine(count);
        }
    }
}

public static class Programm 
{
    public static void Main()
    {
        new Solution().Solve();
    }
}
