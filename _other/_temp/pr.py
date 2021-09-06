'''

    
'''
full = 0
empty = N

def producer():
    while True:
        wait_for_message()
        item = produce()
        send_to_consumers(item)

        
def consumer():
    for i in range(N):
        send(producer, null)
    while True:
        wait_for_message()
        item = receive()
        send(producer, empty)
        consume(item)


full 0
empty n
buffer 

producer
full 1
empty n-1
buffer 1

consumer
full 0
buffer 
empty n

... 

from heapq import heappush, heappop
from collections import defaultdict, deque
from enum import Enum


adj = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
]
V = len(adj)
W = defaultdict(lambda: defaultdict(lambda: float('inf')))
W[0][1] = 1
W[0][2] = 3
W[0][3] = 4
W[1][2] = 1
W[1][3] = 3
W[2][3] = 1


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


'''
MST: Prim's algo
'''

def prim(adj, weight, s):
    Q = []
    marked = set()
    edgeto = [None] * len(adj)
    def visit(v):
        marked.add(v)
        for u in adj[v]:
            if u in marked:
                continue
            heappush(Q, (weight(v, u), v, u))
    visit(s)
    while Q:
        print(Q)
        _, v, u = heappop(Q)
        if v in marked and u in marked:
            continue
        edgeto[u] = v
        if v not in marked:
            visit(v)
        if u not in marked:
            visit(u)
    return edgeto


def weight(u, v):
    return W[u][v]

edgeto = prim(adj, weight, 0)
print(edgeto)

exit()



def dfs():
    '''
    Depth first search. Iterates all nodes visiting closest nodes 
    first.
    '''
    q = deque()
    q.append(0)
    color = [Color.WHITE] * len(adj)
    color[0] = Color.GRAY
    while q:
        v = q.popleft()
        color[v] = Color.BLACK
        print(v)
        print(color)
        for u in adj[v]:
            if color[u] == Color.WHITE:
                color[u] = Color.GRAY
                q.append(u)


dfs()


def lazyP(source):
    marked = set()
    pq = []
    edgeto = [None] * V
    def visit(v):
        marked.add(v)
        for u in adj[v]:
            heappush(pq, (W[v][u], v, u))
    visit(source)
    while pq:
        _, v, u = heappop(pq)
        if v in marked and u in marked:
            continue
        edgeto[u] = v
        if v not in marked:
            visit(v)
        if u not in marked:
            visit(u)
    return edgeto

# print(lazyP(0))

def ts():
    order = []
    marked = set()
    def visit(v):
        if v in marked:
            return
        marked.add(v)
        for u in adj[v]:
            visit(u)
        order.append(v)
    for v in range(V):
        visit(v)
    return list(reversed(order))

# print(ts())
