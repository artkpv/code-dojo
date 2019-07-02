#include <stdio.h>
#define MAXLINE 1000   /* maximum input line length */

int getline(char line[], int maxline);
void copy(char to[], char from[]);
void reverse(char s[], int len);

/* print the longest input line */
main()
{
	int len;            /* current line length */
	int max;            /* maximum length seen so far */
	char line[MAXLINE];    /* current input line */
	char longest[MAXLINE]; /* longest line saved here */

	max = 0;
	while ((len = getline(line, MAXLINE)) > 0)
	{
		if (len > max) {
			max = len;
			copy(longest, line);
		}
		reverse(line, len);
		printf("%s", line);
	}
	if (max > 0)  /* there was a line */
		printf("%d: %s", max, longest);

	return 0;
}

/* getline:  read a line into s, return length  */
int getline(char s[], int lim)
{
	int c, i;

	for (i=0; (c=getchar())!=EOF && c!='\n'; ++i)
		if(i < lim-2)
			s[i] = c;

	int strEnd;
	if(i < lim-2)
	{
		strEnd = i;
		if (c == '\n') {
			s[strEnd] = c;
			++strEnd;
			++i;
		}
	}
	else
	{
		strEnd = lim-2;
	}

	s[strEnd] = '\0';
	
	return i;
}

void reverse(char s[], int len)
{
	for(int i=0; i < len / 2; i++)
	{
		char t = s[i];
		s[i] = s[len - 1 - i];
		s[len - 1 - i] = t;
	}
}

/* copy:  copy 'from' into 'to'; assume to is big enough */
void copy(char to[], char from[])
{
	int i;

	i = 0;
	while ((to[i] = from[i]) != '\0')
		++i;
}



