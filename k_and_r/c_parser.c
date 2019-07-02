#include <stdio.h>
#include "getch.c"

void skip_string_constants()
{
	char c;
	while((c = getch()) != '"' && c != EOF) {
		if(c == '\\' && (c = getch()) == '"')
			continue;
	}
}

void skip_comments()
{
	// expected that previous char was '/'
	char c = getch();

	if(c == '*') { // multiline
		while((c = getch()) != EOF && !(c == '*' && (c = getch()) == '/'))
			;
	}

	if(c == '/') { // oneline
		while((c = getch()) != '\n' && c != EOF)
			;
	}
}

void skip_preprocessor()
{
	char c;
	while((c = getch()) != '\n' && c != EOF)
		;
}

void skip_whitespace_and_preprocessor() 
{
	char c;
	int isNewLine = (((c = getch()) == '\r' && ((c = getch()) == '\n')) || c == '\n');

	while(isspace(c)) {
		c = getch();
	}

	if(c == '#') {
		while((c = getch()) != '\n' || c != EOF)
			;
		skip_whitespace_and_preprocessor();
	}
	else
		return;
}
