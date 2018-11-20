#include <stdio.h>

#define MAX(x,y) ((x<y) ? (y) : (x))

int max_subarray(int*cost, int lo, int hi) {
	if (lo >= hi) return 0;
	if (lo - hi == 2 && cost[lo] < cost[hi])
		return cost[hi] - cost[lo];

	int m = (lo+hi)/2;
	int r1 = max_subarray(cost, lo, m);
	int r2 = max_subarray(cost, m+1, hi);
	int min_ = 999999;
	int max_ = 0;
	for (int i = lo; i <= m; i++)
		if (cost[i] < min_)
			min_ = cost[i];
	for (int i = m; i <= hi; i++)
		if (cost[i] > max_)
			max_ = cost[i];
	int r3 = max_-min_;
	return MAX(MAX(r1,r2),r3);
}

void main() { 
	int cost[] = {100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97};
	int n = 17;
	int r = max_subarray(cost, 0, n-1);
	printf("%d\n", r);
}
