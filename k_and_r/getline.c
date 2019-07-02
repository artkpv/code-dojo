#include <stdio.h>

/* getline:  read a line into s, return length  */
int getline(char *s,int lim)
{
	int c, i;

	for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
		*(s++) = c;
	if (c == '\n') {
		*(s++) = c;
		++i;
	}
	*s = '\0';
	return i;
}
