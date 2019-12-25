#include <stdio.h>
#include <stdlib.h>


int main() 
{
    int n;
    scanf("%d", &n);
    int a[n];
    int i;
    for (i = 0; i < n; ++i) {
        scanf("%d", (a+i));
    }

    int gap = 1;
    while (gap < n)
        gap = gap * 3 + 1;
    gap /= 3;

    long long count = 0;

    while (gap >= 1)
    {
        for (i = gap; i < n; i++) {
            int j = i;
            while (j-gap >= 0 && a[j-gap] > a[j])
            {
                int t = a[j-gap];
                a[j-gap] = a[j];
                a[j] = t;
                j -= gap;
                count++;
            }
        }
        gap /= 3;
    }

    /*for (int i = 0; i < n; i++)*/
        /*printf("%d ", a[i]);*/
    /*printf("\n");*/

    printf("Exchanges: %d\n", count);
    return 0;
}
