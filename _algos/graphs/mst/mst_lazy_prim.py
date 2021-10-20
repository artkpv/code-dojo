'''

Lazy Prim's algo

Given G graph find MST.

create min queue by weight of edges
relax some first vertex
while q not empty
    pop edge
    put it into mst
    for other vertex just added relax it 

relax vertex v:
    for each edge v,u
        if u not in the tree
            add to queue this edge


T: E*log(E)
S: V+V
'''

from heapq import heappop, heappush
def prim_mst(adj, weights, V, E):
    q = []
    marked = set()
    def relax(v):
        for u in adj[v]:
            if u in marked:
                continue
            heappush(q, (weights[(v,u)], v, u))
    marked.add(1)
    relax(1)
    mst = [None] * (V+1)
    while q:
        _, v, u = heappop(q)
        if v in marked and u in marked:
            continue
        v, u = (v, u) if v in marked else (u, v)
        assert u not in marked
        assert v in marked
        mst[u] = v
        marked.add(u)
        relax(u)
    return mst

res = prim_mst([
    None,
    [2,3,4],
    [3,4],
    [4],
    []
], {
    (1,2):1, (1,3):1, (1,4):1,
    (2,3):2, (2,4):2,
    (3,4):3
}, 4, 6)
print(res)


res = prim_mst([
    None,
    [2,3,4],
    [3,4],
    [4],
    []
], {
    (1,2):1, (1,3):2, (1,4):2,
    (2,3):1, (2,4):2,
    (3,4):1
}, 4, 6)
print(res)
