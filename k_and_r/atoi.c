
#include <assert.h>
#include <ctype.h>

/* atoi: convert s to integer; version 2 */
int atoi(char *s)
{
	int sign;
	while(isspace(*s)) { /* skip white space */
		//printf(" (atoi: space skipped) ");	
		s++;
	}

	sign = (*s == '-') ? -1 : 1;
	if (*s == '+' || *s == '-') { /* skip sign */
		//printf(" (atoi: sign skipped) ");	
		s++;
	}
		
	int n = 0;
	while (isdigit(*s)) {
		n = 10 * n + *s - '0';
		//printf(" (atoi: digit added (%d) ) ", n);	
		s++;
	}
	return sign * n;
}

void assert_atoi()
{
	assert(atoi("   123") == 123);
	assert(atoi("  -123") == -123);
	assert(atoi("123") == 123);
	assert(atoi("123 ") == 123);
	assert(atoi("") == 0);
}
