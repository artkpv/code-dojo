/*
 * Knuth-Morris-Pratt algorithm for substring search.
 *
 * Author: Artyom K. <w1ld [dog] inbox [dot] ru>
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define R 256

int ** ttable = NULL;

void build_machine(const char * pattern);

int nextstate(int current, char c);

int kmp(const char * text, const char * pattern)
{
    build_machine(pattern);
    
    int state = 0;
    int i; 
    int tlen = strlen(text);
    int plen = strlen(pattern);
    for (i = 0; i < tlen; ++i) {
        state = nextstate(state, text[i]);
        if (state == plen)
            return i - plen + 1;
    }
    return -1;
}

void build_machine(const char * pattern)
{
    int plen = strlen(pattern);
    if (plen == 0)
        return;
    ttable = (int**) realloc(ttable, sizeof(int*) * R);
    int i;
    for (i = 0; i < R; ++i) 
        ttable[i] = (int*) realloc(ttable[i], sizeof(int) * plen);        

    for (i = 0; i < R; ++i)
        ttable[i][0] = 0;
    ttable[pattern[0]][0] = 1;
    int state = 0;     
    int j;
    for (j = 1; j < plen; j++) {
        for (i = 0; i < R; ++i) {
            ttable[i][j] = ttable[i][state];
        }
        ttable[pattern[j]][j] = j + 1;
        state = ttable[pattern[j]][state];
    }
}

int nextstate(int current, char c)
{
    return ttable[c][current];
}

int main()
{
    assert(kmp("abcdefg", "cde") == 2);
    assert(kmp("abcdefg", "cee") == -1);
    assert(kmp("abcdefg", "g") == 6);
    assert(kmp("abcdefg", "a") == 0);
    assert(kmp("", "a") == -1);
    assert(kmp("a", "") == -1);
    assert(kmp("asdf ASLDKJA 3234 sdf !@#$% *", "!") == 22);
    assert(kmp("asdf ASLDKJA 3234 sdf !@#$% *", "5") == -1);
    printf("Done\n");
    return 0;
}
