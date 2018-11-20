#include <stdio.h>
#include <assert.h>
#include "graph.c"

int test_iter_adj() {
	int v = 10;
	GraphPtr g = Graph_ctor(v);
	add_edge(g, 0, 1);
	return 1;
}

void main() {
	assert(test_iter_adj() == 1);
}

