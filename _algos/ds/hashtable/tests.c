#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>
#include "hashtable_lp.c"


int get_hash(const char * s) {
	// using Horner's method:
	int r = 31;  // some radix for chars
	unsigned hash = 0;
	int n = strlen(s);
	for (int i = 0; i < n; i++) 
		hash = ((hash*r) + (int)s[i]) % INT_MAX;

	assert (hash > 0);
	return (int)hash;
}

const char * malloc_str(const char * buffer) {
	char * value = (char*) calloc(strlen(buffer)+1, sizeof(char));
	strcpy(value, buffer);
	return value;
}

bool test_put_search_delete() {
	int m = 2;
	HT * ht = HT_ctor(m);

	const char * value = malloc_str("testmehere");
	int key = get_hash(value);

	// act:
	ht_put(ht, key, value);

	// assert :
	const char * found = ht_search(ht, key);
	assert(strcmp(value, found) == 0);

	// act:
	ht_delete(ht, key);

	// assert:
	found = ht_search(ht, key);
	assert(found == NULL);

	HT_free(ht);
	printf("test_put_search_delete - done\n");
	return true;
}

bool test_many_keys(){
	int m = 100;
	HT * ht = HT_ctor(m);

	const char * s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.";

	int N = strlen(s);
	int word = 1;
	const char * sp = s;
	while (*sp != '\0') {
		if (*sp == ' ') {
			if (word > 1) {
				char * value = (char*) calloc(word, sizeof(char));
				strncpy(value, (sp-word+1), word-1);
				int key = get_hash(value);

				// act:
				ht_put(ht, key, value);

				// assert:
				const char * found = ht_search(ht, key);
				assert(found != NULL);
				assert(strcmp(found, value) == 0);
			}
			sp++;
			word = 1;
		}
		else {
			sp++;
			word++;
		}
	}

	// assert 2:
	const char * tests[] = {"Lorem", "ipsum", "kasd"};
	for (int i = 0; i < 3; i++) {
		int key = get_hash(tests[i]);
		const char * found = ht_search(ht, key);
		assert(found != NULL && strcmp(found, tests[i]) == 0);
	}

	// assert 3:
	assert(ht_search(ht, get_hash("anything")) == NULL);

	HT_free(ht);
	printf("test_many_keys - done\n");
	return true;
}

bool test_resize() {
	printf("test_resize... \n");
	int init_size = 1;
	HT * ht = HT_ctor(init_size);

	int N = 15000;
	for (int i = 1; i <= N; i++) {
		char buffer[20];
		itoa(i, buffer, 10);
		const char * value = malloc_str(buffer);
		int key = get_hash(value);

		// act:
		ht_put(ht, key, (const char*)value);

		// assert:
		const char * found = ht_search(ht, key);
		assert(strcmp(value, found) == 0);
		assert(ht->count == i);
	}

	// print_ht(ht);

	printf(" test_resize, deleting...\n");

	for (int i = 1; i <= N; i++) {
		char buffer[20];
		itoa(i, buffer, 10);
		int key = get_hash(buffer);
		const char * nvalue = ht_search(ht, key);
		assert(nvalue != NULL);

		// act:
		ht_delete(ht, key);

		// assert:
		const char * found = ht_search(ht, key);
		assert(found == NULL);
		assert(ht->count == (N - i));
		if (i % 1000 == 0)
			printf(" test_resize, %d deleted\n", i);
	}

	HT_free(ht);
	printf("test_resize - done\n");
	return true;
}

int main() {
	assert(test_put_search_delete());
	assert(test_many_keys());
	assert(test_resize());
	printf("\nAll tests pass. Press any key.\n");
	getc(stdin);
	return 0;
}
