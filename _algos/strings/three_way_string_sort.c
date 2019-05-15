#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdbool.h>

int charat(const char * s, int d) {
    if (strlen(s) <= d)
        return -1;
    return s[d];
}

void exch(const char ** a, int i, int j) {
    const char * t = a[i];
    a[i] = a[j];
    a[j] = t;
}

void sort(const char ** a, int lo, int hi, int d) 
{
    while (lo < hi && strlen(a[lo]) <= d) 
        lo++;
    if (lo >= hi)
        return;
    int pivot = a[lo][d];
    int lt = lo, gt = hi, i = lo;
    while (i <= gt) {
        int compare = pivot - charat(a[i], d);
        if (compare < 0){
            exch(a, i++, gt--);
        }
        else if (compare > 0) {
            exch(a, i++, lt++);
        }
        else {
            i++;
        }
    }
    // invariant: a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi]
    sort(a, lo, lt-1, d++);
    if (lt < gt) sort(a, lt, gt, d++);
    sort(a, gt+1, hi, d++);
}

void print_strings(const char * strs[], int n) {
    for (int i = 0; i < n; i++)
        printf("%s\n", strs[i]);
}

int main() 
{
    const char *test1[] = { "abd", "abc", "abb", "aba" };
    sort(test1, 0, 3, 0);
    assert(strcmp(test1[0], "aba") == 0);
    assert(strcmp(test1[1], "abb") == 0);
    assert(strcmp(test1[2], "abc") == 0);
    assert(strcmp(test1[3], "abd") == 0);
    printf("sorted test1:\n");
    print_strings(test1, 4);
    printf("\n");

    const char *test2[] = { "bc", "a", "ab", "abc", "" };
    sort(test2, 0, 4, 0);
    assert(strcmp(test2[0], "") == 0);
    assert(strcmp(test2[1], "a") == 0);
    assert(strcmp(test2[2], "ab") == 0);
    assert(strcmp(test2[3], "abc") == 0);
    assert(strcmp(test2[4], "bc") == 0);
    printf("sorted test2:\n");
    print_strings(test2, 5);
    printf("\n");

    printf("all tests pass\n");
    return 0;
}
