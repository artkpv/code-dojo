/*
 * Exercise 4-13. Write a recursive version of the function reverse(s), which
 * reverses the string sin place.
 *
 * Done at 1st of Aug, 2015, <w1ld at inbox dot ru>
 */

#include <string.h>
#include <stdio.h>

void reverse_recursive(char s[], int i, int len)
{
	if(i >= len / 2)
		return;

	char tmp = s[i];
	s[i] = s[len-1-i];
	s[len-1-i] = tmp;

	reverse_recursive(s, i+1, len);
}

void reverse(char s[])
{
	reverse_recursive(s, 0, strlen(s));
}

void assert_reverse(char s[], char expected[])
{
	reverse(s);
	int sComparedToExpected = strcmp(s, expected);	
	if(sComparedToExpected == 0)
	{
		printf("SUCCESS: result: '%s', expected: '%s'\n", s, expected);
	}
	else
	{
		printf("FAILED: result: '%s', expected: '%s'\n", s, expected);
	}
}

int main(void)
{
	assert_reverse("abcde", "edcba");
	assert_reverse("", "");
	assert_reverse("aabb", "bbaa");
	assert_reverse(" aabb ", " bbaa ");
	return 0;
}
