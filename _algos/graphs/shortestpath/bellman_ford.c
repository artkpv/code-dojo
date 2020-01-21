/*
 *
 * Bellman-Ford shortest path algorithm.
 *
 * Author: Artyom K. <w1ld [dog] inbox [dot] ru>
 *
 * TODO:
 * - Use VLA (see branch 'bellmanford_c_vla') and make several tests.
 * - Make queue-based version.
 * - Make cycle detection on DFA.
 *
 */
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

#define INF 999999

#define V 5

int graph[][V+1] = {
//           1    2    3    4    5
    { INF, INF, INF, INF, INF, INF },
    { INF, INF,   4,   3,   2, INF },  // 1
    { INF, INF, INF,  -8,   9, INF },  // 2
    { INF, INF, INF, INF,   4, INF },  // 3
    { INF, INF, INF, INF, INF,   2 },  // 4
    { INF, INF, INF, INF,  -3, INF }   // 5. Negative cycle.
};

int * distto = NULL;

int * edgeto = NULL;

int * path = NULL;

int has_negative_cycle = 0;

int find_cycle();

int* bfsp(int source, int target) {
    // Initialize.
    distto = (int*) realloc(distto, sizeof(int) * V+1);
    edgeto = (int*) realloc(edgeto, sizeof(int) * V+1);
    int i;
    for (i = 0; i < V+1; ++i) {
        distto[i] = INF;
        edgeto[i] = INF;
    }
    distto[source] = 0;

    // Relax.
    for (i = 0; i < V; ++i) {
        int v;
        for (v = 1; v <= V; ++v) {
            int w;
            for (w = 1; w <= V; ++w) {
                if (graph[v][w] == INF)
                    continue;
                if (distto[w] > distto[v] + graph[v][w]) {
                    distto[w] = distto[v] + graph[v][w];
                    edgeto[w] = v;
                }
            }
        }
    }
    
    // Has negative cycle?
    has_negative_cycle = find_cycle();
    if (has_negative_cycle)
        return NULL;

    // Reconstruct.
    path = (int*) realloc(path, sizeof(int) * (V+1));  // 0 ended.
    for (i = 0; i < V+1; ++i)
        path[i] = 0;
    int x = target;
    i = 0;
    while (edgeto[x] != INF) {
        path[i] = x;
        x = edgeto[x];
        i += 1;
    }
    path[i] = x;
    return path;
}

int find_cycle() {
    int v;
    for (v = 1; v <= V; ++v) {
        int w;
        for (w = 1; w <= V; ++w) {
            if (graph[v][w] == INF)
                continue;
            if (distto[w] > distto[v] + graph[v][w])
                return 1;
        }
    }
    return 0;
}

int main() {
    int * path = bfsp(1, 4);
    if (has_negative_cycle)
        printf("Negative cycle\n");
    else {
        printf("Path: ");
        while (*path != 0)
            printf("%d ", *(path++));
        printf("\n");
    }
    return 0;
}
