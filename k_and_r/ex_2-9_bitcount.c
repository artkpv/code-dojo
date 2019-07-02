/*
 * Exercise 2-9. In a two's complement number system, x &= (x-1) deletes the
 * rightmost 1-bit in x. Explain why. Use this observation to write a faster
 * version of bitcount.
 *
 * Author: Artyom K., w1ld at inbox dot ru, July, 2015.
 */

/*
 * Discussion at http://stackoverflow.com/questions/17238457/bitwise-operations-confused-with-expression-used-in-the-c-programming-language/17238557#17238557
 *
 */
/* bitcount: count 1 bits in x */
int bitcount(unsigned x)
{
	int b;
	for (b = 0; x != 0; x &= (x-1))
		b++;
	return b;
}

void assert_bitcount(unsigned x, int expected)
{
	int r = bitcount(x);
	if(r == expected)
		printf("SUCCESS: bitcount(%u) == %d == %d\n", x, r, expected);
	else
		printf("FAIL: bitcount(%u) == %d != %d\n", x, r, expected);
}

int main(void)
{
	assert_bitcount(0xf, 4);
	assert_bitcount(0xffff, 16);
}
