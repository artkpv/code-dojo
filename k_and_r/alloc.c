// 
// 
// alloc and afree 
//
// From K&R:
//   There are two routines. The first, alloc(n), returns a pointer to n
//   consecutive character positions, which can be used by the caller of alloc for
//   storing characters. The second, afree(p), releases the storage thus acquired
//   so it can be reused later. The routines are ``rudimentary'' because the calls
//   to afree must be made in the opposite order to the calls made on alloc. That
//   is, the storage managed by alloc and afree is a stack, or last-in, first-out. 

#define ALLOCSIZE 1000000 /* size of available space */

static char allocbuf[ALLOCSIZE]; /* storage for alloc */
static char *allocp = allocbuf; /* next free position */

char *alloc(int n) /* return pointer to n characters */
{
	if (allocbuf + ALLOCSIZE - allocp >= n) { /* it fits */
		allocp += n;
		return allocp - n; /* old p */
	} else /* not enough room */
		return 0;
}

void afree(char *p) /* free storage pointed to by p */
{
	if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
		allocp = p;
}
