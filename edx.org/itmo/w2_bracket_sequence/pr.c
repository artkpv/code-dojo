#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    scanf("%d", &n);
    char opens[] = "([";
    char closes[] = ")]";
    char s[10000];
    int count = 0;
    char line[10000];
    for (int i = 0; i < n; i++){
        count = 0;
        scanf("%s", line);
        int len = strlen(line);
        int isvalid = 1;
        for (int j = 0; j < len; j++) {
            char ch = line[j];
            if (strchr(opens, ch)) {
                s[count++] = ch;
            }
            else {
                // pop and check:
                if (count > 0) {
                    char last = s[--count];
                    int close_i = strchr(closes, ch) - closes;
                    int open_i = strchr(opens, last) - opens;
                    if (close_i == open_i)
                        continue;
                }
                isvalid = 0;
            }
        }
        if (count > 0) 
            isvalid = 0;
        printf(isvalid ? "YES\n" : "NO\n");
    }
    return 0;
}