/* 
 * Exercise 5-10. Write the program expr, which evaluates a reverse Polish
 * expression from the command line, where each operator or operand is a separate
 * argument. For example, 
 *   expr 2 3 4 + *
 * evaluates 2 * (3+4).
 *
 */
#include "stack.c"
#include <ctype.h>
#include <stdlib.h> /* for atof() */
#include <stdio.h>

#define NUMBER '0'
#define MAXOP 100

/* getop: get next character or numeric operand */
int gettype(char *s)
{
	if (!isdigit(*s) && *s != '.')
		return *s; /* not a number */

	if (isdigit(*s)) /* collect integer part */
		while (isdigit(*s++))
			;

	if (*s == '.') /* collect fraction part */
		while (isdigit(*s++))
			;
	return NUMBER;
}

void calc(int *argc, char *argv[])
{
	int type;
	double op2;

	int divided, divisor;
	while (*argc > 0) {
		char *s = *(argv++);
		(*argc)--;
		type = gettype(s);
		//printf(" (type = %c; arg='%s'; ", type, s);
		//sprint();
		//printf(") \n");

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
			default:
				printf("error: unknown command %s\n", s);
				break;
		}
	}
	printf("\t%.8g\n", pop());
}

int main(int argc, char *argv[])
{
	if(argc == 1)
	{
		printf("usage: ex_5-10_expr [expression]");
		return 0;
	}
	argv++; // skip first
	argc--;
	calc(&argc, argv);
	return 0;
}

