/*

Idea with using two queues (two doubly linked list)

*/ 

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

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
    llnode * node = malloc(sizeof(llnode));
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
    llnode * node = malloc(sizeof(llnode));
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


void enqueue(linkedlist * q, linkedlist * mins, int num) {
	int * nump = (int*) malloc(sizeof(int));
	*nump = num;
	ll_addright(q, nump);

	int * num_count = (int*)calloc(2, sizeof(int));
	num_count[0] = num;
	num_count[1] = 1;
	llnode * x = mins->right;
	while (x != NULL && ((int*)x->value)[0] >= num) {
		num_count[1] += ((int*)x->value)[1];
		ll_popright(mins);
		x = mins->right;
	}
	ll_addright(mins, num_count);
}

void dequeue(linkedlist * q, linkedlist * mins) {
	if (q->left == NULL) return;
	int * nump = (int*) ll_popleft(q);
	int num = *nump;
	free(nump);

	assert(mins->left);
	llnode * minn = mins->left;
	int * num_count = (int*)minn->value;
	if (num_count[1] > 1){
		num_count[1]--;
	}
	else{
		ll_popleft(mins);
	}
}

int get_min(linkedlist * q, linkedlist * mins) {
	llnode * minn = mins->left;
	int * num_count = (int*)minn->value;
	return num_count[0];
}

void main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int n = 0;
	scanf("%d\n", &n);

	linkedlist * queue = ll_ctor();
	linkedlist * mins = ll_ctor();

	while (n-- > 0) {
		char op;
		int num;
		scanf(" %c", &op);
		if (op == '+') {
			scanf("%d", &num);
			enqueue(queue, mins, num);
		}
		else if (op == '-') {
			dequeue(queue, mins);
		}
		else if (op == '?') {
			int min = get_min(queue, mins);
			printf("%d\n", min);
		}
	}
	ll_free(queue);
	ll_free(mins);
	exit(0);
}
