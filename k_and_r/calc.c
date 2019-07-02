/*
 * Exercise 4-3. Given the basic framework, it's straightforward to extend the
 * calculator. Add the modulus (%) operator and provisions for negative numbers.
 *
 * Exercise 4-4. Add the commands to print the top elements of the stack without
 * popping, to duplicate it, and to swap the top two elements. Add a command to
 * clear the stack.
 *
 */
#include <stdio.h>
#include <stdlib.h> /* for atof() */
#include "stack.c"
#include "getch.c"

#define MAXOP 100 /* max size of operand or operator */
#define NUMBER '0' /* signal that a number was found */

int getop(char []);
extern void push(double);
extern double pop(void);
extern void assert_stack(void);
extern void sprint(void);

void calc()
{
	int type;
	double op2;
	char s[MAXOP];
	int divided, divisor;
	while ((type = getop(s)) != EOF) {
		switch (type) {
			case NUMBER:
				push(atof(s));
				break;
			case '+':
				push(pop() + pop());
				break;
			case '*':
				push(pop() * pop());
				break;
			case '-':
				op2 = pop();
				push(pop() - op2);
				break;
			case '/':
				op2 = pop();
				if (op2 != 0.0)
					push(pop() / op2);
				else
					printf("error: zero divisor\n");
				break;
			case '%':
				divisor = pop();
				divided = pop();
				push((divided % divisor));
				break;
			case '\n':
				printf("\t%.8g\n", pop());
				break;
			default:
				printf("error: unknown command %s\n", s);
				break;
		}
	}
}

// Getop
// ====
#include <ctype.h>
extern int getch(void);
extern void ungetch(int);

/* getop: get next character or numeric operand */
int getop(char s[])
{
	int i, c;
	while ((s[0] = c = getch()) == ' ' || c == '\t')
		;
	s[1] = '\0';
	if (!isdigit(c) && c != '.')
		return c; /* not a number */
	i = 0;
	if (isdigit(c)) /* collect integer part */
		while (isdigit(s[++i] = c = getch()))
			;
	if (c == '.') /* collect fraction part */
		while (isdigit(s[++i] = c = getch()))
			;
	s[i] = '\0';
	if (c != EOF)
		ungetch(c);
	return NUMBER;
}

/* reverse Polish calculator */
int main(void)
{
	assert_stack();
	calc();
	return 0;
}
