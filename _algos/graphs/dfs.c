#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#define VERTICES 6

int g[][VERTICES] = 
{
 {0, 0, 0, 0, 0},
 {2, 3, 4, 0, 0},
 {1, 3, 4, 0, 0},
 {1, 2, 4, 0, 0},
 {1, 2, 3, 0, 0},
 {6, 0, 0, 0, 0},
 {5, 0, 0, 0, 0},
};

int marked[VERTICES + 1];
int onstack[VERTICES + 1];

void dfs(int v)
{
    if (marked[v]) 
        return; 
    marked[v] = 1;
    onstack[v] = 1;
    printf("%d ", v);
    int i;
    for (i = 0; i < VERTICES && g[v][i] != 0; ++i) 
    {
        int w = g[v][i];
        if (onstack[w])
        {
            printf("BE:%d-%d ", v, w);
            continue;
        }
        if (marked[w])
        {
            printf("CFE:%d-%d ", v, w);
            continue;
        }
        printf("TE:%d-%d ", v, w);
        dfs(w);
    }
    onstack[v] = 0;
}

int main() 
{
    printf("Prints DFS edges \n TE - tree edge\n BE - back edge\n CFE - cross or forward edge\n");
    int i;
    for (i = 0; i < VERTICES+1; ++i) 
        marked[i] = 0;

    int source;
    for (source = 1; source <= VERTICES; ++source) {
        for (i = 0; i < VERTICES+1; ++i) 
            onstack[i] = 0;
        dfs(source);
    }
    printf("\n");
    return 0;
}
