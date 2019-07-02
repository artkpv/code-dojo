/*
 * Exercise 2-8. Write a function rightrot(x,n) that returns the value of the
 * integer x rotated to the right by n positions. 
 *
 * Author: Artyom K., w1ld at inbox dot ru, July 2015
 */

#include <limits.h>
#include <assert.h>

int get_uint_bits()
{
	int uint_bits = 0;
	unsigned y = 1;
	while((y <<= 1) != 0) uint_bits++;
	return uint_bits;
}

unsigned rightrot(unsigned x, int n)
{
	int uint_bits = get_uint_bits();

	for(int i = 0; i < n; i++)
	{
		unsigned lastBitMoved = x << uint_bits;
		unsigned shifted = x >> 1;
		x = shifted | lastBitMoved;
	}
	return x;
}

void assert_rightrot(unsigned x, int n, unsigned expected)
{
	unsigned r = rightrot(x, n);
	if(r == expected)
	{
		printf("SUCCESS: rightrot(%x, %d) == %x == %x\n", x, n, r, expected);
	}
	else
	{
		printf("FAIL: rightrot(%x, %d) == %x != %x\n", x, n, r, expected);
	}
}

int main(void)
{
	assert_rightrot(0xf0, 4, 0xf);
	assert_rightrot(0xf, 4, 0xf0000000);
	assert_rightrot(0xff, 8, 0xff000000);
	assert_rightrot(UINT_MAX, 1, UINT_MAX); 
}
