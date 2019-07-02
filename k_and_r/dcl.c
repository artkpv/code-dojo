
// Exercise 5-18.Make dclrecover from input errors.
// Exercise 5-20. Expand dcl to handle declarations with function
// argument types, qualifiers like const, and so on. 
//
//
// NEXT here: 
//  - make it parse qualifiers like const etc.
//  - ex. 5-19

/*
Syntax:
 dcl: 		optional *'s direct-dcl
 direct-dcl	name
			(dcl)
			direct-dcl(dcl [,dcl].. )
			direct-dcl[optional size]
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "getch.c"

#define MAXTOKEN 100

enum { NAME, PARENS, BRACKETS };

void dcl(void);
void dirdcl(void);
int gettoken(void);
void argument(void);

int tokentype; /* type of last token */

char token[MAXTOKEN]; /* last token string */
char name[MAXTOKEN]; /* identifier name */
char datatype[MAXTOKEN]; /* data type = char, int, etc. */
char out[1000];
char debug[10000];

void throw_error(char *message) 
{
	printf("Failed to parse: %s.\n", message);
	printf("\nDEBUG:\n%s\n", debug);
	exit();
}

main() /* convert declaration to words */
{
	while (gettoken() != EOF) { /* 1st token on line */
		if(tokentype != NAME)
			throw_error("first token should be datatype");
		strcpy(datatype, token); /* is the datatype */
		out[0] = '\0';
		strcat(debug, "in main before dcl. token='%s'\n", token);
		dcl(); /* parse rest of line */
		if (tokentype != '\n')
			throw_error("should end with new line");
		printf("%s: %s%s\n", name, out, datatype);
	}

	printf("\nDEBUG:\n%s\n", debug);
	return 0;
}

/* dcl: parse a declarator and get next token */
void dcl(void)
{
	int ns;
	for (ns = 0; gettoken() == '*'; ) /* count *'s */
		ns++;
	strcat(debug, "in dcl before dirdcl. ns=%d token='%s'\n", ns, token);
	dirdcl();
	while (ns-- > 0)
		strcat(out, "pointer to ");
}

/* dirdcl: parse a direct declarator AND get next token */
void dirdcl(void)
{
	strcat(debug, "in dirdcl\n");
	if (tokentype == '(') { /* ( dcl ) */
		dcl();
		if (tokentype != ')')
			throw_error("missing ')'");
	} else if (tokentype == NAME) /* variable name */
		strcpy(name, token);
	else
		return; // not error as can be arguments parsing

	while (1) {
		int type = gettoken();

		if (type == PARENS) // funciton without arguments
			strcat(out, "function returning ");
		else if(type == BRACKETS) {
			strcat(out, "array");
			strcat(out, token);
			strcat(out, " of ");
		}
		else if(type == '(') { // function with arguments
			gettoken();
			if (tokentype == ')') { // no arguments
				strcat(out, "function returning ");
			} else if(tokentype == NAME) { // arguments parsing
				strcat(out, "function of (");
				argument();
				while(tokentype == ',') {
					strcat(out, "and ");
					gettoken();
					argument();
				}
				if (tokentype != ')')  // no arguments
					throw_error("invalid function declaration: missing ')'");
					
				strcat(out, ") returning ");
			}
			else
				throw_error("invalid function declaration");
		}
		else { 
			break;
		}
	}
}

void argument() 
{
	if(tokentype == NAME) { // arguments parsing
		char *name = malloc(sizeof(char)*strlen(token) + 1);
		strcpy(name, token);
		dcl();
		strcat(out, name); // type
		strcat(out, " "); // type
	}
}

int gettoken(void) /* return next token */
{
	int c, getch(void);
	void ungetch(int);
	char *p = token;
	while ((c = getch()) == ' ' || c == '\t')
		;
	if (c == '(') {
		while ((c = getch()) == ' ' || c == '\t') // skip whitespace
			;

		if (c == ')' ) {
			strcpy(token, "()");
			return tokentype = PARENS;
		} else {
			ungetch(c);
			return tokentype = '(';
		}
	} else if (c == '[') {
		for (*p++ = c; (*p++ = getch()) != ']'; )
			;
		*p = '\0';
		return tokentype = BRACKETS;
	} else if (isalpha(c)) {
		for (*p++ = c; isalnum(c = getch()); )
			*p++ = c;
		*p = '\0';
		ungetch(c);
		return tokentype = NAME;
	} else
		return tokentype = c;
}

