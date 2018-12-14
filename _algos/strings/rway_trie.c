/*
 *
 * R-way trie data structure. Stores values, positive integers by string key.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

struct node {
	struct node ** next;
	int value;
};

typedef struct node Node;
typedef Node * NodePtr;

int RADIX = 26;
int NULLVALUE = -1;

NodePtr Node_ctr() {
	NodePtr n = (NodePtr) malloc(sizeof(Node));
	n->next = (NodePtr*) malloc(sizeof(NodePtr*) * RADIX);
	for (int i = 0; i < RADIX; i++)
		n->next[i] = NULL;
	n->value = NULLVALUE;
	return n;
}

void Node_free(NodePtr trie) {
	for(int i = 0; i < RADIX; i++) {
		if (trie->next[i] != NULL) {
			Node_free(trie->next[i]);
		}
	}
	free(trie);
}

int _rt_chr_to_inx(char ch) {
	return (int)(ch - 'a');
}

NodePtr _rt_put(NodePtr t, char * key, int keylen, int i, int value) {
	if (t == NULL)
		t = Node_ctr();
	if (i == keylen - 1) {
		t->value = value;
		return t;
	}
	int inx = _rt_chr_to_inx(key[i]);
	t->next[inx] = _rt_put(t->next[inx], key, keylen, i + 1, value);
	return t;
}

void rt_put(NodePtr t, char * key, int value) {
	int n = strlen(key);
	*t = *_rt_put(t, key, n, 0, value);
}

int _rt_search(NodePtr t, char * key, int keylen, int i) {
	if(t == NULL)
		return NULLVALUE;
	if (keylen - 1 == i)
		return t->value;
	int inx = _rt_chr_to_inx(key[i]);
	return _rt_search(t->next[inx], key, keylen, i + 1);
}

int rt_search(NodePtr t, char * key) {
	return _rt_search(t, key, strlen(key), 0);
}

void main() {
	NodePtr trie = Node_ctr();
	rt_put(trie, "entry", 4);
	rt_put(trie, "entrance", 6);
	assert(rt_search(trie, "entry") == 4);
	assert(rt_search(trie, "entrance") == 6);
	assert(rt_search(trie, "ending") == NULLVALUE);
	rt_put(trie, "she", 10);
	rt_put(trie, "shell", 11);
	rt_put(trie, "sea", 12);
	assert(rt_search(trie, "she") == 10);
	assert(rt_search(trie, "shell") == 11);
	assert(rt_search(trie, "sea") == 12);

	
	Node_free(trie);
	printf("all tests pass\n");
}
