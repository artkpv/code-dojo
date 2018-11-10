/*
 * Hash table with separate chaining for collision resolution:
 *   put(..)
 *   search(..)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct hnode {
	int key;
	char * value;
};

typedef struct hnode Node;
typedef struct hnode * NodePtr;

int get_hash(char * s) {
	int r = 19;  // some radix for chars
	int hash = 0;
	int n = strlen(s);
	for (int i = 0; i < n; i++) 
		hash = hash*r + (int)s[i];
	return hash;
}

int calculate_hash(int hash, int m) {
	int bits31 = 0x7fffffff;
	return (hash & bits31) % m;
}

void put (NodePtr ht[], int m, int key, char * value) {
	int i = calculate_hash(key, m);
	for (; ht[i] != NULL; i++) {
		if (ht[i]->key == key)
		{
			ht[i]->key = key;
			ht[i]->value = value;
			return;
		}
	}

	NodePtr newnode = (NodePtr) malloc(sizeof(Node));
	newnode->key = key;
	newnode->value = value;
	ht[i] = newnode;
}

char * search (NodePtr ht[], int m, int key) {
	for (int i = calculate_hash(key, m); ht[i] != NULL; i++) {
		if (ht[i]->key == key)
			return ht[i]->value;
	}
	return NULL;
}

void print_ht(NodePtr ht[], int m) {
	int count = 0;
	for (int i = 0; i < m; i++) {
		printf("%d: ", i);
		if (ht[i] != NULL) {
			NodePtr np = ht[i];
			printf("%d '%s'", np->key, np->value);
			count++;
		}
		printf("\n");
	}
	printf("count: %d\n", count);
}

void main() {
	char * s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.";

	int N = strlen(s);
	int m = 100;
	NodePtr hashtable[m];  
	for (int i = 0; i < m; i++) // INIT! Or underfined (garbage).
		hashtable[i] = NULL;
	int word = 1;
	char * sp = s;
	int words_num = 0;
	while ( *sp != '\0') {
		if (*sp == ' ') {
			if (word > 1) {
				char * value = calloc(word, sizeof(char));
				strncpy(value, (sp-word+1), word-1);
				int key = get_hash(value);
				put(hashtable, m, key, value);
				words_num++;
			}
			sp++;
			word = 1;
		}
		else {
			sp++;
			word++;
		}
	}
	printf("%d\n", words_num);
	print_ht(hashtable, m);

	char * tests[] = { "Lorem", "ipsum", "kasd", "anything" };
	for (int i = 0; i < 4; i++) {
		int key = get_hash(tests[i]);
		char * value = search(hashtable, m, key);
		printf("test '%s': %s\n", tests[i], value);
	}
}
