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
	char * s;
	int s_size;
	struct hnode * next;
};

typedef struct hnode Node;
typedef struct hnode * NodePtr;

int get_hash(char * s, int n) {
	int r = 19;  // some radix for chars
	int hash = 0;
	for (int i = 0; i < n; i++) 
		hash = hash*r + (int)s[i];
	return hash;
}

void put (NodePtr ht[], int m, char * s, int n) {
	int bits31 = 0x7fffffff;
	int hash = get_hash(s, n);
	int inx = (hash & bits31) % m;

	NodePtr np = ht[inx];
    
	while (np != NULL) {
		if (hash == np->key) {
			free(np->s);
			np->key = hash;
			np->s = s;
			np->s_size = n;
			printf("replace %d %d %s\n",inx, hash, s);
			return;
		}
		np = np->next;
	}

	NodePtr newnode = (NodePtr) malloc(sizeof(Node));
	newnode->key = hash;
	newnode->s = s;
	newnode->s_size = n;
	newnode->next = ht[inx];
	ht[inx] = newnode;
}

int search (NodePtr ht[], int m, char * s) {
	int bits31 = 0x7fffffff;
	int hash = get_hash(s, strlen(s));
	int inx = (hash & bits31) % m;

	NodePtr np = ht[inx];

	while (np != NULL) {
		if (hash == np->key) 
			return 1;
		np = np->next;
	}
	return 0;
}

void print_ht(NodePtr ht[], int M) {
	int count = 0;
	for (int i = 0; i < M; i++) {
		NodePtr np = ht[i];
		printf("%d: ", i, np);
		while (np != NULL) {
			printf("(%d '%s')", np->key, np->s);
			count++;
			np = np->next;
		}
		printf("\n");
	}
	printf("count: %d\n", count);
}

void main() {
	char * s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.";

	int N = strlen(s);
	int M = 20;
	NodePtr hashtable[M];  
	for (int i = 0; i < M; i++) // INIT! Or underfined (garbage).
		hashtable[i] = NULL;
	int word = 1;
	char * sp = s;
	int words_num = 0;
	while ( *sp != '\0') {
		if (*sp == ' ') {
			if (word > 1) {
				char * new_s = calloc(word, sizeof(char));
				strncpy(new_s, (sp-word+1), word-1);
				put(hashtable, M, new_s, word-1);
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
	print_ht(hashtable, M);

	char * tests[] = { "Lorem", "ipsum", "kasd", "anything" };
	for (int i = 0; i < 4; i++) {
		int res = search(hashtable, M, tests[i]);
		printf("test '%s': %d\n", tests[i], res);
	}
}
