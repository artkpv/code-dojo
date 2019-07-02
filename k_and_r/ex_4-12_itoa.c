/*
 * Exercise 4-12. Adapt the ideas of printd to write a recursive version of
 * itoa; that is, convert an integer into a string by calling a recursive
 * routine.
 *
 * Last update: July, 2015. Author: Artyom K., <w1ld at inbox dot ru> 
 *
 * NEXT: simplify recursive_itoa
 *
 */

#define MAXNUMBER 100

int recursive_itoa(int n, char s[])
{
	int next = n / 10;
	if(next > 0)
	{
		int i = recursive_itoa(next, s);
		char d = n % 10 + '0'; 
		s[i] = d;
		return i + 1;
	}
	else 
	{
		char d = n % 10 + '0'; 
		s[0] = d;
		return 1;
	}
}

void itoa(int n, char s[])
{
	int last = recursive_itoa(n, s);
	s[last] = '\0';
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

void assert_itoa(int n, char s[])
{
	char r[MAXNUMBER];
	itoa(n, r);
	if(isStrEqual(r, s))
	{
		printf("SUCCESS: result: %s; expected: %s\n", r, s);
	}
	else
	{
		printf("FAIL: result: %s; expected: %s\n", r, s);
	}
}

int main(void)
{
	assert_itoa(10, "10");
	assert_itoa(123456789, "123456789");
}
