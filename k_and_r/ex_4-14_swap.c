/*
 * Exercise 4-14. Define a macro swap(t,x,y) that interchanges two arguments of
 * type t. (Block structure will help.)
 */

#include <assert.h>

#define swap(t,x,y) \
{\
	t z = x;\
	x = y;\
	y = z;\
}


int main(void)
{
	int i1, i2;

	i1 = 0; i2 = 1;
	swap(int, i1, i2);
	assert(i1 == 1);
	printf("DONE");
}
