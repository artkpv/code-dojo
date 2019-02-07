/*
NEXT: implement k-th order statistic instead of QSort there. Quicker.

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

int compare_ints(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
 
    // return (arg1 > arg2) - (arg1 < arg2); // possible shortcut
    // return arg1 - arg2; // erroneous shortcut (fails if INT_MIN is present)
}
 
int main() {
	freopen("input.txt", "r", stdin);
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
    qsort(a, n, sizeof(int), compare_ints);
    for(size_t i = k1-1; i < k2; i++)
        printf("%d ", a[i]);
    return 0;
}