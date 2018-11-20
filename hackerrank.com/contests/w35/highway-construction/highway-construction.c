#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int m = 1000000009;

int modexp(long int x, int y, int m) {
	if(y == 0)
		return 1;
	int z = modexp(x, (int)floor(y/2), m);
	if(z%2 == 0)
		return (z*z)%m;
	return (x*z)%m;
}

int highwayConstruction(long int n, int k) {
	long int sum = 0;
    for(long int i = n - 1; i > 1; i--) {
		sum += modexp(i, k, m)%m;
	}
	return sum;
}

int main() {
    int q; 
    scanf("%i", &q);
    for(int a0 = 0; a0 < q; a0++){
        long int n; 
        int k; 
        scanf("%li %i", &n, &k);
        int result = highwayConstruction(n, k);
        printf("%d\n", result);
    }
    return 0;
}
