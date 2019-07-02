/*
 * Exercise 3-1. Our binary search makes two tests inside the loop, when one would suffice (at
the price of more tests outside.) Write a version with only one test inside the loop and measure
the difference in run-time. 
 *
 * NEXT: Find out how to make one check.
 */
#include <limits.h>

/* binsearch: find x in v[0] <= v[1] <= ... <= v[n-1] */
int binsearch(int x, int v[], int n)
{
	int low, high, mid;
	low = 0;
	high = n - 1;
	while (low <= high) {
		mid = (low+high)/2;
		if (x < v[mid])
			high = mid + 1;
		else if (x > v[mid])
			low = mid + 1;
		else /* found match */
			return mid;
	}
	return -1; /* no match */
}

#define SIZE 222222

//  Why it falls with stackoverflow when SIZE is 1000000? Run out of stack space. See
//  http://stackoverflow.com/questions/2836033/suggestion-for-chkstk-asm-stackoverflow-exception-in-c-with-visual-studio-2010#2839053

int main(void)
{
	int count = SIZE;
	int v[SIZE];

	for(int i = 0; i < count; i++)
		v[i] = i;

	int x = count / 4;
	printf("Finding %d in array of %d size\n", x, count);	
	int r = binsearch(x, v, count);
	printf("Found at %d\n", r);
	return 0;
}
