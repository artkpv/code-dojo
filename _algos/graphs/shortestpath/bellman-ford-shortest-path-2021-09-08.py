'''

Given graph (directed with negative weights) and source vertex find shortest path or report negative cycle if one exists.

Example 1.
    Source: 1
    Graph:
        1: 2 4 3
        2: 4
        3: 
        4: 3
    Weights:
        1,2=3
        2,4=-3
        1,4=1
        4,3=2
        1,3=4

    1 -> 2
    | \  |
    v  v v
    3 <- 4

    Out:
    1: 2
    2: 4
    3: 
    4: 3


Example 2

    1 -> 2
      ^  |
       \ v
         3
    1,2=1
    2,3=-3
    1,3=1

    Out: None (cycle)

Example 3

    1 -> 2
      ^  | ^
       \ v |
         3

    1,2=1
    2,3=-3
    2,3=2
    1,3=4
    
    Out: None (cycle)

'''

from heapq import heappop, heappush

INF = float('inf')

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.weights = [[INF] * V for _ in range(V)]

    def add(self, v, u, w):
        assert v < self.V
        assert u < self.V
        assert 0 <= u and 0 <= v
        self.adj[v] += [u]
        self.weights[v][u] = w

    def __str__(self):
        return f'<Graph {self.adj} {self.weights} >'

class MQ:
    def __init__(self):
        self._a = []
        self._d = {}

    def enqueue(self, w, v):
        if v in self._d:
            del self._a[self._a.index((self._d[v], v))]
        heappush(self._a, (w, v))
        self._d[v] = w

    def dequeue(self):
        v = heappop(self._a)[1]
        del self._d[v]
        return v

    def size(self):
        return len(self._a)

def bellman_ford_sp(graph, source):
    edgeto = [None] * graph.V
    distto = [INF] * graph.V
    distto[source] = 0
    def has_cycle():
        adj = [[] for _ in range(graph.V)]
        for i, e in enumerate(edgeto):
            if e is not None:
                adj[e] += [i]
        marked = set()
        stack = set()
        def _has_cycle(v):
            if v in marked:
                return False
            marked.add(v)
            for u in adj[v]:
                if u in stack:
                    return True
                stack.add(u)
                if _has_cycle(u):
                    return True
                stack.remove(u)
            return False
        for v in range(graph.V):
            stack.clear()
            stack.add(v)
            if _has_cycle(v):
                return True
        return False

    q = MQ()
    q.enqueue(0, source)
    counter = 0
    while q.size() > 0:
        if counter % graph.V == 0:
            if has_cycle():
                return None 
        counter += 1
        v = q.dequeue()
        for u in graph.adj[v]:
            d = distto[v] + graph.weights[v][u]
            if d < distto[u]:
                edgeto[u] = v
                distto[u] = d
                q.enqueue(d, u)
    return edgeto

def myassert(graph, source, expected):
    print(f'TEST: {graph} graph, {source} source')
    r = bellman_ford_sp(graph, source)
    assert r == expected, f' result {r}, expected: {expected}'
    print("PASS")

graph = Graph(4)
graph.add(0, 1, 3)
graph.add(0, 3, 1)
graph.add(0, 2, 4)
graph.add(1, 3, -3)
graph.add(3, 2, 2)
myassert(graph, 0, [None, 0, 3, 1])

graph = Graph(3)
graph.add(0, 1, 1)
graph.add(1, 2, -3)
graph.add(2, 0, 1)
myassert(graph, 0, None)

graph = Graph(4)
graph.add(0, 1, 1)
graph.add(1, 2, -3)
graph.add(2, 3, 1)
graph.add(3, 0, 1)
myassert(graph, 0, [None, 0, 1, 2])

graph = Graph(1)
myassert(graph, 0, [None])
