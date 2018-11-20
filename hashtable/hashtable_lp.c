#include <stdio.h>
#include <stdlib.h>
// #include <stdint.h>
#include <string.h>
#include <assert.h>

//
//  HASHTABLE, linear probing for collision resolution
//

// #define INT_MAX 0x7fffffff

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
_arr_free(NodePtr * arr, int n, int free_elems) {
	if (arr != NULL) {
		if (free_elems == 1) {
			for (int i = 0; i < n; i++) {
				if (*(arr + i) != NULL)
					free(*(arr + i));
			}
		}
		free(arr);
	}
}

void
_ht_resize(HT ht, int newsize) {
	printf(" resizing %d\n", newsize);
	assert(ht->count <= newsize);
	NodePtr * arr = calloc(newsize, sizeof(NodePtr));
	for (int i = 0; i < ht->m; i++)
		arr[i] = ht->arr[i];
	free(ht->arr);
	ht->arr = arr;
	ht->m = newsize;
}


void
HT_free(HT ht) {
	if (ht != NULL) {
		_arr_free(ht->arr, ht->m, 1);
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

// Stores value by a key
void 
put (HT ht, int key, char * value) {
	_put(ht->arr, ht->m, key, value);
	ht->count++;
	if (ht->count * 2 > ht->m)
		_ht_resize(ht, ht->m * 2);
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
		_ht_resize(ht, ht->m / 2);
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
