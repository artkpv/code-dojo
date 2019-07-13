#!python3
"""

E1
5 3
5 1 4

1 2 3 4 5 
2     3 1

- 5,5 1,1 4,4 5,4
+ 4,5


E2
5 0

1 2 3 4 5 

1,1 1,2
2,1 2,2 2,3
3,2 3,3 3,4


"""
n, k = [int(i) for i in input().strip().split(' ')]
X = [int(i) for i in input().strip().split(' ')]

adj = [[] for _ in range(n+1)]
for i, cell in enumerate(X):
    if cell not in adj[cell]:
        adj[cell] += [cell]
    # add to left
    if cell > 1:
        if adj[cell-1]:
            if (cell-1, cell) not in adj[cell-1]:
                adj[cell-1] += [(cell-1, cell)]
            if (cell-1, cell) not in adj[cell]:
                adj[cell] += [(cell-1, cell)]
    # add to right
    if cell < n:
        if adj[cell+1]:
            if (cell+1, cell) not in adj[cell+1]:
                adj[cell+1] += [(cell+1, cell)]
            if (cell+1, cell) not in adj[cell]:
                adj[cell] += [(cell+1, cell)]

count = 0
for c in range(1, n+1):
    if not adj[c]:
        # (c,c), (c-1, c), (c+1, c)
        count += 3 if 1 < c < n else 2
    else:
        # (c-1,c)
        if 1 < c:
            if (c-1, c) not in adj[c]:
                count += 1
        # (c, c-1)
        if c < n:
            if (c+1, c) not in adj[c]:
                count += 1
print(count)


