#include <stdio.h>

// Last update: 7 of July, 2015 (3.75h)
// Author: w1ld at inbox dot ru

#define BSIZE 9999

char b[BSIZE];
int i = -1;

void flush()
{
	extern char b[BSIZE];
	extern int i;
	for(int j = 0; j < i + 1; j++)
		putchar(b[j]);

	// reset buffer:
	i = -1; 
}

void handle_eof()
{
	flush();
	exit();
}

void skip_one_line_comment()
{
	extern char b[BSIZE];
	extern int i;
	char c;
	while(1)
	{
		c = getchar();
		if(c == '\n')
		{
			// keep line breaks
			i++;
			b[i] = '\n';
			break;
		}
		else if(c == EOF)
		{
			handle_eof();
		}
	}
}

void skip_multi_line_comment()
{
	char c = -1, previousC;

	while(1)
	{
		previousC = c;
		c = getchar();
		if(previousC == '*' && c == '/')
		{
			break;
		}
		else if(c == EOF)
		{
			handle_eof();
		}
	}
}

void skip_string()
{
	char c = -1, previousC;

	while(1)
	{
		previousC = c;
		c = getchar();
		if(previousC != '\\' && c == '"')
		{
			putchar(c);
			break;
		}
		else if(c == EOF)
		{
			handle_eof();
		}
		putchar(c);
	}
}

void throw_error(int errorNumber)
{
	printf("ERROR: %d", errorNumber);
	if(errorNumber == 1)
	{
		printf("Buffer overflow");
	}
	exit();
}

void output_without_comments()
{
	extern char b[BSIZE];
	extern int i;
	char c;
	while(1)
	{
		c = getchar();

		if(c == EOF)
		{
			handle_eof();
		}

		if(i + 1 >= BSIZE)
		{
			throw_error(1); // overflow
		}
		i++;
		b[i] = c;

		if((c == '/' || c == '*'))
		{
			char previousC = -1;
			if(i > 0)
				previousC = b[i-1];

			if(previousC == '/')
			{
				i = i - 2; // remove previous char
				if(c == '/')
					skip_one_line_comment();
				else if( c == '*')
					skip_multi_line_comment();
			}
		}
		else if(c == '"')
		{
			flush();
			skip_string();
		}
		else if(c == '\n')
		{
			flush();
		}
	}
}

main()
{
	output_without_comments();
}

/* comment to
 *
 *
 *
 * test remove */

// test 1: 
/*/
 * asf
 */

// oneliner comment 

void somemethod(){}
char* s = " \" /* some comment in string */ "; // comment
char* s1 = " \" // some comment in string  "; /* comment */
char* s2 = " \" // some c \
omment in string // comment here now /* comment */  "; /* comment */

