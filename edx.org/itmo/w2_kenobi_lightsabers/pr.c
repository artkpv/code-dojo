/*
 
8
add 1
add 2
add 3
add 4
mum!
take
add 5
mum!

1 2 3 4
3 4 1 2
3 4 1 
3 4 1 5
1 5 3 4

 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

typedef struct node {
	struct node * l; // left
	struct node * r; // right
	int num; // lightsaber number
} node;

// Kenobi's table:
typedef struct {
	int n; // count
	node * l; // left
	node * r; // right
	node * m; // middle
} kentable;

kentable * kentable_ctor() { 
	kentable * kt = malloc(sizeof(kentable));
	*kt = (kentable) {.n = 0, .l = NULL, .r = NULL, .m = NULL};
	return kt;
}

void kt_push(kentable * kt, int num) {
	node * oldr = kt->r;
	node * new = malloc(sizeof(node));
	*new = (node) {.l = oldr, .r = NULL, num = num};
	kt->r = new;
	if (oldr != NULL) {
		oldr->r = new;
	}
	if (kt->l == NULL) {
		assert(kt->m == NULL);
		kt->m = new;
		kt->l = new;
	}
	kt->n++;

	// update middle:
	if (kt->n > 3 && kt->n % 2 == 0) {
		kt->m = kt->m->r;
	}
}

int kt_pop(kentable * kt) {
	assert(kt->n > 0);
	int num = kt->r->num;
	// only one:
	if (kt->n == 1) { 
		free(kt->r);
		kt->r = NULL;
		kt->l = NULL;
		kt->m = NULL;
		kt->n = 0;
	}
	else if(kt->n == 2) {
		free(kt->r);
		assert(kt->m == kt->l);
		kt->r = kt->l;
		kt->n--;
	}
	else {  // >2
		node * old = kt->r;
		kt->r = old->l;
		kt->r->r = NULL;
		free(old);
		kt->n--;

		// update middle:
		// 1(m) 2 3 -> 1(m) 2
		// 1 2(m) 3 4 5 -> 1 2(m) 3 4
		// 1 2(m) 3 4 -> 1(m) 2 3
		if (kt->n % 2 == 1) {
			kt->m = kt->m->l;
		}
	}
	return num;
}

void kt_mum(kentable * kt) {
	if (kt->n < 2) {
		return;
	}
	node * l = kt->l;
	node * r = kt->r;
	node * m = kt->m;

	kt->l = m->r;
	kt->l->l = NULL;
	kt->r = m;
	kt->r->r = NULL;
	l->l = r;
	r->r = l;

	kt->m = (kt->n % 2 == 0) ? r : r->l;
}

void kt_print(kentable * kt) {
	printf("%d\n", kt->n);
	node * next = kt->l;
	while (next != NULL) {
		printf("%d ", next->num);
		next = next->r;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n = 0;
	scanf("%d\n", &n);
	const int MAXS = 10;
	char op[MAXS];  
	kentable * kt = kentable_ctor();
	for (int i = 0; i < n; i++){
		scanf("%s", op);
		if (strcmp(op, "add") == 0){
			int num;
			scanf("%d", &num);
			kt_push(kt, num);
		}
		else if (strcmp(op, "take") == 0) {
			kt_pop(kt);
		}
		else if (strcmp(op, "mum!") == 0) {
			kt_mum(kt);
		}
		else {
			assert(0); // should hit some op
		}
	}
	kt_print(kt);
}
