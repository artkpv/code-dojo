#include <stdio.h>

#define MAXLINE 1000

int getline(char s[], int lim);

/* 
 *
 * test:
 *  col1    col2    col3
 *  l1  val2    val3
 */

main()
{
    int len;
    char line[MAXLINE];
    char c;
    int charsCount;
    int columnLength = 4;

    while ((len = getline(line, MAXLINE)) > 0)
    {
        charsCount = 0;
        for(int i = 0; i < len; i++)
        {
            c = line[i];
            if(c == '\t')
            {
                int charsToNextCol = columnLength - charsCount % columnLength;

                for(int j = 0; j < charsToNextCol; j++)
                    putchar(' ');

                charsCount += charsToNextCol;
            }
            else
            {
                ++charsCount;
                putchar(c);
            }
        }

    }
}

/* getline:  read a line into s, return length  */
int getline(char s[],int lim)
{
    int c, i;

    for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

