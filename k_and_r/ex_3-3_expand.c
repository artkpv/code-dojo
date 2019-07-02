/*
 * Exercise 3-3. Write a function expand(s1,s2) that expands shorthand notations
 * like a-z in the string s1 into the equivalent complete list abc...xyz in s2.
 * Allow for letters of either case and digits, and be prepared to handle cases
 * like a-b-c and a-z0-9 and -a-z. Arrange that a leading or trailing -is taken
 * literally. 
 *
 * Author : Artyom K., <w1ld at inbox dot ru>, July, 2015
 *
 * NEXT: Refactor
 */ 

#define MAXLINE 9999

int isDigit(char c)
{
	return '0' <= c && c <= '9';
}

int isUpper(char c)
{
	return 'A' <= c && c <= 'Z';
}

int isLower(char c)
{
	return 'a' <= c && c <= 'z';
}

void expand(char s1[], char s2[])
{
	int i = 0, j = 0;
	char c;
	while((c = s1[i++]) != '\0')
	{
		if(c == '-')
		{
			if((i-2) >= 0) // not beginning
			{
				char startC =  s1[i-2];
				if(isDigit(startC) || isUpper(startC) || isLower(startC))
				{
					c = s1[i++];
					if(c == '\0')
					{
						break;
					}

					if(isDigit(c) || isUpper(c) || isLower(c))
					{
						do
						{
							startC = startC + 1;
							s2[j++] = startC;
						}
						while(startC < c);
					}
					else 
					{
						s2[j++] = c;
					}
				}
				else 
				{
					s2[j++] = c;
				}

			}
			else
			{
				s2[j++] = c;
			}
		}
		else 
		{
			s2[j++] = c;
		}
	}
	s2[j++] = c;
}

int getLength(char s[])
{
	char c;
	int i = 0;
	while(1) 
	{
		if(s[i++] == '\0')
			break;
	}
	return i;
}

void assert_expand(char s1[], char s2[])
{
	char s[MAXLINE];

	expand(s1, s);

	char c ;
	int i = 0;
	while((c = s[i++]) != '\0')
	{
		char s2Char = s2[i-1];

		if(c != s2Char)
		{
			printf("FAIL: Result is '%s', expected: '%s'. Char at %d does not match.\n",
					s, s2, (i-1));
			return;
		}
	}

	int s2len = getLength(s2);
	int slen = i - 1;

	if(slen > s2len)
	{
		printf("FAIL: size does not match. Result is '%s' (%d), expected: '%s' (%d)\n",
				s, slen, s2, s2len);
		return;
	}

	printf("SUCCESS: Result is '%s', expected: '%s'.\n", s, s2);
}

int main(void)
{
	assert_expand("a-c", "abc");
	assert_expand("aa-cc", "aabcc");
	assert_expand("a-z", "abcdefghijklmnopqrstuvwxyz");
	assert_expand("A-Z", "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
	assert_expand("A-Za-z", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
	assert_expand("A-Za-z", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");

	assert_expand("0-9", "0123456789");
	assert_expand("0-9a-d", "0123456789abcd");
	assert_expand("0-9a-d", "0123456789abcd");
	assert_expand("a-b-c", "abc");
	assert_expand("a-b-d", "abcd");
	assert_expand("-a-z", "-abcdefghijklmnopqrstuvwxyz");
	assert_expand("a-z-", "abcdefghijklmnopqrstuvwxyz-");
	assert_expand("-a-z-", "-abcdefghijklmnopqrstuvwxyz-");
}
