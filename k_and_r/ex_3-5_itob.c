/*
 * Exercise 3-5. Write the function itob(n,s,b) that converts the integer n into
 * a base b character representation in the string s. In particular,
 * itob(n,s,16) formats s as a hexadecimal integer in s. 
 *
 *
 * Author: Artyom K., <w1ld at inbox dot ru>, July 2015
 *
 */

#define MAXNUMBER 1000

void reverse(char s[])
{
	int c, i, j;
	for (i = 0, j = strlen(s)-1; i < j; i++, j--) {
		c = s[i];
		s[i] = s[j];
		s[j] = c;
	}
}

void itob(int n, char s[], int b)
{
	/*
	 *
	 * n = d0*10^0 + d1*10^1 + d2*10^2 + d3*10^3 + ... 
	 * n = d0*2^0 + d1*2^1 + ... 
	 * b = 2, s = '10': 0*2^0 + 1*2^1 = 2
	 * b = 2, s = '100': 0*2^0 + 0*2^1 + 1*2^2 = 4; 4%2 = 0; 2%2 = 0; 1%2 = 1
	 *
	 */
	int i, sign;
	if ((sign = n) < 0) /* record sign */
		n = -n; /* make n positive */
	i = 0;
	do { /* generate digits in reverse order */
		int d = n % b; /* get next digit */
		char c = d + '0';
		if(c > '9')
			c = 'A' + (c - '9' - 1);
		s[i++] = c;
	} while ((n /= b) > 0); /* delete it */
	if (sign < 0)
		s[i++] = '-';
	s[i] = '\0';
	reverse(s);
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

void assert_itob(int n, int b, char expected[])
{
	char r[MAXNUMBER];
	itob(n, r, b);

	if(isStrEqual(r, expected))
		printf("SUCCESS: \"%s\" == \"%s\"\n", r, expected);
	else
		printf("FAIL: \"%s\" != \"%s\"\n", r, expected);
}

int main(void)
{
	assert_itob(1, 10, "1");
	assert_itob(15, 16, "F");
	assert_itob(15, 2, "1111");
	assert_itob(1, 2, "1");
	assert_itob(4438765, 16, "43BAED");
	assert_itob(4438765, 16, "43BAED");
	assert_itob(4438765, 8, "20735355");
	assert_itob(288, 17, "GG");
}
