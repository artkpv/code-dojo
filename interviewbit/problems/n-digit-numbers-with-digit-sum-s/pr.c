/**
 * @input A : Integer
 * @input B : Integer
 * 
 * @Output Integer
 */

#define ll long long

const int MAXN = 100;
const int MAXS = 1000;
const ll MOD = 1000000007;

#include <stdio.h>
#include <assert.h>
 
ll _solve(ll DP[MAXN][MAXS], int n, int s) 
{
    if (n == 0 && s == 0)
        return 1;
    if (DP[n][s] == -1) 
    {
        ll count = 0;
        int i;
        for (i = 0; i <= 9; i++)
        {
            if (s - i < 0)
                continue;
            count = (count + _solve(DP, n-1, s - i)%MOD) % MOD;
        }
        DP[n][s] = count;
    }
    return DP[n][s];
}

int solve(int n, int s) {
        
    ll DP[MAXN][MAXS];
    int i, j;
    for (i = 0; i < MAXN; i++)
    {
        for (j = 0; j < MAXS; j++)
            DP[i][j] = -1;
    }
    if (n == 0)
        return 0;
    ll count = 0;
    for (i = 1; i <= 9; i++) 
    {
        if (s-i < 0)
            continue;
        count = (count + _solve(DP, n-1, s-i)%MOD) % MOD;
    }
    return (int)count;
}


int main()
{
    assert(solve(2, 4) == 4);
    assert(solve(75, 22) == 478432066);
    assert(solve(22, 96) == 290751713);

    printf("done\n");

    return 0;
}
