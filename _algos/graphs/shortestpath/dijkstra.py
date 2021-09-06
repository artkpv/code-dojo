
from heapq import heapify, heappop, heappush

INF = float('inf')
adj = [
    [1, 2, 3],
    [2, 3],
    [3],
    []
]
W = [
    [INF, 1, 3, 4],
    [INF, INF, 5, 6],
    [INF, INF, INF, 1],
    [INF, INF, INF, INF],
]

def weights(v, u):
    return W[v][u]

class MQ:
    def __init__(self):
        self.q = []

    def enqueueOrDecrease(self, v, d):
        for i, (d, u) in enumerate(self.q):
            if u == v:
                self.q[i] = (d, v)
                break
        else:
            self.q.append((d, v))
        heapify(self.q)

    def dequeue(self):
        if self.q:
            t = heappop(self.q)
            print(t)
            return t[1]
        return None

    def size(self):
        return len(self.q)

    def __str__(self):
        return str(self.q)



V = len(adj)

def dijkstra(source):
    q = MQ()
    edgeto = dict()
    distto = dict((v, INF) for v in range(V))
    distto[source] = 0
    q.enqueueOrDecrease(source, 0)
    while q.size()>0:
        print(str(q))
        v = q.dequeue()
        print(v)
        for u in adj[v]:
            d = distto[v] + weights(v, u)
            if d < distto[u]:
                distto[u] = d
                edgeto[u] = v
                q.enqueueOrDecrease(u, d)
    print(edgeto)
    print(distto)


dijkstra(0)
