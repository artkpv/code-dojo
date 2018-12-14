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
	int inx = (int)(ch - 'a');
	assert(0 <= inx);
	assert(inx < RADIX);
	return inx;
}

char _rt_inx_to_chr(int inx) {
	return (char) ('a' + inx);
}

NodePtr _rt_put(NodePtr t, char * key, int keylen, int i, int value) {
	if (t == NULL)
		t = Node_ctr();
	if (i == keylen) {
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
	if (keylen == i)
		return t->value;
	int inx = _rt_chr_to_inx(key[i]);
	return _rt_search(t->next[inx], key, keylen, i + 1);
}

int rt_search(NodePtr t, char * key) {
	return _rt_search(t, key, strlen(key), 0);
}

int _rt_longest_prefix(NodePtr t, char * query, int i, int length, int qlen) {
	if (t == NULL)
		return length;
	if (t->value != NULLVALUE)
		length = i;
	if (i == qlen)
		return length;
	int inx = _rt_chr_to_inx(query[i]);
	if (t->next[inx] == NULL)
		return length;	
	return _rt_longest_prefix(t->next[inx], query, i + 1, length, qlen);
}

// Returns length of longest prefix key in the trie for the given query string.
// Example: Trie: "a", "ab". Query: "ac". Result: 1
int rt_longest_prefix(NodePtr t, char * query) {
	int qlen = strlen(query);
	if (qlen == 0)
		return 0;
	int inx = _rt_chr_to_inx(query[0]);
	if (t == NULL)
		return 0;
	return _rt_longest_prefix(t->next[inx], query, 1, 0, qlen);
}

void _rt_print_inorder(NodePtr t, char * buffer, int len) {
	if (t->value != NULLVALUE) {
		char str[len + 1];
		int i = -1;
		while (++i < len)
			str[i] = buffer[i];
		str[i] = '\0';
		printf("'%s': %d\n", str, t->value);
	}
	for (int i = 0; i < RADIX; i++) {
		if (t->next[i] != NULL) {
			buffer[len] = _rt_inx_to_chr(i);
			_rt_print_inorder(t->next[i], buffer, len + 1);
		}
	}
}

void rt_print_inorder(NodePtr t) {
	static int MAXSTRING = 999;
	char * buffer = malloc(sizeof(char) * MAXSTRING);
	_rt_print_inorder(t, buffer, 0);
	free(buffer);
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

	assert(rt_longest_prefix(trie, "shellsort") == 5);
	assert(rt_longest_prefix(trie, "she") == 3);
	assert(rt_longest_prefix(trie, "nonexistant") == 0);

	rt_print_inorder(trie);
	
	Node_free(trie);
	printf("all tests pass\n");
}
