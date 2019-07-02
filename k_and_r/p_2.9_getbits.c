/* getbits: get n bits from position p */
unsigned getbits(unsigned x, int p, int n)
{
	return (x >> (p+1-n)) & ~(~0 << n);
}

int main(void)
{
	printf("getbits(%u): %u", 0xff, getbits(0xff, 4, 4)); 
}
