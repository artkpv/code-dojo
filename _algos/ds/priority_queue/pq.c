/* 
 * Min priority queue.
 *
 * Author: Artyom K. <w1ld [at] inbox [dot] ru>
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct pq_s {
    int size;
    int capacity;
    int * array;
} * MinPQ;

#define NaN -9999999

MinPQ new_PQ(int capacity) {
    MinPQ pq = (MinPQ) malloc(sizeof(struct pq_s));
    pq->array = (int*) malloc(sizeof(int) * (capacity+1));  // 1 based.
    pq->size = 0;
    pq->capacity = capacity;
    return pq;
}

void free_PQ(MinPQ pq) {
    free(pq->array);
    free(pq);
}

int heappush(MinPQ pq, int val) {
    if (pq->capacity <= pq->size)
        return 1;
    pq->array[pq->size+1] = val;
    pq->size += 1;
    
    int i = pq->size;
    while (i > 1 && pq->array[i/2] > pq->array[i]) {
        int t = pq->array[i/2];
        pq->array[i/2] = pq->array[i];
        pq->array[i] = t;
        i = i / 2;
    }
    return 0;
}

int heappop(MinPQ pq) {
    if (pq->size <= 0)
        return NaN;
    int val = pq->array[1];
    pq->array[1] = pq->array[pq->size];
    pq->size -= 1;

    int i = 1;
    while (i * 2 <= pq->size) {
        int k = i * 2;
        if (k + 1 <= pq->size && pq->array[k] > pq->array[k+1])
            k += 1;
        if (pq->array[i] < pq->array[k])
            break;
        int t = pq->array[k];
        pq->array[k] = pq->array[i];
        pq->array[i] = t;
        i = k;
    }
    return val;
}


// *********************** 
//          Tests
// *********************** 

void test_heappush() {
    int n = 10;
    MinPQ pq = new_PQ(n);
    int i;
    for (i = 0; i < n; ++i) 
        heappush(pq, n-i);

    while (pq->size > 1) {
        int prev = heappop(pq);
        int next = heappop(pq);
        assert(prev <= next);
    }
    assert(heappop(pq) == NaN);
    free_PQ(pq);
}

void test_larger() {
    int n = 1000000;
    MinPQ pq = new_PQ(n);
    int i;
    for (i = 0; i < n; ++i) 
        heappush(pq, n-i);

    // printf(" test_larger ");
    while (pq->size > 1) {
        int prev = heappop(pq);
        int next = heappop(pq);
        assert(prev <= next);
        // printf(" %d %d", prev, next);
    }
    // printf("\n");
    free_PQ(pq);
}

int main() {
    test_heappush();
    test_larger();

    printf("Tests passed.\n");
    
    return 0;
}
