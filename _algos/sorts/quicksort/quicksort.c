#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int COUNT = 0;

void exch(int*a, int i, int j) {
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
}

void printme(int*a, int l, int r) {
	for (int i = l; i <= r; i++)
	  	printf("%d ", a[i]);
	printf("\n");
}

void quicksort(int*a, int l, int r) {
	if (l >= r) return;

	// int p = l + (r-l+1)*rand()/RAND_MAX;
	// exch(a, p, l);
	int i = l, j = r+1;
	while (i < j) {
		while (a[++i] < a[l])
			if (i == r) break;
		while (a[l] < a[--j])
			if (j == l) break;
		if (i >= j) break;
		exch(a, i, j);
	}
	exch(a, j, l); 
	quicksort(a, l, i-1); 
	quicksort(a, i+1, r); 
}

void shuffle(int*a, int n) {
	for (int i = 0; i < n; i++) {
		int r = i*rand()/RAND_MAX;
		exch(a, i, r);
	}
}

void main() {
	srand(time(NULL)); 
	int n = 20;
	int * a = calloc(n, sizeof(int));
	for (int i = 0; i < n; i++) {
		a[i] = n-i;
	}

	// shuffle(a, n);

	printme(a, 0, n-1);
	quicksort(a, 0, n-1);
	printme(a, 0, n-1);

	printf("%d\n", COUNT);
}

