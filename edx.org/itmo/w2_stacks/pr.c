#include <stdio.h>

typedef struct node {
	struct node * next;
	int count;
	int height;
} node;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n = 0;
	scanf("%d\n", &n);
	int a[n];
	for (int i = 0; i < n; i++)
		scanf("%d", (a+i));

	/* 
	node * first;
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (a[i] > 0) {
			if (first == NULL) {
				*first = (node) {.count = 1, .height = 1, .next = NULL};
				count++;
			}
			else if (first->height == 1) {
				first
			}
		}
	}
	*/
}
