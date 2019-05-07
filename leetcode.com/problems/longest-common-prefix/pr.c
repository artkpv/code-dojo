/*
aaaaab
aaaab
aaaaab
... 


 */
char * longestCommonPrefix(char ** strs, int strsSize){
    static char * empty = "";
    if (strsSize == 0)
        return empty;
    if (strsSize == 1)
        return strs[0];
    int i = 0;
    while (i >= 0) {
        bool are_same = true;
        for (int j = 1; j < strsSize; j++) {
            char * a = strs[j-1];
            char * b = strs[j];
            are_same = i < strlen(a) 
                       && i < strlen(b)
                       && a[i] == b[i];
            if (!are_same) {
                break;
            }
        }
        if (!are_same) {
            i -= 1;
            break;
        }
        i++;
    }
    char * prefix = strs[0];
    prefix[i+1] = '\0';
    return prefix;
}

