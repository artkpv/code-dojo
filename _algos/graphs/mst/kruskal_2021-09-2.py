
'''
MST. Kruskal's algo.

given graph
take each edge (v, u) in asc order
    if v in 


        
Time: E*log(E) 
Space: V
'''

def kruskal(edges, vertices):
    mst = [[] for _ in range(vertices)]
    marked = set()
    def add(edge, v):
        marked.add(v)
        mst[v].append(edge.other(v))
        mst[edge.other(v)].append(v)
    for e in sorted(edges, key=lambda x: x.weight):
        if e.u not in marked:
            add(e, e.u)
        if e.v not in marked:
            add(e, e.v)
    return mst


class Edge():
    def __init__(self, v, u, weight):
        self.v = v
        self.u = u
        self.weight = weight

    def other(self, v):
        if self.v == v:
            return self.u
        if self.u == v:
            return self.v
        raise Exception()


edges = [
    Edge(0, 1, 1),
    Edge(1, 2, 3),
    Edge(2, 3, 3),
    Edge(0, 3, 1),
    Edge(0, 2, 1),
]
result = kruskal(edges, 4)

print(result)

