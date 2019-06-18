#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 *
 * max(profit(i,j) + max(profit(0,i-1), profit(j+1,n))), 1 <= i,j <= n 
 *
 * I 1 
 * T: O(N^6)
 * S: 1
 *
 *
 * I 2
 * DP
 * P(0,j)
 * P(j,n)
 *
 * 
 */

inline int max(int a, int b)
{
    return a < b ? b : a;
}

int maxProfit(const int* prices, int n1) {
    if (n1 == 0)
        return 0;
    int leftprofit[n1];
    leftprofit[0] = 0;
    int min_ = prices[0];
    int i;
    for (i = 1; i < n1; i++)
    {
        leftprofit[i] = max(leftprofit[i-1], prices[i] - min_);
        if (min_ > prices[i])
            min_ = prices[i];
    }
    int rightprofit[n1];
    rightprofit[n1-1] = 0;
    int max_ = prices[n1-1];
    for (i = n1-2; i >= 0; i--)
    {
        rightprofit[i] = max(rightprofit[i+1], max_ - prices[i]);
        if (max_ < prices[i])
            max_ = prices[i];
    }
    int optimal = 0;
    for (i = 0; i < n1; i++) 
    {
        optimal = max(optimal, leftprofit[i] + rightprofit[i]);
    }
    return optimal;
}

/*
 * E 1
 * 1 2 1 2 
 * lp 
 * 0 1 2 3
 * 0 1 1 1
 * rp 
 * 0 1 2 3
 * 1 1 1 0
 * optimal 
 * 1 2 2 2
 * 2
 */

int main() 
{
    return 0;
}
