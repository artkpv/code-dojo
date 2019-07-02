/*
 * Exercise 5-2.Write getfloat, the floating-point analog of getint. What type
 * does  getfloat return as its function value? 
 *
 * Last modification at 03.08.2015 Пн 18:36
 *
 * NEXT: Fix:
 * 
 * 132.44
 * (0: 132.440002)
 */

#include "getch.c"
#include <stdio.h>

#define SIZE 100

/* getfloat: get next float from input into *pn */
int getfloat(float *pn)
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
	if(c == '.') {
		c = getch();
		int n = 0;
		while(isdigit(c))
		{
			*pn = 10 * *pn + (c - '0');
			n++;
			c = getch();
		}
		while(n-- > 0)
			*pn /= 10.0;
	}

	*pn *= sign;
	if (c != EOF)
		ungetch(c);
	return c;
}

int main(void)
{
	int n, getfloat(float *);
	float array[SIZE];
	for (n = 0; n < SIZE ; n++)
	{
		int r = getfloat(&array[n]);
		if(r <= 0)
			break;

		printf("(%d: %f)\n", n, array[n]);
	}
	printf("END\n");
	return 0;
}

