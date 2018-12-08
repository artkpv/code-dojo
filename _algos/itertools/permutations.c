/*
 * Produces permutations in lexocographical order.
 *
 * 1 2
 * 2 1 
 *
 * 1 2 3
 * 1 3 2 
 * 2 1 3
 * 2 3 1 
 * 3 1 2
 * 3 2 1 
 *
 * NEXT: change to use factorial positioning system:
 * 0 0000 1234
 * 1 0010 1243
 * 2 0100 1324
 * 3 0110 1342
 * etc.
 *
 *
 * See
 * - Python itertools
 *   https://github.com/python/cpython/blob/9718b59ee5f2416cdb8116ea5837b062faf0d9f8/Modules/itertoolsmodule.c#L3226
 */

#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#define bool int
#define TRUE 1
#define FALSE 0

unsigned long
factorial(unsigned long n, unsigned long k) {
	unsigned long r = 1;
	while (k > 0 && n > 0) {
		r *= n;
		n--; k--;
	}
	return r;
}


// Increment kfactorial
// Example: n=4 k=3 kfactorial=311 Result: 320
bool
inc_kfactorial(int * kfactorial, int n, int k) {
	int i = k-1;  // where to start incrementing
	int a = 1;    // number to add to kfactorial
	while (i >= 0 || a <= 0) {
		assert(kfactorial[i] <= n-1-i); // max value here
		int max = n-1-i;
		if (kfactorial[i] + a <= max) {
			kfactorial[i] += a;
			return TRUE;
		}
		else {
			int b = max - kfactorial[i];
			kfactorial[i] = 0;
			a -= b;
		}
		i--;
	}
	return (a <= 0 ? TRUE : FALSE);
}

void 
convert_kfactorial_to_perms(int * kfactorial, int * perms, int n, int k) {
	// kfactorial - is factorial based digit describing a permutation
	// example:
	// kfact  permutation
	// 0000   1234  a[0]==0 : least in 1,2,3,4 = 1; a[1]==0: least in 2,3,4, ..
	// 0010   1243  .. a[2]==1 : second to last in 3,4 = 4; .. 
	// 0100   1324
	// 0110   1342
	// .. 

	// possible digits set, example:
	// 4 3 2 1
	// 0 1 0 1   -- mask, 1,3 chosen, right aligned
	int digits = 0; 
	for (int i = 1; i <= n; i++) { 
		digits <<= 1;
		digits |= 1;
	}

	for (int i = 0; i < k; i++) {
		// a - digit to put here
		// b - num of digits less than a
		// digits - remaining set of possible digits 
		int b = kfactorial[i];

		// determine a:
		int a = 0;
		int t = digits;
		int ones_skipped = 0;
		while (ones_skipped < b + 1) {
			if (t & 1 == 1)
				ones_skipped++;
			a++;
			t >>= 1;
		}
		digits = digits & (~(1<<(a-1)));
		perms[i] = a;
	}
}

int **
permutations(int n, int k) {
	// assert (n == k); // BUG. CAN NOT. TODO

	if (k == 0) return NULL;
	if (n < k) return NULL;
	unsigned long m = factorial(n, k);
	assert(m < INT_MAX);
	int ** perms = calloc(m, sizeof(int*));

	int kfactorial[k]; // in factorial system
	for (int i = 0; i < k; i++)
		kfactorial[i] = 0;

	int i = 0;
	do {
		perms[i] = calloc(k, sizeof(int));
		convert_kfactorial_to_perms(kfactorial, perms[i], n, k);
		i++;

	} while (inc_kfactorial(kfactorial, n, k) == TRUE);
	return perms;
}

void
free_permutation(int ** p, int n, int k) {
	for (int i = 0; i < n; i++)
		free(p[i]);
	free(p);
}

void 
print_permutation(int ** p, int n, int k) {
	printf("permutation %d n, %d k:\n", n, k);
	for (int i = 0; i < factorial(n, k); i++) {
		printf("%d:", i+1);
		for (int j = 0; j < k; j++) {
			printf(" %d", p[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}



void main() {
	printf("perm 1 0\n");
	assert(permutations(1, 0) == NULL);
	printf("perm 1 2\n");
	assert(permutations(1, 2) == NULL);

	{
		printf("perm 1 1\n");
		int ** p = permutations(1, 1);
		assert(p != NULL);
		assert(p[0] != NULL);
		assert(p[0][0] == 1);
		free_permutation(p, 1, 1);
	}

	{ 
		printf("perm 2 2\n");
		int ** p = permutations(2, 2);
		assert(p != NULL);
		assert(p[0] != NULL);
		assert(p[0][0] == 1);
		assert(p[0][1] == 2);
		assert(p[1] != NULL);
		assert(p[1][0] == 2);
		assert(p[1][1] == 1);
		free_permutation(p, 2, 2);
	}

	{
		printf("perm 3 3\n");
		int ** p = permutations(3, 3);
		free_permutation(p, 3, 3);
	}

	{
		int ** p = permutations(5, 4);
		assert(p != NULL);
		assert(p[0] != NULL);
		assert(p[46] != NULL);
		assert(p[46][0] == 2);
		assert(p[46][1] == 5);
		assert(p[46][2] == 4);
		assert(p[46][3] == 1);
		print_permutation(p, 5, 4);
		free_permutation(p, 5, 4);
	}
}



/*  
 
void 
_exch(int* a, int i, int j) {
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
}

void
_sort_suffix(int * a, int lo, int hi) {
	assert(lo <= hi);
	if (lo == hi) return;
	// a[lo+1] > a[lo+2] > .. > a[hi]
	// a[lo] - undefined
	for (int i = 0; i < (hi - lo + 1 + 1) / 2; i++) {
		_exch(a, lo + 1 + i, hi - i);
	}
	int i = lo;
	while (i < hi && a[i] > a[i+1]) {
		_exch(a, i, i+1);
		i++;
	}
}

bool
next_permutation(int n, int k, int* a) {
	 //  1. Find first pair in asc order from left.
	 //  2. Exch them
	 //  3. Sort in asc all to right of the first 
	assert(n >= k);
	if (k == 0) return FALSE;
	if (n < k) return FALSE;
	int i = k-2;
	while (i >= 0) {
		if (a[i] < a[i+1]) {
			_exch(a, i, i+1);
			_sort_suffix(a, i+1, k-1);
			return TRUE;
		}
	}
	return FALSE;
}


// k-permutations on n-element set 
// returns (n-k)! k-sets of indecies
int **
permutationsx(int n, int k) {
	if (k == 0) return NULL;
	if (n < k) return NULL;
	unsigned long m = factorial(n, k);
	assert(m < INT_MAX);
	int ** perms = calloc(m, sizeof(int*));
	perms[0] = calloc(k, sizeof(int));
	for (int j = 1; j <= k; j++) 
		perms[0][j-1] = j;
	for (int i = 1; i < m; i++) {
		perms[i] = calloc(k, sizeof(int));
		for (int j = 0; j < k; j++) 
			perms[i][j] = perms[i-1][j];
		next_permutation(n, k, perms[i]);
	}
	return perms;
}
*/
