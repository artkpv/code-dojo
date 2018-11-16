#include "vector.c"
#include <time.h>
#include <windows.h> 

int
equals(void * a, void * b) {
	int cmp = *((int*)a) - *((int*)b);
	if (cmp == 0)
		return 1;
	return 0;
}

void
v_print(VectorPtr v) {
	printf("Vector: size %d, count %d:\n", v->size, v->count);
	for (int i = 0; i < v->count; i++) {
		printf("%d ", *((int *)(v->arr[i])));
	}
	printf("\n");
}

int
test_adds_deletes() {
	VectorPtr v = Vector_ctor(sizeof(int));
	for (int i = 1; i < 10; i++) {
		int * ip = malloc(sizeof(int));
		*ip = i;
		v_add(v, ip);
		assert(v->count == i);
	}
	// printf(" after add:\n");
	// v_print(v);

	int deleted = 0;
	int before = v->count;
	for (int i = 1; i < 10; i++) {
		v_delete(v, &i, (int (*) (void *, void *)) equals);
		deleted++;
		assert(v->count == before - deleted);
	}
	// printf(" after delete:\n");
	// v_print(v);
	assert(v->count == 0);

	Vector_free(v);
	return 1;
}

int 
resizing_perf() {
	VectorPtr v = Vector_ctor(sizeof(int));

	int n = 1e5;  // on 1e9 breaks

	clock_t start = clock();
	for (int i = 1; i <= n; i++) {
		int * ip = malloc(sizeof(int));
		*ip = i;
		v_add(v, ip);
		assert(v->count == i);
	}
    double dur = 1000.0*(clock()-start)/CLOCKS_PER_SEC;
	printf("adding %d took: %.f ms\n", n, dur);

	start = clock();
	int deleted = 0;
	while (v->count > 0) {
		v_delete_at(v, 0);
		deleted++;
		assert(v->count == n - deleted);
	}
    dur = 1000.0*(clock()-start)/CLOCKS_PER_SEC;
	printf("deleting %d took: %.f ms", deleted, dur);

	Vector_free(v);
	return 1;
}

void
main() {
	assert(test_adds_deletes() == 1);
	printf("done test_adds_delete\n");
	assert(resizing_perf() == 1);
}
