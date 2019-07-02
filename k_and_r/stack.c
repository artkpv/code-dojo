/*
 * STACK
 * =====
 */

#define MAXVAL 100 /* maximum depth of val stack */
static int sp = 0; /* next free stack position */
static double val[MAXVAL]; /* value stack */

/* push: push f onto value stack */
void push(double f)
{
	if (sp < MAXVAL)
		val[sp++] = f;
	else
		printf("error: stack full, can't push %g\n", f);
}

/* pop: pop and return top value from stack */
double pop(void)
{
	if (sp > 0)
		return val[--sp];
	else {
		printf("error: stack empty\n");
		return 0.0;
	}
}

double peep(void)
{
	if (sp > 0)
		return val[(sp-1)];
	else {
		printf("error: stack empty\n");
		return 0.0;
	}
}

void sprint(void)
{
	printf("Stack: ");
	int i;
	for(i = 0; i < sp; i++)
	{
		printf("%f, ", val[i]);
	}
	printf("\n");
}

void assert_stack(void)
{
	// peeping:
	double expected = 1.1;
	push(expected);
	double actual = peep();
	printf("Peep test: ");
	if(expected != actual)
	{
		printf("FAIL\n");
	}
	else
	{
		printf("SUCCESS\n");
	}
	pop();

	// duplicating
	// expected = 1.2;
	// push(expected);
	// duplicate();

}

