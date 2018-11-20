#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int COUNT = 0;

void exch(int*a, int i, int j) {
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
	COUNT++;
}

void printme(int*a, int l, int r) {
	for (int i = l; i <= r; i++)
	  	printf("%d ", a[i]);
	printf("\n");
}

int median(int a, int b, int c) {
	if (a < b) {
		if (b < c) return b;
		else if (a < c) return c;
		else return a;
	}
	else {
		if (a < c) return a;
		else if (b < c) return c;
		return b;
	}
}

void sort(int*a, int l, int r) {
	if (l >= r) return;

	int v = median(a[l], a[r], a[(int)((r+l)/2)]);
	int lt = l, i = l, gt = r;
	while (i <= gt) {
		if (a[i] < v) exch(a, i++, lt++);
		else if (v < a[i]) exch(a, i, gt--);
		else i++;
	}

	sort(a, l, lt-1); 
	sort(a, gt+1, r); 
}

void shuffle(int*a, int n) {
	for (int i = 0; i < n; i++) {
		int r = i*rand()/RAND_MAX;
		exch(a, i, r);
	}
}

void main() {
	srand(time(NULL)); 
	int n = 10000;
	int * a = calloc(n, sizeof(int));
	for (int i = 0; i < n; i++) {
		a[i] = 1+i;
	}

	// shuffle(a, n);

	// printme(a, 0, n-1);
	sort(a, 0, n-1);
	// printme(a, 0, n-1);

	printf("%d\n", COUNT);
}

