#include <stdio.h>

#define MAXLINE 1000

int getline(char s[], int lim);

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
   int spaces = 0;
        for(int i = 0; i < len; i++)
        {
            c = line[i];

            if(spaces != -1 && c == ' ')
            {
                ++spaces;

                if(spaces == columnLength)
                {
                    putchar('\t');
                    spaces = 0;
                }
            }
            else if(spaces != -1 && c == '\t')
            {
                // keep the previous spaces
                if(spaces > 0)
                {
                    putchar('\t');
                    spaces = 0;
                }

                putchar(c);
            }
            else
            {
                // keep spaces
                if(spaces > 0)
                {
                    for(int j = 0; j < spaces; j++)
                        putchar(' ');
                }

                spaces = -1;
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

