/*
 * Snowmen.
 *
 * Next: test max (n == 1e6; "i 1000")
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int p;
	unsigned long long m;
} smi;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n = 0;
	scanf("%d\n", &n);
	smi sm[n+1];
	sm[0] = (smi) {0, 0};
	for (int i = 0; i < n; i++) {
		int t,m;
		scanf("%d %d\n", &t, &m);
		if (m > 0) {
			sm[i+1] = (smi) {t, sm[t].m + m};;
		}
		else {
			sm[i+1] = sm[sm[t].p];
		}
	}
	unsigned long long sum = 0;
	for (int i = 0; i < n+1; i++) {
		sum += sm[i].m;
	}
	printf("%llu\n", sum);
	return 0;
}
