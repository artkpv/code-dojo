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
 */

#include <assert.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#define bool int
#define TRUE 1
#define FALSE 1

unsigned long
factorial(unsigned long n, unsigned long k) {
	unsigned long r = 1;
	while (k > 0 && n > 0) {
		r *= n;
		n--; k--;
	}
	return r;
}

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
	/*
	 * 1. Find first pair in asc order from left.
	 * 2. Exch them
	 * 3. Sort in asc all to right of the first 
	 */
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
permutations(int n, int k) {
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


void main() {
	assert(permutations(1, 0) == NULL);
	assert(permutations(1, 2) == NULL);

	int ** perms1_1 = permutations(1, 1);
	assert(perms1_1 != NULL);
	assert(perms1_1[0] != NULL);
	assert(perms1_1[0][0] == 1);

	int ** perms2_2 = permutations(2, 2);
	assert(perms2_2 != NULL);
	assert(perms2_2[0] != NULL);
	assert(perms2_2[0][0] == 1);
	assert(perms2_2[0][1] == 2);
	assert(perms2_2[1] != NULL);
	assert(perms2_2[1][0] == 2);
	assert(perms2_2[1][1] == 1);

	printf("\n 3-k from 3-n:\n");
	// TODO
	int ** perms3_3 = permutations(3, 3);
	for (int i = 0; i < factorial(3, 3); i++) {
		for (int j = 0; j < 3; j++) {
			printf("%d ", perms3_3[i][j]);
		}
		printf("\n");
	}
	printf("\n");

}
