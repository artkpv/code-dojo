/*
 * Exercise 3-2. Write a function escape(s,t) that converts characters like
 * newline and tab into visible escape sequences like '\n' and '\t' as it copies the
 * string t to s. Use a switch. Write a function for the other direction as
 * well, converting escape sequences into the real characters. 
 *
 * Author : Artyom K. <w1ld at inbox dot ru>, July, 2015
 *
 * NEXT: fix bug when while unescaping it does not unescape '\n' sometime
 *
 */

#include <assert.h.>
#include <stdio.h>

#define MAXLINE 9999

void escape(char s[], char t[])
{
	char c;
	int i = 0, j = 0;
	while((c = s[i++]) != '\0')
	{
		switch(c)
		{
//			case ' ':
//				t[j++] = '-';
//				break;
			case '\t':
				assert(i + 2 < MAXLINE);
				t[j++] = '\\';
				t[j++] = 't';
				break;
			case '\n':
				assert(i + 2 < MAXLINE);
				t[j++] = '\\';
				t[j++] = 'n';
				break;
			case '\r':
				assert(i + 2 < MAXLINE);
				t[j++] = '\\';
				t[j++] = 'r';
				break;
			default:
				t[j++] = c;
				break;
		}
	}
	t[j++] = '\0';
}

void escape_stdin()
{
	char c;
	char s[MAXLINE], t[MAXLINE];
	int i = 0;
	while((c = getchar()) != EOF)
	{
		s[i++] = c;
		if(c == '\n')
		{
			// escape and flush
			s[i++] = '\0';
			escape(s, t);
			printf(t);
			i = 0;
		}
	}
}

int isQuotes(char c) 
{
	return c == '"' || c == '\'';
}
void unescape(char s[], char t[])
{
	int i = 0, j = 0; 
	char c;

	// loop
	//   take next char from s
	while((c = s[i++]) != '\0')
	{
		if(isQuotes(c))
		{
			do
			{
				t[j++] = '1';
				t[j++] = c;

				if(c == '\\') // escape in string or char
				{
					c = s[i++];
					t[j++] = '2';
					t[j++] = c;
				}

				c = s[i++];
			} while(c != '\0' && !isQuotes(c));
			t[j++] = '3'; // TODO: NEXT here . WHY it prints 3 then 1!?
			t[j++] = c;
//			if(c == '\0') break; // TODO refactor to methods as this is bad to break here.
		}
		else if(c == '\\') 
		{
	//   if char is \\
	//     read next char from s
	//     if second char is escape
	//       put the escaped char into t
	//     else
	//       put \ and another char into t

			char c1 = s[i++];	
			switch(c1)
			{
				case 'n':
					t[j++] = '\n'; 
					break;
				case 'r':
					t[j++] = '\r'; 
					break;
				case 't':
					t[j++] = '\t';
					break;
				default:
					t[j++] = c;
					t[j++] = c1;
					break;
			}
		}
		else 		
		{
			t[j++] = c;
		}
	}
	t[j++] = '\0';
}

void unescape_stdin()
{
	char c;
	char s[MAXLINE], t[MAXLINE];
	int i = 0;
	
	// fill s till '\n' then unescape and flush
	while((c = getchar()) != EOF)
	{
		s[i++] = c;
		if(i >= 1 && s[i-2] == '\\' && s[i-1] == 'n')
		{
			s[i++] = '\0';
			unescape(s, t);
			printf(t);
			i = 0;
		}
	}
}

int main(int argc, char *argv[])
{
	int isEscape = -1;
	if(argc == 2)
	{
		char firstArgChar = argv[1][0];
		if(firstArgChar == 'e')
		{
			isEscape = 1;
		}
		else if(firstArgChar == 'u')
		{
			isEscape = 0;
		}
	}

	if(isEscape == -1)
	{
		printf("Usage:\n  ex_3-2_escape [escape|unescape]\n");
		return 0;
	}

	if(isEscape)	escape_stdin();
	else 			unescape_stdin();
	return 0;
}
