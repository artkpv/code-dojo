/*
 * 
 * Radix sort, MSD - Most Significant Digit first (left to right)
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int charat(char * s, int i) {
	int len = strlen(s);
	if (i < len)
		return (int)s[i];
	return -1;
}

void _rsort(char ** a, int lo, int hi, int digit, int radix, char ** aux) {
	int count[radix+2]; // extra for -1 and index
	if (lo >= hi) return;
	for (int i = 0; i < radix+2; i++)
		count[i] = 0;
	for (int i = lo; i <= hi; i++)
		count[charat(a[i], digit)+2]++; // extra for -1 
	for (int i = 1; i < radix+1; i++)
		count[i] += count[i-1];
	for (int i = lo; i <= hi; i++) {
		int c = charat(a[i], digit)+1;
		aux[lo+count[c]] = a[i];
		count[c]++;
	}
	for (int i = lo; i <= hi; i++)
		a[i] = aux[i];

	// repeat for parts, skip the extra:
	for (int i = 1; i < radix+2; i++) {
		int lo1 = lo + count[i-1];
		int hi1 = lo + count[i];
		if (lo1 == hi1)  // no strings at count[i]
			continue;
		_rsort(a, lo1, hi1-1, digit+1, radix, aux);
	}

}

// Most Significant Digit sort (MSD)
void radix_sort(char ** a, int n, int radix) {
	char ** aux = calloc(sizeof(char *), n);
	_rsort(a, 0, n-1, 0, radix, aux);
	free(aux);	
}


void main() {
	printf("Sorting text..\n");
	int n = 97;
	char * a[] = {"Picture", "yourself", "in", "a", "boat", "on", "a", "river", "With", "tangerine", "trees", "and", "marmalade", "skies", "Somebody", "calls", "you,", "you", "answer", "quite", "slowly", "A", "girl", "with", "kaleidoscope", "eyes", "Cellophane", "flowers", "of", "yellow", "and", "green", "Towering", "over", "your", "head", "Look", "for", "the", "girl", "with", "the", "sun", "in", "her", "eyes", "And", "she's", "gone", "Lucy", "in", "the", "sky", "with", "diamonds", "Lucy", "in", "the", "sky", "with", "diamonds", "Lucy", "in", "the", "sky", "with", "diamonds,", "ahh", "Follow", "her", "down", "to", "a", "bridge", "by", "a", "fountain", "Where", "rocking", "horse", "people", "eat", "marshmallow", "pies", "Everyone", "smiles", "as", "you", "drift", "past", "the", "flowers", "That", "grow", "so", "incredibly", "high" };

	int radix = 127; // ascii
	radix_sort(a, n, radix);
	for (int i = 0; i < n; i++)
		printf("%d: %s\n", i, a[i]);
}

