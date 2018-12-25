/*
 Collection based on resizing array
*/ 
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

typedef struct vector_t {
	int size;
	int count;
	const void ** arr;
} Vector;

typedef Vector * VectorPtr;

VectorPtr Vector_ctor();

void Vector_free(VectorPtr v);

void v_push(VectorPtr v, const void* el);

void v_delete_at(VectorPtr v, int inx);

int v_delete(VectorPtr v, const void* el, int (*equals)(const void* a, const void* b));


VectorPtr Vector_ctor() {
	VectorPtr vector = (VectorPtr) malloc(sizeof(Vector));
	vector->size = 1;
	vector->count = 0;
	vector->arr = (const void **)calloc(vector->size, sizeof(const void *));
	return vector;
}

void _arr_free(const void ** arr, int n, int free_elems) {
	if (arr != NULL) 
		free(arr);
}

void Vector_free(VectorPtr v) {
	if (v != NULL) {
		_arr_free(v->arr, v->count, 0);
		free(v);
	}
}

void v_resize(VectorPtr v, int newsize) {
	assert(v->count <= newsize);
	const void ** arr = (const void**) calloc(newsize, sizeof(const void *));
	for (int i = 0; i < v->count; i++)
		arr[i] = v->arr[i];
	_arr_free(v->arr, v->count, 0);
	v->arr = arr;
	v->size = newsize;
}

const void * v_get_at(VectorPtr v, int i) {
	assert(v != NULL);
	assert(v->count > i);
	return v->arr[i];
}

void v_push(VectorPtr v, const void* el) {
	if (v->size == v->count) {
		v_resize(v, v->size * 2);
	}

	v->arr[v->count] = el;
	v->count++;
}

void v_delete_at(VectorPtr v, int inx) {
	assert(v->count > inx);
	for (int i = inx; i < v->count-1; i++) {
		v->arr[i] = v->arr[i + 1];
	}
	v->count--;
	if (v->count * 4 <= v->size) {
		v_resize(v, v->size / 2);
	}
}

int v_delete(VectorPtr v, const void* el, int (*equals)(const void* a, const void* b)) {
	for (int i = 0; i < v->count; i++) {
		if ((*equals)(v->arr[i], el) == 1) {
			v_delete_at(v, i);
			return 1;
		}
	}
	return 0;
}
