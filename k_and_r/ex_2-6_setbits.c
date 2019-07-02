/*
 * Exercise 2-6. Write a function setbits(x,p,n,y) that returns x with the n
 * bits that begin at position p set to the rightmost n bits of  y, leaving the
 * other bits unchanged. 
 *
 * Author: Artyom K, w1ld at inbox dot ru; July 2015
 */

unsigned setbits(unsigned i, int p, int n, unsigned i2)
{
	unsigned mask = (i2 & ~(~0 << n)) << (p + 1 - n); // mask with n bits set to bits of i2 and positioned at p
	unsigned shifted = ~(~(~0 << n) << (p + 1 - n)) & i; 
	return shifted | mask;
}

void assert_setbits(unsigned i, int p, int n, unsigned i2, unsigned expected)
{
	unsigned r = setbits(i, p, n, i2);
	if(r != expected)
	{
		printf("FAIL: setbits(%x, %d, %d, %x) == %x != %x\n", i, p, n, i2, r, expected);
	}
	else
	{
		printf("SUCCESS: setbits(%x, %d, %d, %x) == %x == %x\n", i, p, n, i2, r, expected);
	}
}

int main(void)
{
	assert_setbits(0xf0, 3, 4, 0xf, 0xff);
	assert_setbits(0x33, 3, 2, 0xf, 0x3f);
	assert_setbits(0x33, 7, 4, 0xf, 0xf3);
	assert_setbits(0xf3, 7, 4, 0x3, 0x33);
}
