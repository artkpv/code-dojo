#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

void main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int n = 0;
	int count = 0;
	scanf("%d\n", &n);
	int stack[n];
	while (n-- > 0) {
		char op;
		int num;
		scanf(" %c", &op);
		if (op == '+') {
			scanf("%d", &num);
			stack[count++] = num;
		}
		else if (op == '-') {
			num = stack[--count];
			printf("%d\n", num);
		}
	}
	exit(0);
}
