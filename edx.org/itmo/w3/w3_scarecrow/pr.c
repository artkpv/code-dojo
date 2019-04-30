#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void exch(int a[], int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
}

void k_sort(int a[], int n, int k, int left, int right) {
    if (left >= right)
        return;
    int elements_num = 1 + (right-left) / k;
    int middle = left  + k * ((elements_num - 1) / 2);
    int pivot = a[middle];
    exch(a, left, middle);
    int i = left + k;
    int j = right;
    while (i <= j) {
        while (a[i] <= pivot) {
            if (i == right) 
                break;
            i += k;
        }
        while (a[j] >= pivot) {
            if (j == left)
                break;
            j -= k;
        }
        if (i >= j) 
            break;
        exch(a, i, j);
    }
    exch(a, left, j);
    k_sort(a, n, k, left, j-k);
    k_sort(a, n, k, j+k, right);
}

int main() {

    #ifdef JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #endif


    int n, k;
    scanf("%d %d", &n, &k);
    int a[n];
    for (int i = 0; i < n; i++) {
        int e;
        scanf("%d ", &e);
        a[i] = e;
    }

    if (k == 1)  {
        printf("YES");
        return 0;
    }

    int full = n / k;
    if (full > 0) {
        for (int start = 0; start < k; start++) {
            int end = k * full + start;
            if (end >= n) 
                end -= k;
            k_sort(a, n, k, start, end);
        }
    }
    
    bool issorted = true;
    for (int i = 1; i < n; i++) {
        if (a[i-1] > a[i]) {
            issorted = false;
            break;
        }
    }

    printf(issorted ? "YES" : "NO");

    return 0;
}
