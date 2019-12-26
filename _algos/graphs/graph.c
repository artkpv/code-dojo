// TODO
#include <stdio.h>

struct adj_n {
	int w;
	adj_n * next;
};

typedef struct graph_t {
	int vertices;
	int edges;
	adj_n * adj;
} Graph;

typedef Graph * GraphPtr;

GraphPtr 
Graph_ctor(int vertices) {
	GraphPtr g = (GrapthPtr) malloc(sizeof(Graph));
	g->vertices = vertices;
	g->edges = 0;
	adj_n * arr = (adj_n*) calloc(vertices, sizeof(adj_n));
	g->adj_n = arr;
}

void
Graph_free(GraphPtr g) {
	if (g != NULL) {
		if (g->adj != NULL) {
			for (int i = 0; i < g->vertices; i++) {
				adj_n * x = g->adj[i];
				while (x != NULL) {
					t = x->next;
					free(x);
					x = t;
				}
			}
			free(g);
		}
	}
}

void
add_edge(GraphPtr g, int v, int w) {
	assert(g->vertices > v);
	assert(g->vertices > w);

	adj_n * x = g->adj[v];
	adj_n * x2 = (adj_n *) malloc(sizeof(adj_n));
	x2->next = x;
	x2-> = 
	g->adj[v] = x2;
}

adj_n * 
g_adj(GraphPtr g, int v) {
	return g->adj[v];
}


int test_iter_adj() {
	int v = 10;
	GraphPtr g = Graph_ctor(v);
	add_edge(g, 0, 1);
	return 1;
}

void main() {
	assert(test_iter_adj() == 1);
}

