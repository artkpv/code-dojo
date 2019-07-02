//
// ---------------------------------------------------------------------------
// Exercise 5-13. Write the program tail, which prints the last n lines of its
// input. By default, n is set to 10, let us say, but it can be changed by an
// optional argument so that 
//    tail -n 
// prints the last n lines. The program should
// behave rationally no matter how unreasonable the input or the value of n.
// Write the program so it makes the best use of available storage; lines should
// be stored as in the sorting program of Section 5.6, not in a two-dimensional
// array of fixed size. 
// ---------------------------------------------------------------------------
//
// Author: w1ld at inbox dot ru
// Last edit at 12.08.2015 
// ---------------------------------------------------------------------------
//
// History:
// 14.08.2015 Пт 23:45. Tried to make alloc with memory reallocation (on filling
//   it would copy to beginning everything). But points then won't work. So they
//   need to be kept separately which makes everything more difficult!
//   (Hard, reconsider)
//   Need to somehow dynamically allocate memory but not using alloc.c (stack
//   based) and malloc not to be used so far
//
// 15.08.2015 Сб 10:53. Дерьмище. Откладываю. Выводит ерунду. Следующее: проверить alloc 
//   и этоту queue
// 

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "atoi.c"
#include "getline.c"

// ALLOC modified:
//
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

void afree(char *p) /* free storage pointed to by p AND rearrange the storage */
{
	if (p >= allocbuf && p < allocbuf + ALLOCSIZE)
	{
		char *left = p;
		char *right = p;
		while(*right++ != '\0') // skip freed
			;

		while(right < allocp) {
			*left++ = *right++;
		}
		allocp = right;
	}
}


#define MAXLINES 5000 /* max #lines to be sorted */
#define DEFAULT 10

/*
 * Dropping queue: removes the very first if no size. Array based. FIFO. 
 *
 * 1. No elements:
 *  | f,l | | | | | | |
 * 2. One element at l:
 *  | l | f | | | | | | 
 * 3. Before overfill:
 *  | l | | | | | | f | 
 * 4. Overfilled:
 *  | f | l | | | | | | 
 * 5. Before overfill for last:
 *  | | | | | | f | l | 
 * 6. After overfill for last = (3):
 *  | l | | | | | | f | 
 */

char *queue[MAXLINES]; /* pointers to text lines */
int first = 0;
int last = 0;
int count = 0;

void enqueue(char *s)
{
	int len = 0;

	char *sForLen = s;
	while(*sForLen++ != '\0') len++;

	char *p = alloc(len + 1);
	if(p == NULL)
		exit();

	strcpy(p, s);
	queue[first] = p;

	if(MAXLINES <= first + 1)  // overfilled
		first = 0;
	else  // there is space or removes last
		first++;

	int isToDropLast = (first == last);
	if(isToDropLast) {
		if(MAXLINES <= last + 1) // if loops
			last = 0;
		else
			last++;
		count--;
	}

	count++;
}

// returns and removes last element or &void if no elements
char *dequeue() { 
	if(count == 0)
		return NULL;
	else {
		char *s = queue[last];

		afree(s);

		if(last + 1 >= MAXLINES) { // loop
			last = 0;
		}
		else {
			last++;
		}

		count--;
		return s;
	}
}

void assert_queue()
{
	// fully fill
	for(int i = 0; i < MAXLINES; i++)
	{
		enqueue("1");
	}
	enqueue("One more");
//	printf("(queue: first = %d, last = %d)\n", first, last);
	assert(first == 1);
	assert(last == 2);

	for(int i = 0; i < MAXLINES - 1; i++)
	{
		enqueue("1");
	}
	assert(first == 0);
	assert(last == 1);
	enqueue("One more");
	assert(first == 1);
	assert(last == 2);
}

void print_queue() {
	int n = 1;
	int i = last;
	while(i != first) {
		printf("%d: %s\n", n++, queue[i]);

		if(i == MAXLINES -1)
			i = 0;
		else
			i++;
	}
}

#define MAXLEN 1000 /* max length of any input line */

int getline(char *, int);

/* sort input lines */
int main(int argc, char *argv[])
{
	//assert_queue();

	// init args:
	int tail = DEFAULT;
	while(argc-- > 1) {
		argv++;
		if((*argv)[0] == '-') {
			tail = atoi(++(*argv));
			if(tail < 0) {
				tail = DEFAULT;
			}
		}
	}

	assert(tail > 0); // todo add upper border
	assert(tail <= MAXLINES);

	int len;
	char line[MAXLEN];
	while ((len = getline(line, MAXLEN)) > 0) {
		enqueue(line, len);
		if(count > tail)
			dequeue(); // TODO handle memory leaks as no afree?
	}

	//print_queue();
	//printf("(asserting %d count, %d tail)\n", count, tail);
	assert(count <= tail);
	for(int i = 0; i < tail; i++) {
		printf(dequeue());
	}
}

// For test:
//
// 0 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz 
// 1 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz 
// 2 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 3 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 4 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 5 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 6 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 7 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 8 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 9 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
// 10 abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz abcdefghigklmopqrstuvwxyz
