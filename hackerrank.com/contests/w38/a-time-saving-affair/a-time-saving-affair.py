#!python3

import heapq

INF = 10**15

class V:
    def __init__(self, junction, color, seconds):
        self.j = junction
        self.c = color
        self.s = seconds

    def __lt__(self, other):
        return self.s < other.s

class G:
    def __init__(self, roads, n):
        global INF
        self.roads = roads
        self.vertices = [None] * n
        for i in range(n):
            self.vertices[i] = V(i, '', INF)

    def vertex(self, i):
        return self.vertices[i]

    def adj(self, v):
        return self.roads[v.j]


class LeastTimeRoad:
    def __init__(self, g, n, k):
        self.g = g
        self.n = n
        self.k = k
        self.bfs()

    def bfs(self):
        v = self.g.vertex(0)
        v.s = 0
        q = [v]
        while len(q) > 0:
            v = heapq.heappop(q)
            is_red = (v.s // self.k) % 2 == 1
            if is_red and v.j != self.n-1:
                v.s += (k - (v.s % self.k))
                heapq.heappush(q, v)
            else:  # green
                for road in g.adj(v):
                    u = g.vertex(road[0])
                    seconds = v.s + road[1]
                    if u.s > seconds:
                        u.s = seconds
                        heapq.heappush(q, u)

    def mintime(self):
        return self.g.vertex(self.n - 1).s


n = int(input().strip())
k = int(input().strip())
m = int(input().strip())

roads = [None] * n
for road in range(m):
    j1, j2, t = [int(i) for i in input().strip().split(' ')]
    j1 -= 1
    j2 -= 1
    if roads[j1] == None:
        roads[j1] = list()
    roads[j1] += [(j2, t)]
    if roads[j2] == None:
        roads[j2] = list()
    roads[j2] += [(j1, t)]

g = G(roads, n)
ltr = LeastTimeRoad(g, n, k)
print(ltr.mintime())
