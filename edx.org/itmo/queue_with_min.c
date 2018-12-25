#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

void main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int n = 0;
	int last = 0;
	int first = 0;
	scanf("%d\n", &n);
	int queue[n];
	int min[n];
	while (n-- > 0) {
		char op;
		int num;
		scanf(" %c", &op);
		if (op == '+') {
			scanf("%d", &num);
			queue[last++] = num;
		}
		else if (op == '-') {
			num = queue[first++];
			printf("%d\n", num);
		}
	}
	exit(0);
}
