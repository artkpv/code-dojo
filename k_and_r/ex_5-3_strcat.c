/* 
 * Exercise 5-3. Write a pointer version of the function strcat that we showed in
 * Chapter 2: strcat(s,t)copies the string tto the end of s.
 *
 * Last edit at 04.08.2015
 * Author: Artyom K. <w1ld at inbox dot ru>
*/

#include <string.h>

/* strcat:  concatenate t to end of s; s must be big enough */
void mystrcat(char s[], char t[])
{
	int i, j;

	i = j = 0;
	while (s[i] != '\0') /* find end of s */
		i++;
	while ((s[i++] = t[j++]) != '\0') /* copy t */
		;
}

void assert_strcat(char s[], char t[], char expected[])
{
	mystrcat(s, t);

	if(strcmp(s, expected) != 0)
		printf("FAILED: '%s' != '%s'\n", s, expected);
	else
		printf("SUCCESS: '%s' == '%s'\n", s, expected);
}

int main(void)
{
	assert_strcat("abc\0   ", "def", "abcdef");
	assert_strcat("abc", "", "abc");
	assert_strcat("123A\0 ", "B", "123AB");
	assert_strcat("\0   ", "def", "def");
}
