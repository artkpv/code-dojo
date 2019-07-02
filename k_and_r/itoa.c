#include <limits.h>
#include <string.h>

/*
 * Exercise 3-4. In a two's complement number representation, our version of
 * itoa does not handle the largest negative number, that is, the value of n
 * equal to -(2^wordsize-1). Explain why not.  Modify it to print that value
 * correctly, regardless of the machine on which it runs. 
 *
 */

/*
 * Breaks with INT_MIN because abs(INT_MIN) > INT_MAX
 *
 * Done on 2015-7-22 
 */

/* reverse: reverse string s in place */
void reverse(char s[])
{
	int c, i, j;
	for (i = 0, j = strlen(s)-1; i < j; i++, j--) {
		c = s[i];
		s[i] = s[j];
		s[j] = c;
	}
}

/* itoa: convert n to characters in s */
void itoa(int m, char s[])
{
	int i, sign;
	unsigned int n; 
	if ((sign = m) < 0) /* record sign */
		n = -m; /* make n positive */
	else
		n = m; 

	i = 0;
	do { /* generate digits in reverse order */
		s[i++] = n % 10 + '0'; /* get next digit */
	} while ((n /= 10) > 0); /* delete it */
	if (sign < 0)
		s[i++] = '-';
	s[i] = '\0';
	reverse(s);
}

int main(void)
{
	char s[1000];

	itoa(123, s);
	printf("%d : %s\n", 123, s);
	itoa(INT_MIN, s);
	printf("%d \n", INT_MAX, s);
	printf("%d : %s\n", INT_MIN, s);
}
