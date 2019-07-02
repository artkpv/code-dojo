// 
// Exercise 2-1. Write a program to determine the ranges of char, short, int,
// and long variables, both signed and unsigned, by printing appropriate values
// from standard headers and by direct computation. Harder if you compute them:
// determine the ranges of the various floating-point types.
//
// Next: do computation of FLT_MIN
//
// Question at 
// http://stackoverflow.com/questions/31357258/why-float-wont-increase-at-some-point-while-computing-flt-max-by-summation/31358238#31358238
//
#include <limits.h>
#include <float.h>
#include <stdio.h>

float decrease(float a, float step)
{
	fflush(stdout);
	float t = a, original = a;
	while((t = a - step) > 0)
	{
		if(1.0f/(1.0f/t) == 0.0) break; // infinity detection
		a = t;
	}

	if(original == a)
	{
		printf(" %e was not changed with %e step \n", original, step);
		return a;
	}
	printf(" %e decreased to %e with %e step \n", original, a, step);
	return decrease(a, step * 0.01);
}

float increase(float a, float step)
{
	float t = a, original = a;
	while((t = a + step) > a)
	{
		if(1.0/t == 0.0) break; // infinity detection
		a = t;
	}

	if(original == a)
	{
		printf(" %e was not increased with %e step \n", original, step);
		if(step > 1.0) return increase(a, step / 2.0);
		return a;
	}
	printf(" %e increased to %e with %e step \n", original, a, step);
	return increase(a, step * 2.0);
}

void print_char_limits()
{
	char a, b = 0;
	while((b = a + 1) > a )
		a++;
	printf("Max (default, signed) char: %d\n", a);

	while((b = a - 1) < a)
		a--;
	printf("Min (default, signed) char: %d\n", a);

	unsigned char c, d = 0;
	while((d = c + 1) > c )
		c++;
	printf("Max (unsigned) char: %d\n", c);

	while((d = c - 1) < c)
		c--;
	printf("Min (unsigned) char: %d\n", c);
}

void main()
{
	print_char_limits();
	//print_int_limits();

	// compute:
	// increase(0.0, 10.0);
	// printf("FLT_MAX : %e \n", FLT_MAX);

	//decrease(1.0, 0.1);
	//printf("FLT_MIN : %e \n", FLT_MIN);
}

void print_int_limits()
{
	printf("\n----------------------\nPrints limits of types\n----------------------\n");
	printf("From <limits.h>:\n");
	printf("CHAR_BIT: %d\n", CHAR_BIT); //    8 bits in a char 
	printf("CHAR_MAX: %d\n", CHAR_MAX); //  UCHAR_MAX or SCHAR_MAX   maximum value of char  
	printf("CHAR_MIN: %d\n", CHAR_MIN); //  0 or SCHAR_MIN maximum value of char 
	printf("INT_MAX: %d\n", INT_MAX); //  32767 maximum value of int 
	printf("INT_MIN: %d\n", INT_MIN); //  -32767 minimum value of int 
	printf("LONG_MAX: %d\n", LONG_MAX); //  2147483647 maximum value of long 
	printf("LONG_MIN: %d\n", LONG_MIN); //  -2147483647 minimum value of long 
	printf("SCHAR_MAX: %d\n", SCHAR_MAX); // +127 maximum value of signed char 
	printf("SCHAR_MIN: %d\n", SCHAR_MIN); // -127 minimum value of signed char 
	printf("SHRT_MAX: %d\n", SHRT_MAX); //  +32767 maximum value of short 
	printf("SHRT_MIN: %d\n", SHRT_MIN); //  -32767 minimum value of short 
	printf("UCHAR_MAX: %u\n", UCHAR_MAX); // 255 maximum value of unsigned char 
	printf("UINT_MAX: %u\n", UINT_MAX); //  65535 maximum value of unsigned int 
	printf("ULONG_MAX: %u\n", ULONG_MAX); // 4294967295 maximum value of unsigned long 
	printf("USHRT_MAX: %u\n", USHRT_MAX); // 65535 maximum value of unsigned short 

	printf("---------------\nBy calculation:\n");

	//char c = 0, c2;
	//while((c2 = c + 1) > c) 
	//	c = c2;
	//printf("Max char: %d\n", c);
	//c = 0;
	//while((c2 = c - 1) < c) 
	//	c = c2;
	//printf("Min char: %d\n", c);

	//int i = 0, i2;
	//while((i2 = i + 1) > i)
	//	i = i2;
	//printf("Max int: %d\n", i);
	//i = 0;
	//while((i2 = i - 1) < i)
	//	i = i2;
	//printf("Min int: %d\n", i);

	//long l = 0, l2;
	//while((l2 = l + 1) > l)
	//	l = l2;
	//printf("Max int: %d\n", l);
	//l = 0;
	//while((l2 = l - 1) < l)
	//	l = l2;
	//printf("Min int: %d\n", l);

	//signed char sc = 0, sc2;
	//while((sc2 = sc + 1) > sc) 
	//	sc = sc2;
	//printf("Max char: %d\n", sc);
	//sc = 0;
	//while((sc2 = sc - 1) < sc) 
	//	sc = sc2;
	//printf("Min char: %d\n", sc);
}

