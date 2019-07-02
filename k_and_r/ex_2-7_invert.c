/*
 * Exercise 2-7. Write a function invert(x,p,n) that returns x with the n bits
 * that begin at position p inverted (i.e., 1 changed into 0 and vice versa),
 * leaving the others unchanged.
 *
 * Author: Artyom K., w1ld at inbox dot ru, July, 2015
 */

unsigned invert(unsigned x, int p, int n)
{
	unsigned mask = ~(~0 << n) << (p + 1 - n);
	unsigned invertedBits = ~x & mask;
	unsigned xWithoutTheBits = x & ~mask;
	//printf("(mask: %x; invert: %x; without bits: %x)\n", mask, invertedBits, xWithoutTheBits);
	return invertedBits | xWithoutTheBits;
}

void assert_invert(unsigned x, int p, int n, unsigned expected)
{
	unsigned r = invert(x, p, n);
	if(r == expected)
	{
		printf("SUCCESS: invert(%x, %i, %i) == %x == %x\n", x, p, n, r, expected);
	}
	else
	{
		printf("FAIL: invert(%x, %i, %i) == %x != %x\n", x, p, n, r, expected);
	}
}

int main(void)
{
	assert_invert(0xff, 7, 4, 0x0f);
	assert_invert(0xfcf, 7, 4, 0xf3f);
	assert_invert(0xcff, 11, 4, 0x3ff);
	assert_invert(0xfff, 11, 12, 0x0);
}
