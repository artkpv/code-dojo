/*
 *
 * Exercise 3-6. Write a version of itoa that accepts three arguments instead of
 * two. The third argument is a minimum field width; the converted number must
 * be padded with blanks on the left if necessary to make it wide enough.
 *
 *
 * Author: done on 27 of July
 */

#define MAXOUT 1000

void reverse(char s[])
{
	int c, i, j;
	for (i = 0, j = strlen(s)-1; i < j; i++, j--) {
		c = s[i];
		s[i] = s[j];
		s[j] = c;
	}
}

void itoa(int n, char s[], int p)
{
	int i, sign;
	if ((sign = n) < 0) /* record sign */
		n = -n; /* make n positive */
	i = 0;
	do { /* generate digits in reverse order */
		s[i++] = n % 10 + '0'; /* get next digit */
	} while ((n /= 10) > 0); /* delete it */
	if (sign < 0)
		s[i++] = '-';

	while(i < p)
		s[i++] = ' ';

	s[i] = '\0';
	reverse(s);
}

void assert_itoa(int n, int p, char expected[])
{
	char s[MAXOUT];

	itoa(n, s, p);
	if(isStrEqual(s, expected))
	{
		printf("SUCCESS: '%s' == '%s'; with %d and %d padding\n", s, expected, n, p);
	}
	else
	{
		printf("FAIL: '%s' != '%s'; with %d and %d padding\n", s, expected, n, p);
	}
}

int isStrEqual(char s1[], char s2[])
{
	if(strlen(s1) != strlen(s2))
	{
		printf(" (size not the same) " );
		return 0;
	}

	int i = 0, j = 0;
	while(1)
	{
		char c1 = s1[i++];
		char c2 = s2[j++];
		if(c1 != c2)
		{
			printf(" (char '%c' at %d does not match char '%c' at %d) ", c1, i, c2, j);
			return 0;
		}
		if(c1 == '\0')
			break;
	}
	return 1;
}

int main(void)
{
	assert_itoa(123, 6, "   123");
	assert_itoa(123, 2, "123");
	assert_itoa(-123, 6, "  -123");
	assert_itoa(0, 6, "     0");
	return 0;
}
