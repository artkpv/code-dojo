#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
    char arg1 = *(const char*)a;
    char arg2 = *(const char*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int isgood(char * p, int n) {
    int opens = 0;
    for (int i = 0; i < n; i++) {
        if (p[i] == '(')
            opens++;
        else if(opens > 0)
            opens--;
        else
            return 0;
    }
    return opens == 0 ? 1 : 0;
}

int nextpermutation(char * p, int n) {
    int i = n - 2;
    int closes = 0;
    while (0 <= i) {
        if (p[i] < p[i+1]) {
            char t = p[i];
            p[i] = p[i+1];
            p[i+1] = t;
            qsort((p+i+1), n-i-1, sizeof(char), compare);
            if (isgood(p, n))
                return 1;
            i = n - 2;
        }
        i--;
    }
    return 0;
    
}

#define MAX_LEN 2049
int _array[MAX_LEN];
int count = 0;

void generate(int length, int p, int i, int opens) {
    // printf("%s %d %d\n", "print_seq", i, opens);
    if (i == length) { // found next one
        if (opens != 0) // invalid
            return;
        _array[count] = p;
        return;
    }
    if (length / 2 < opens) { // can not close then
        return;
    }
    // 1) open
    p &= 1 << (length - i + 1);
    generate(length, p, i+1, opens+1);
    if (opens > 0) {
        // 2) close
        p &= 0 << (length - i + 1);
        generate(length, p, i+1, opens-1);
    }
    return;
}

int main() {
    int n;
    scanf("%d", &n);
    int p = 0;
    generate(n*2, p, 0, 0);
    qsort(_array, count, sizeof(char), compare);
    for (int i = 0; i < count; i++) {
        int p = _array[i];
        printf("%d", p);
        for (int j = 0; j < n; j++) {
            if ((p & (1 << (n-j+1)))== 1)
                putc('(', stdout);
            else
                putc(')', stdout);
        }
        putc('\n', stdout);
    }
    return 0;

    // for (int i = 0; i < n; i++) {
    //     p[i] = '(';
    //     p[2*n-i-1] = ')';
    // }
    // do {
    //     char * nullterm = p + '\0';
    //     printf("%s\n", nullterm);
    // } while(nextpermutation(p, 2*n) == 1);
}
