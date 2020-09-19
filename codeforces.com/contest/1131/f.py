#!python3
"""
2 <= n <= 150_000

I1

Ex1
5
1 4
2 5
3 1
4 5



"""

n = int(input().strip())
adj = [[] for _ in range(n)]
border_cat = None
for day in range(n-1):
    left, right = [int(i) for i in input().strip().split(' ')]
    left -= 1
    right -= 1
    adj[left] += [(day, right)]
    adj[right] += [(day, left)]
    for cat in left, right:
        if len(set(w for day, w in adj[cat])) == 1:
            border_cat = cat


order = []
marked = [False] * n
def dfs(v):
    if marked[v]:
        return
    marked[v] = True
    order.append(v)
    for day, w in sorted(adj[v], key=lambda i:i[0]):
        if not marked[w]:
            dfs(w)

dfs(border_cat)
print(' '.join(str(i+1) for i in order))
