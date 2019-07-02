/*
 *
 * Exercise 4-1. Write the function strindex(s,t) which returns the position of
 * the rightmost occurrence of tin  s, or  -1if there is none.
 *
 * Done on 27 of July, 2015
 */
#include <stdio.h>

#define MAXLINE 1000 /* maximum input line length */

void assert_strindex(char s[], char t[], int expected)
{
	int r = strindex(s, t);
	if(r != expected) printf("FAIL: strindex('%s', '%s') == %d != %d expected\n", s, t, r, expected);
	else printf("SUCCESS: strindex('%s', '%s') == %d == %d expected\n", s, t, r, expected);

}

main()
{
	// assert strlen works:
	if(strlen("123" "\0" "123") != 3 || strlen("") != 0)
	{
		printf("strlen does not work\n");
		exit();
	}

	assert_strindex("aba", "a", 2);
	assert_strindex("aba", "c", -1);
	assert_strindex("ababa", "b", 3);
	assert_strindex("", "b", -1);
	assert_strindex("abc", "", -1);
}


/* strindex: return index of t in s, -1 if none */
int strindex(char s[], char t[])
{
	int i, j, k;

	if(strlen(t) == 0)
		return -1;

	for (i = strlen(s) - 1; i >= 0; i--) 
	{
		for (j=i, k = strlen(t) - 1; k >= 0 && s[j] == t[k]; j--, k--) 
			;
		if (k == -1 && s[j+1] == t[k+1])
			return j+1;
	}
	return -1;
}
