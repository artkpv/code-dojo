#!python3

from heapq import heappush, heappop
from collections import deque

def mst_kruskal(graph, weights):
    pq = []
    for v in range(len(graph)):
        for w in range(v):
            f, t = sorted([v, w])
            assert (t, f) not in weights
            assert (f, t) in weights
            heappush(pq, (weights[(f, t)], v, w))
    mst = [[] for _ in range(len(graph))]
    marked = set()
    while pq:
        ew, v, w = heappop(pq)
        if v not in marked or w not in marked:
            mst[w].append(v)
            mst[v].append(w)
            marked.add(w)
            marked.add(v)
    return mst


def levelorder(mst):
    marked = set()
    array = []
    q = deque()
    q.append(0)
    marked.add(0)
    while q:
        v = q.pop()
        array.append(v)
        for w in mst[v]:
            if w not in marked:
                marked.add(w)
                q.append(w)
    return array


mst1 = mst_kruskal([
        [1, 2, 3, 4],   # 0
        [0, 2, 3, 4],   # 1
        [0, 1, 3, 4],
        [0, 1, 2, 4],
        [0, 1, 2, 3]
    ], { 
        (0, 1): 10, (0, 2): 1, (0, 3): 10, (0, 4): 1,   # Equals to (1, 0), ... 
        (1, 2): 1, (1, 3): 10, (1, 4): 10, 
        (2, 3): 1, (2, 4): 10, 
        (3, 4): 10
    })

"""
0   1   2   3   4
  -                  10
  -----              1
  ---------          10
  -------------      1
      -              1
      -----          10
      ----------     10
          -          1
          -----      1
               -     10

MST:
     0
  4     2
      3   1
        
 
"""

ordered = levelorder(mst1)
print(mst1)
print(ordered)
assert ordered == [0, 4, 2, 3, 1]
print('done')
