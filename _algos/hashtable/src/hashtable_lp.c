#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

/*

HASHTABLE / map
Linear probing for collision resolution and resizing.

*/

// Key and value pair
typedef struct {
	int key;
	const char * value;
} Node;

// Hashtable
typedef struct {
	int count;
	int m;
	Node ** arr;
} HT;

HT * HT_ctor(int m);

void HT_free(int m);

// Stores value by a key. Increases size if limit reached.
void ht_put (HT * ht, int key, const char * value);

// Finds value by key. Returns NULL if nothing found.
const char * ht_search (HT * ht, int key);

// Removes key. Shrinks hashtable if sparse.
void ht_delete (HT * ht, int key);

// Prints to STDOUT all key/value pairs
void print_ht(HT * ht); 


// Truncates by modulo m
int _calculate_hash(int hash, int m) {
	return (hash & INT_MAX) % m;
}

HT * HT_ctor(int m) {
	HT * ht = (HT*) malloc(sizeof(HT));
	ht->count = 0;
	ht->m = m;
	Node ** arr = (Node **) calloc(m, sizeof(Node*));
	for (int i = 0; i < m; i++)
		arr[i] = NULL;
	ht->arr = arr;
}

void HT_free(HT * ht) {
	if (ht != NULL) {
		if (ht->arr != NULL) {
			for (int i = 0; i < ht->count; i++) {
				// free((void*)ht->arr[i]->value);
				free(ht->arr[i]);
			}
			free(ht->arr);
		}
		free(ht);
	}
}

// Puts key/value into the given arr
void _put(Node ** arr, int m, int key, const char * value) {
	int i = _calculate_hash(key, m);
	for (; arr[i] != NULL; i = (i + 1) % m) {
		if (arr[i]->key == key)
		{
			Node * n = arr[i];
			n->key = key;
			n->value = value;
			return;
		}
	}
	Node * newnode = (Node*) malloc(sizeof(Node));
	newnode->key = key;
	newnode->value = value;
	arr[i] = newnode;
}

// Copies all nodes to new array of newsize size. Replaces the old.
void _ht_resize(HT * ht, int newsize) {
	printf(" resizing %d\n", newsize);
	assert(ht->count <= newsize);
	Node ** arr = (Node**) calloc(newsize, sizeof(Node*));
	for (int i = 0; i < ht->m; i++){
		Node * node = ht->arr[i];
		if (node != NULL) 
			_put(arr, newsize, node->key, node->value);
	}
	free(ht->arr);
	ht->arr = arr;
	ht->m = newsize;
}

void ht_put (HT * ht, int key, const char * value) {
	_put(ht->arr, ht->m, key, value);
	ht->count++;
	if (ht->count > 0 && ht->count * 2 >= ht->m)
		_ht_resize(ht, ht->m * 2);
}

const char * ht_search (HT * ht, int key) {
	int i = _calculate_hash(key, ht->m);
	for (; ht->arr[i] != NULL; i = (i+1) % ht->m) {
		if (ht->arr[i]->key == key)
			return ht->arr[i]->value;
	}
	return NULL;
}

void ht_delete (HT * ht, int key) {
	int i = _calculate_hash(key, ht->m);
	for (; ht->arr[i] != NULL; i = (i+1) % ht->m) {
		if (ht->arr[i]->key == key) {			
			free((void*)ht->arr[i]->value);
			free(ht->arr[i]);
			ht->arr[i] = NULL;
			break;
		}
	}
	ht->count--;

	i = (i+1) % ht->m;

	while (ht->arr[i] != NULL) {
		Node * n = ht->arr[i];
		const char * value = n->value;
		int key = n->key;
		free(n);
		ht->arr[i] = NULL;
		ht->count--;
		_put(ht->arr, ht->m, key, value);
		ht->count++;
		i = (i+1) % ht->m;
	}

	if (ht->count > 0 && ht->count * 8 <= ht->m) 
		_ht_resize(ht, ht->m / 2);
}

void print_ht(HT * ht) {
	int count = 0;
	for (int i = 0; i < ht->m; i++) {
		printf("%d: ", i);
		if (ht->arr[i] != NULL) {
			Node* np = ht->arr[i];
			printf("%d '%s'", np->key, np->value);
			count++;
		}
		printf("\n");
	}
	printf("count: %d (%d)\n", count, ht->count);
}
