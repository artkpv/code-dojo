/*
 * Exercise 4-2.Extend atofto handle scientific notation of the form 
 *   123.45e-6
 * where a floating-point number may be followed by eor Eand an optionally signed exponent. 
 *
 * Author: Artyom K. <w1ld at inbox dot ru>, July 2015
 *
 * NEXT: See below
 *
 */
#include <ctype.h>

#define EPSILON 0.0000001

/* atoi: convert s to integer; version 2 */
int atoi(char s[], int k)
{
	int i , n, sign;
	for (i = k; isspace(s[i]); i++) /* skip white space */
		;
	sign = (s[i] == '-') ? -1 : 1;
	if (s[i] == '+' || s[i] == '-') /* skip sign */
		i++;
		for (n = 0; isdigit(s[i]); i++)
			n = 10 * n + (s[i] - '0');
	return sign * n;
}

/* atof: convert string s to double */
double atof(char s[])
{
	double val, power;
	int i, sign;
	for (i = 0; isspace(s[i]); i++) /* skip white space */
		;
	sign = (s[i] == '-') ? -1 : 1;
	if (s[i] == '+' || s[i] == '-')
		i++;
	for (val = 0.0; isdigit(s[i]); i++)
		val = 10.0 * val + (s[i] - '0');
	if (s[i] == '.')
		i++;
	for (power = 1.0; isdigit(s[i]); i++) {
		val = 10.0 * val + (s[i] - '0');
		power *= 10;
	}

	if(s[i] == 'e' || s[i] == 'E')
	{
		int e = atoi(s, ++i);

		if(e > 0) 
			for(;e > 0;e--)
				power /= 10;
		else
			for(;e < 0;e++)
				power *= 10;

	}

	return sign * val / power;
}

void assert_atof(char s[], double d)
{
	double r = atof(s);
	if(r != d && (r-d) > EPSILON)
		printf("FAIL: atof(\"%s\") == %f != %f\n", s, r, d);
	else
		printf("SUCCESS: atof(\"%s\") == %f == %f\n", s, r, d);
}

int main(void)
{
	assert_atof("1.0e1", 10);
	assert_atof("1.1e1", 11);
	assert_atof("1.1e-1", 0.11);
	assert_atof("1.0e4", 10000);
	assert_atof("1.0e5", 100000);
	assert_atof("9.99999e5", 999999);
	// TODO. NEXT: FIX it to work with these large numbers 
	assert_atof("1.0e6", 1000000);
	assert_atof("1.0e8", 100000000);
	assert_atof("1.0e10", 10000000000);
}

