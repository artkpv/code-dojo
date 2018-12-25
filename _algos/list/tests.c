#include "vector.c"
#include <time.h>
#include <windows.h> 

int equals(void * a, void * b) {
	int cmp = *((int*)a) - *((int*)b);
	if (cmp == 0)
		return 1;
	return 0;
}

void v_print(VectorPtr v) {
	printf("Vector: size %d, count %d:\n", v->size, v->count);
	for (int i = 0; i < v->count; i++) {
		printf("%d ", *((int *)(v->arr[i])));
	}
	printf("\n");
}

int test_adds_deletes() {
	VectorPtr v = Vector_ctor();
	for (int i = 1; i < 10; i++) {
		int * ip = (int*) malloc(sizeof(int));
		*ip = i;
		v_push(v, ip);
		assert(v->count == i);
	}
	// printf(" after add:\n");
	// v_print(v);

	int deleted = 0;
	int before = v->count;
	for (int i = 1; i < 10; i++) {
		v_delete(v, &i, (int (*) (const void *, const void *)) equals);
		deleted++;
		assert(v->count == before - deleted);
	}
	// printf(" after delete:\n");
	// v_print(v);
	assert(v->count == 0);

	Vector_free(v);
	return 1;
}

int resizing_perf() {
	VectorPtr v = Vector_ctor();

	int n = 1e3;  // on 1e9 breaks

	clock_t start = clock();
	for (int i = 1; i <= n; i++) {
		int * ip = (int*) malloc(sizeof(int));
		*ip = i;
		v_push(v, ip);
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
	// printf("deleting %d took: %.f ms\n", deleted, dur);

	Vector_free(v);
	return 1;
}

int intcmp (int* left, int * right) {
	return *left - *right;
}

int put_various_objects_test() {
	Vector * v = Vector_ctor();
	v_push(v, "1");
	v_push(v, "2");
	int third_el = 3;
	v_push(v, &third_el);
	assert(v->count == 3);
	assert(strcmp(v_get_at(v, 0), "1") == 0);
	assert(strcmp(v_get_at(v, 1), "2") == 0);
	int * found = (int*)v_get_at(v, 2);
	assert(*found == 3);
	v_delete(v, "1", (int (*)(const void*, const void*)) strcmp);
	v_delete(v, "2", (int (*)(const void*, const void*)) strcmp);
	v_delete(v, &third_el, (int (*)(const void*, const void*)) intcmp);
	Vector_free(v);
	return 1;
}

int main() {
	assert(test_adds_deletes() == 1);
	printf("Done test_adds_delete\n");
	assert(resizing_perf() == 1);
	printf("Done resizing_perf\n");
	assert(put_various_objects_test() == 1);
	printf("Done put_various_objects_test\n");

	printf("Tests done. Press any key.\n");
	getc(stdin);
	return 0;
}
