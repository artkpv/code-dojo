/*
 * Exercise 5-4. Write the function strend(s,t), which returns 1 if the string t
 * occurs at the end of the string s, and zero otherwise.
 *
 * Author: Artyom K. <w1ld at inbox dot ru>, 04.08.2015
 */

#include <assert.h>

int strend(char *s, char *t)
{
	char *s1 = s; // could concat lines?
	char *t1 = t;
	while(*s++ != '\0')
		;
	s--;
	while(*t++ != '\0')
		;
	t--;
	if(t1 == t) // unknown for 0 size
	{
		printf("(return 0 as t is empty)\n");
		return 0; 
	}

	if(s1 == s) // unknown for 0 size
	{
		printf("(return 0 as s is empty)\n");
		return 0; 
	}

	while(1)
	{
		if(*t != *s)
		{
			printf("(return 0 as chars do not match)\n");
			return 0;
		}

		if(s == s1 && t != t1)
		{
			printf("(return 0 as end of s but not end of t)\n");
			return 0;
		}
		
		if(t == t1)
		{
			printf("(end of t reached)\n");
			break;
		}

		s--;		
		t--;
	}
	return 1;
}

int main(void)
{
	//printf("'\\0' char is: '");
	//printf("0x%x", '\0');
	//printf("'\n");
	//printf("' ' char is: '");
	//printf("0x%x", ' ');
	//printf("'\n");

	assert(strend("abc", "bc") == 1);
	assert(strend("abc", "bc") == 1);
	assert(strend("abc", "ab") == 0);
	assert(strend("abc", "") == 0);
	assert(strend("abc ", "c") == 0);
	assert(strend("c ", "abc") == 0);
	assert(strend("", "abc") == 0);

	return 0;
}
