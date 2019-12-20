#!python3

from collections import deque


def bfs(g, s):
    q = deque([s])
    marked = set()
    while q:
        v = q.pop()
        marked.add(v)
        print(v)
        for w in g[v]:
            if w not in marked:
                q.append(w)

bfs([[1, 3],
     [2],
     [3],
     [0]], 0)
