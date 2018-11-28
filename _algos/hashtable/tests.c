#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
#include "hashtable_lp.c"

#define bool int
#define TRUE 1
#define FALSE 0

int get_hash(char * s) {
	// using Horner's method:
	int r = 31;  // some radix for chars
	unsigned hash = 0;
	int n = strlen(s);
	for (int i = 0; i < n; i++) 
		hash = ((hash*r) + (int)s[i]) % INT_MAX;

	assert (hash > 0);
	return (int)hash;
}

bool test_many_keys(){
	int m = 100;
	HT ht = HT_ctor(m);

	char * s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.";

	int N = strlen(s);
	int word = 1;
	char * sp = s;
	while (*sp != '\0') {
		if (*sp == ' ') {
			if (word > 1) {
				char * value = calloc(word, sizeof(char));
				strncpy(value, (sp-word+1), word-1);
				int key = get_hash(value);

				put(ht, key, value);
				char * found = search(ht, key);
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

	char * tests[] = { "Lorem", "ipsum", "kasd"};
	for (int i = 0; i < 3; i++) {
		int key = get_hash(tests[i]);
		char * found = search(ht, key);
		assert(found != NULL && strcmp(found, tests[i]) == 0);
	}

	assert(search(ht, get_hash("anything")) == NULL);
	// print_ht(ht);
	for (int i = 0; i < ht->count; i++) 
		free(ht->arr[i]);
	HT_free(ht);
	return TRUE;
}

bool test_put_search_delete() {
	int m = 2;
	HT ht = HT_ctor(m);

	char * value = "testmehere";
	int key = get_hash(value);
	put(ht, key, value);
	char * found = search(ht, key);
	assert(strcmp(value, found) == 0);
	delete(ht, key);
	found = search(ht, key);
	assert(found == NULL);

	for (int i = 0; i < ht->count; i++) 
		free(ht->arr[i]);
	HT_free(ht);
	return TRUE;
}

bool test_resize() {
	int init_size = 1;
	HT ht = HT_ctor(init_size);

	int N = 15000;
	for (int i = 1; i <= N; i++) {
		char buffer[20];
		itoa(i, buffer, 10);
		int key = get_hash(buffer);
		char * value = calloc(strlen(buffer)+1, sizeof(char));
		strcpy(value, buffer);
		put(ht, key, value);
		char * found = search(ht, key);
		assert(strcmp(value, found) == 0);
		assert(ht->count == i);
	}

	// print_ht(ht);

	for (int i = 1; i <= N; i++) {
		char buffer[20];
		itoa(i, buffer, 10);
		int key = get_hash(buffer);
		char * nvalue = search(ht, key);
		assert(nvalue != NULL);
		delete(ht, key);
		char * found = search(ht, key);
		assert(found == NULL);
		assert(ht->count == (N - i));
		free(nvalue);
	}

	for (int i = 0; i < ht->count; i++) 
		free(ht->arr[i]);
	HT_free(ht);
	return TRUE;
}

void main() {
	assert(test_put_search_delete());
	assert(test_many_keys());
	assert(test_resize());
	printf("\nAll tests pass\n");
}
