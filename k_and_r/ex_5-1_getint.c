/*
 * Exercise 5-1. As written, getint treats a + or - not followed by a digit as a
 * valid representation of zero. Fix it to push such a character back on the
 * input. 
 *
 * Done on 2 of Aug, 2015
 */
#include <ctype.h>
#include <assert.h>
#include <stdio.h>
#include "getch.c"

#define SIZE 100

/* getint: get next integer from input into *pn */
int getint(int *pn)
{
	int c, sign;
	while (isspace(c = getch())) /* skip white space */
		;
	if (!isdigit(c) && c != EOF && c != '+' && c != '-') {
		ungetch(c); /* it is not a number */
		return 0;
	}
	sign = (c == '-') ? -1 : 1;
	if (c == '+' || c == '-')
	{
		c = getch();
		if(!isdigit(c))
		{
			ungetch(c);
			return 0;
		}
	}
	for (*pn = 0; isdigit(c); c = getch())
		*pn = 10 * *pn + (c - '0');
	*pn *= sign;
	if (c != EOF)
		ungetch(c);
	return c;
}

int main(void)
{
	int n, array[SIZE], getint(int *);
	for (n = 0; n < SIZE ; n++)
	{
		int r = getint(&array[n]);
		if(r <= 0)
			break;

		printf("(%d: %d)\n", n, array[n]);
	}
	printf("END\n");
	return 0;
}


