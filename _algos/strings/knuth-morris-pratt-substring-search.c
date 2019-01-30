#include <stdio.h>
#include <assert.h>
#include <string.h>

int charat(char c, int R) {
    int inx = c - 'A';
    assert(0 <= inx && inx < R);
    return inx;
}


// KMP search on A-Z chars.
int kmp_search(const char * pattern, const char * txt){
    if (!pattern || !txt) 
        return -1;
    int m = strlen(pattern);
    int n = strlen(txt);
    if (n == 0 || m == 0)
        return -1;

    int R = 'Z' - 'A' + 1;
    // Construct DFA:
    int dfa[R][m];
    {
        for(size_t i = 0; i < R; i++)
            dfa[i][0] = 0;
        dfa[charat(pattern[0], R)][0] = 1;
        int state = 0;
        for(size_t i = 1; i < m; i++)
        {
            for(size_t ii = 0; ii < R; ii++)
            {
                dfa[ii][i] = dfa[ii][state];
            }
            dfa[charat(pattern[i], R)][i] = i + 1;
            state = dfa[charat(pattern[i], R)][state];
        }
    }

    // Simulate DFA:
    size_t j = 0, i = 0;
    for (; i < n && j < m; i++)
        j = dfa[charat(txt[i], R)][j];
    if (j == m) return i - m;
    else        return -1;
}

int main() { 
    printf("Start\n");
    assert(kmp_search("A", "A") == 0);
    printf(" test 1 done\n");
    assert(kmp_search("A", "B") == -1);
    printf(" test 2 done\n");
    assert(kmp_search("A", "") == -1);
    printf(" test 3 done\n");
    assert(kmp_search("", "") == -1);
    printf(" test 4 done\n");
    assert(kmp_search("ABACA", "ABABABABACA") == 6);
    printf(" test 5 done\n");
    assert(kmp_search("AAAB", "AABAABAABAABAAAB") == 12);
    printf(" test 6 done\n");
    printf("Done\n");
}