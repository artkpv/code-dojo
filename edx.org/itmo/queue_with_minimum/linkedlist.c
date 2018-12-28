#include <stdlib.h>
#include <assert.h>

/*
Doubly linked list
*/

typedef struct llnode {
	struct llnode * left;
	struct llnode * right;
	void* value;
} llnode;

typedef struct linkedlist {
	llnode * left;
	llnode * right;
    int count;
} linkedlist;

linkedlist * ll_ctor() {
	linkedlist * ll = malloc(sizeof(linkedlist));
	*ll = (linkedlist) {
        .left = NULL,
        .right = NULL,
        .count = 0
	};
	return ll;
}

void ll_free(linkedlist * ll) {
    llnode * node = ll->left;
    while (node != NULL) {
        if (node->value) free(node->value);
        llnode * next = node->right;
        free(node);
        node = next;
    }
    free(ll);
}

void ll_addright(linkedlist * ll, void * value) {
    assert(ll != NULL);
    assert(value != NULL);
    llnode * node = (llnode*)malloc(sizeof(llnode));
    *node = (llnode) {.left = ll->right, .right = NULL, .value = value};
    if (ll->right != NULL) {
        ll->right->right = node;
    }
    ll->right = node;
    if (ll->left == NULL){ 
        ll->left = ll->right;
    }
    ll->count++;
}

void ll_addleft(linkedlist * ll, void * value) {
    assert(ll != NULL);
    assert(value != NULL);
    llnode * node = (llnode*)malloc(sizeof(llnode));
    *node = (llnode) {.left = NULL, .right = ll->left, .value = value};
    if (ll->left != NULL) {
        ll->left->left = node;
    }
    ll->left = node;
    if (ll->right == NULL){ 
        ll->right = ll->left;
    }
    ll->count++;
}

void * ll_popright(linkedlist * ll) {
    if (ll->right == NULL) return NULL;
    llnode * node = ll->right;
    if (node->left) {
        ll->right = node->left;
        node->left->right = NULL;
        node->left = NULL;
    }
    else {
        assert(ll->left == node);
        ll->right = NULL;
        ll->left = NULL;
    }
    void * value = node->value;
    free(node);
    return value;
}

void * ll_popleft(linkedlist * ll) {
    if (ll->left == NULL) return NULL;
    llnode * node = ll->left;
    if (node->right) {
        ll->left = node->right;
        node->right->left = NULL;
        node->right = NULL;
    }
    else {
        assert(ll->right == node);
        ll->left = NULL;
        ll->right = NULL;
    }
    void * value = node->value;
    free(node);
    return value;
}
