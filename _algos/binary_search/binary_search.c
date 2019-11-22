#include <stdio.h>
#include <assert.h>

int bs_left(int a[], int size, int val)
{
    int lo = 0;
    int hi = size; // So we can return n-th index.
    while (lo < hi)
    {
        int mid = (lo + hi) / 2;
        if (a[mid] < val)
            lo = mid+1;
        else
            hi = mid;
    }
    return lo;
}

int main() 
{
    int a[] = {1,2,3,4,5,6,7,8,9,10};
    int res = bs_left(a, 11, 6);
    printf("%d\n", res);
    assert(res == 5);

    int c[] = {1,10,100};
    res = bs_left(c, 3, 101);
    printf("%d\n", res);
    assert(res == 3);

    int b[] = {1};
    res = bs_left(b, 1, 6);
    printf("%d\n", res);
    assert(res == 1);

    return 0;
}
