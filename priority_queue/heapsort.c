#include <stdio.h>

void exch(int*a, int i, int j) {
  int t = a[i];
  a[i] = a[j];
  a[j] = t;
}

void printme(int*a, int n){
  for (int i = 0; i <= n; i++)
    printf("%d ", a[i]);
  printf("\n");
}

int parent(int i) {
  return (int)(i/2);
}

void sift_down(int*a, int n, int i) {
  while (i*2 <= n) {
    int k = i*2;
    if (k+1 <= n && a[k] < a[k+1]) 
      k++;
    if (a[i] >= a[k])
      break;
    exch(a, i, k);
    i = k;
  }
}

void sift_up(int*a, int n, int i) {
  while (a[parent(i)] < a[i]) {
    exch(a, parent(i), i);
    i = parent(i);
  }
}

void heapsort(int a[], int n) {
  // a[1] - first, a[n] - last, n+1 - real size
  
  for (int i = n/2; i >= 1; i--)
    sift_down(a, n, i);

  while (n > 1) {
    exch(a, 1, n--);
    sift_down(a, n, 1);
  }
}

void main() {
  int n = 100;
  int a[n+1];
  a[0] = 0;
  for (int i = 0; i < n; i++)
    a[i+1] = n-i;

  heapsort(a, n);
  printme(a, n);
}
