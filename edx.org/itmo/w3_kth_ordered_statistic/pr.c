/*

In:
2 <= n <= 4*10^7
1<=k1<=k2<=n, k2-k1 < 200
a_i = A*a[i-2] + B*a[i-1] + C
|A,B,C,a1,a2| <= 10^9

Out: 
k1..k2

E1
5 3 4
2 3 5 1 2
> 13 48
1 2 [13 48]

E2
5 3 4
200000 300000 5 1 2
> 2 800005
1 2 800005 

I1
generate -> sort -> iterate a[k1:k2+1]
 Time out

I2 
generate -> k-th order statistic ?


*/
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

inline void _swap(int * leftp, int * rightp) 
{
    int temp = *leftp;
    *leftp = *rightp;
    *rightp = temp;
}

void sort_interval(int * a, int k1, int k2, int l, int r) {
    /*
    Ex1. [1 2 13 48], 3, 4, 0, 3
         i-1 = 0
    pivot=2
    i j 
    0 3

    Ex2. [1 2 85 -51, 133], 3, 4, 0, 4
    pivot = 85
    i j
    0 4  
    1 2 -51 85 133

    Ex3
    [1 2 800005 -516268571 1331571109], 3, 4, 0, 4
    pivot=8..5
    i j
    0 4
    */

    if (l >= r)
        return;
    int m = (l+r)/2;
    // m = a[l] < a[m] && a[m] < a[r] ? m : 
      //           (a[l] < a[r] && a[r] < a[m] ? r : l);
    int pivot = a[m];
    _swap(a+r, a+m);
    int i = l, j = r-1;
    while (i <= j) 
    {
        while (a[i] <= pivot) 
        {
            if (i == r) break;
            i++;
        }
        while (pivot <= a[j]) 
        {
            if (j == l) break;
            j--;
        }
        if (i >= j) break;
        _swap(a+i, a+j);
        i++;
        j--;
    }
    _swap(a+r, a+i);
    // Now it is: a[l..i-1] <= pivot <= a[i+1..r]
    if (k1 < i) 
        sort_interval(a, k1, k2, l, i-1);
    if (i < k2)
        sort_interval(a, k1, k2, i+1, r);
}
 
int main( int argc, char *argv[]) {
	freopen(argc > 1 ? argv[1] : "input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int n, k1, k2;
    scanf("%d %d %d", &n, &k1, &k2);
    int A,B,C,a1,a2;
    scanf("%d %d %d %d %d", &A, &B, &C, &a1, &a2);
    int * a = (int*)calloc(n, sizeof(int));
    a[0] = a1;
    a[1] = a2;
    for(size_t i = 2; i < n; i++)
        a[i] = (int) ((int)A*a[i-2] + (int)B*a[i-1] + C);  // ignore int overflow.. 

    sort_interval(a, k1-1, k2-1, 0, n-1);
    
    for(size_t i = k1-1; i <= k2-1; i++)
        printf("%d ", a[i]);
    return 0;
}