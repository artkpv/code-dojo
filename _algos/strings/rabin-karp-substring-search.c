/*
 * 
 * Rabin-Karp algorithm to search string for pattern.
 *
 */
#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <string.h>

// 
// Searches for m-chars p pattern in n-chars s string with chars in radix range.
// Returns index of first char in a first match or -1.
//
int search(char * s, int n, char * p, int m, int radix) {
	printf("searching '%s' (%d) in '%s' (%d) with %d radix\n", p, m, s, n, radix);
	assert(radix > 0);
	int mod = 97;  // some prime for modulo
	int ch_to_ord(char ch) { return (int)ch - (int)'0'; }
	int hash(char * s, int n) {
		int hash = 0;
		for (int i = 0; i < n; i++) {
			hash += ch_to_ord(s[i]) * (int) (pow(radix, (n - 1 - i))) % mod;
			hash %= mod;
		}
		return hash;
	}
	if (m > n) return -1;
	int hash_s = hash(s, m);
	int hash_p = hash(p, m);
	if (hash_s == hash_p) {
		printf(" found %d\n", 0);
		return 0;
	}
    int r_in_m1 = (int) (pow(radix, (m - 1))) % mod;
	for (int i = m; i < n; i++) {
		hash_s += mod - ((ch_to_ord(s[i-m]) * r_in_m1) % mod);
		hash_s = (hash_s * radix + ch_to_ord(s[i])) % mod;
		if (hash_s == hash_p && strncmp(s+i+1-m, p, m) == 0) {
			printf(" found %d\n", i+1-m);
			return i + 1 - m;
		}
	}
	printf(" not found\n");
	return -1;
}

void main() {
	assert(search("1", 1, "1", 1, 10) == 0);
	assert(search("22221", 5, "1", 1, 10) == 4);
	assert(search("4321567123", 10, "567", 3, 10) == 4);
	assert(search("4321123", 10, "567", 3, 10) == -1);
}
