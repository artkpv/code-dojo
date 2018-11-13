#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

//
//  HASHTABLE, linear probing for collision resolution
//

typedef struct {
	int key;
	char * value;
} Node;

typedef Node * NodePtr;

int calculate_hash(int hash, int m) {
	return (hash & INT_MAX) % m;
}

typedef struct HTStruct {
	int count;
	int m;
	NodePtr * arr;
} * HT;

HT 
HT_ctor(int m) {
	HT ht = (HT) malloc(sizeof(struct HTStruct));
	ht->count = 0;
	ht->m = m;
	NodePtr * arr = (NodePtr*) calloc(m, sizeof(NodePtr));
	for (int i = 0; i < m; i++)
		arr[i] = NULL;
	ht->arr = arr;
}

void
HT_free(HT ht) {
	if (ht != NULL) {
		if (ht->arr != NULL) 
			free(ht->arr);
		free(ht);
	}
}

void
_put(NodePtr* arr, int m, int key, char * value) {
	int i = calculate_hash(key, m);
	for (; arr[i] != NULL; i = (i + 1) % m) {
		if (arr[i]->key == key)
		{
			NodePtr n = arr[i];
			n->key = key;
			n->value = value;
			return;
		}
	}

	NodePtr newnode = (NodePtr) malloc(sizeof(Node));
	newnode->key = key;
	newnode->value = value;
	arr[i] = newnode;
}

void
resize(HT ht, int m) {
	printf("resize %d -> %d\n", ht->m, m);
	assert(ht->count < m);
	printf(" count=%d\n", ht->count);

	NodePtr * arr = (NodePtr*) calloc(m, sizeof(NodePtr));
	int count = 0;
	for (int i = 0; i < ht->m; i++) {
		NodePtr n = ht->arr[i];
		if (n != NULL) {
			_put(arr, m, n->key, n->value);
			free(n);
			count++;
		}
		else {
			arr[i] = NULL;
		}
	}

	free(ht->arr);
	ht->arr = arr;
	ht->m = m;
	ht->count = count;
}

// Stores value by a key
void 
put (HT ht, int key, char * value) {
	_put(ht->arr, ht->m, key, value);
	ht->count++;
	if (ht->count * 2 > ht->m) 
		resize(ht, ht->m*2);
}

// Finds value by key
char * 
search (HT ht, int key) {
	for (int i = calculate_hash(key, ht->m); ht->arr[i] != NULL; i = (i+1) % ht->m) {
		if (ht->arr[i]->key == key)
			return ht->arr[i]->value;
	}
	return NULL;
}


// Removes key
void
delete (HT ht, int key) {
	int i = calculate_hash(key, ht->m);
	for (; ht->arr[i] != NULL; i = (i+1) % ht->m) {
		if (ht->arr[i]->key == key) {			
			ht->arr[i] = NULL;
		}
	}

	i = (i+1) % ht->m;

	while (ht->arr[i] != NULL) {
		NodePtr n = ht->arr[i];
		char * value = n->value;
		int key = n->key;
		free(n);
		// TODO free(n->value)
		ht->arr[i] = NULL;
		put(ht, key, value);
		if (ht->arr[i] == NULL)
			break;
		else
			i = (i+1) % ht->m;
	}

	ht->count--;
	if ( ht->count * 8 <= ht->m) 
		resize(ht, (int)ht->m/2);
}

void 
print_ht(HT ht) {
	int count = 0;
	for (int i = 0; i < ht->m; i++) {
		printf("%d: ", i);
		if (ht->arr[i] != NULL) {
			NodePtr np = ht->arr[i];
			printf("%d '%s'", np->key, np->value);
			count++;
		}
		printf("\n");
	}
	printf("count: %d (%d)\n", count, ht->count);
}
