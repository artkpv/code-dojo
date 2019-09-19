
using System;
using System.Collections;
using System.Collections.Generic;

class Solution {
    private const int MOD = 1000000007;
    
    private Dictionary<Tuple<int, int>, int> dp = new Dictionary<Tuple<int, int>, int>();
    
    private int _solve(int N, int S)
    {
        if (N == 1 && S/10 == 0)
            return 1;
        var p = Tuple(N, S);
        if (!dp.ContainsKey(p))
        {
            int res = 0;
            for (int i = 0; i <= 9; i++)
            {
                res = (res + _solve(N-1, S - i)) % MOD;
            }
            dp[p] = res;
        }
        return dp[p];
    }
    
    public int solve(int N, int S) {
        if (N <= 0)
            return 0;
        if (N == 1 && S/10 == 0)
            return 1;
        
        int res = 0;
        for (int i = 1; i <= 9; i++)
        {
            res = (res + this._solve(N-1, S - i))%MOD;
        }
        return res;
    }

    public static void Main() 
    {}
}
