/*

1e6 

*/ 

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "linkedlist.c"

linkedlist * queue = ll_ctor();
linkedlist * mins = ll_ctor();

typedef struct mqueue {
	vnode * vqueue_start;
	vnode * vqueue_end;
	cnode * cqueue_start;
	cnode * cqueue_end;
} mqueue;

mqueue * mq_ctor() {
	mqueue * mq = malloc(sizeof(mqueue));
	*mq = (mqueue) {
		.vqueue_start = NULL,
		.vqueue_end = NULL,
		.cqueue_start = NULL,
		.cqueue_end = NULL
	};
	return mq;
}

void mq_enqueue(mqueue * mq, int n) {
	{ 
		vnode * vnew = (vnode*) malloc(sizeof(vnode));
		*vnew = (vnode) {.value = n, .next = NULL};
		vnode * end = mq->vqueue_end;
		if (end != NULL)
			end->next = vnew;
		mq->vqueue_end = vnew;
		if (mq->vqueue_start == NULL)
			mq->vqueue_start = vnew;
	}

	// min tracking:
	{
		int counter = 1;
		while (mq->cqueue_end != NULL && mq->cqueue_end->value >= n) {
			counter += mq->cqueue_end->count;
			if (mq->cqueue_start == mq->cqueue_end) {
				free(mq->cqueue_start);
				mq->cqueue_start = NULL;
				mq->cqueue_end = NULL;
			}
			else {
				cnode * prev = mq->cqueue_end->prev;
				prev->next = NULL;
				free(mq->cqueue_end);
				mq->cqueue_end = prev;
			}
		}
		cnode * end = mq->cqueue_end;
		cnode * new = (cnode*) malloc(sizeof(cnode));
		*new = (cnode) {.value = n, .count = counter, .next = NULL, .prev=end};
		if (end != NULL) {
			end->next = new;
		}
		mq->cqueue_end = new;
		if (mq->cqueue_start == NULL)
			mq->cqueue_start = new;
	}
}
void mq_dequeue(mqueue * mq) {
	{
		if (mq->vqueue_start == NULL)
			return;
		vnode * next = mq->vqueue_start->next;
		free(mq->vqueue_start);
		mq->vqueue_start = next;
		if (next == NULL)
			mq->vqueue_end == NULL;
	}

	{
		cnode * start = mq->cqueue_start;
		if (start->count > 1) {
			start->count--;
		}
		else {
			cnode * next = start->next;
			free(start);
			mq->cqueue_start = next;
			if (next == NULL)
				mq->cqueue_end == NULL;
			else {
				next->prev = NULL;
			}
		}
	}
}

int mq_get_min(mqueue * mq) {
	assert(mq->cqueue_start != NULL);
	return mq->cqueue_start->value;
}

void main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int n = 0;
	scanf("%d\n", &n);

	mqueue * mq = mq_ctor();

	while (n-- > 0) {
		char op;
		int num;
		scanf(" %c", &op);
		if (op == '+') {
			scanf("%d", &num);
			mq_enqueue(mq, num);
		}
		else if (op == '-') {
			mq_dequeue(mq);
		}
		else if (op == '?') {
			int min = mq_get_min(mq);
			printf("%d\n", min);
		}
	}
	exit(0);
}
