#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

// Resizing collection
// Next: 
// - impl pop and dequeue

typedef struct vector_t {
	int size;
	int count;
	void ** arr;
} Vector;

typedef Vector * VectorPtr;

VectorPtr 
Vector_ctor() {
	VectorPtr vector = malloc(sizeof(Vector));
	vector->size = 1;
	vector->count = 0;
	vector->arr = (void **)calloc(vector->size, sizeof(void *));
	return vector;
}

void
_arr_free(void ** arr, int n, int free_elems) {
	if (arr != NULL) {
		if (free_elems == 1) {
			for (int i = 0; i < n; i++) {
				if (*(arr + i) != NULL)
					free(*(arr + i));
			}
		}
		free(arr);
	}
}

void 
Vector_free(VectorPtr v) {
	if (v != NULL) {
		_arr_free(v->arr, v->count, 1);
		free(v);
	}
}

void
v_resize(VectorPtr v, int newsize) {
	assert(v->count <= newsize);
	void ** arr = calloc(newsize, sizeof(void *));
	for (int i = 0; i < v->count; i++)
		arr[i] = v->arr[i];
	_arr_free(v->arr, v->count, 0);
	v->arr = arr;
	v->size = newsize;
}

void
v_add(VectorPtr v, void* el) {
	if (v->size == v->count) {
		v_resize(v, v->size * 2);
	}

	v->arr[v->count] = el;
	v->count++;
}

void
v_delete_at(VectorPtr v, int inx) {
	assert(v->count > inx);
	for (int i = inx; i < v->count-1; i++) {
		v->arr[i] = v->arr[i + 1];
	}
	v->count--;
	if (v->count * 4 <= v->size) {
		v_resize(v, v->size / 2);
	}
}

int 
v_delete(VectorPtr v, void* el, int (*equals)(void* a, void* b)) {
	for (int i = 0; i < v->count; i++) {
		if ((*equals)(v->arr[i], el) == 1) {
			v_delete_at(v, i);
			return 1;
		}
	}
	return 0;
}
