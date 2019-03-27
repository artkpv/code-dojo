#!python3
"""
NEXT: Implement this. But fix that it can visit leaves first and assign 1 to them. How to fix?
Run DFS, with a > b, a points to b. Vertices with '=' in one group. If cycle
then stop. Assign number when no children or by taking from child. Then 
unify.




Time:
V = 1000
E = O(500*500 = 250_000
2E + 2E ~= O(1_000_000)


----

E1
3 4
>>>>
>>>>
>>>>

Tree:
a1 > b1 
a2   b2
a3   b3


E2
3 3
>>>
<<<
>>>

E3
2 2
< >
< >
1 1
2 

Ex4
3 2
==
=<
==

Ex

"""

n,m = [int(i) for i in input().strip().split(' ')]
comparisons = []
for i in range(n):
    comparisons += [input().strip()]

# class UnionFind:
#     def __init__(self, count):
#         self.arr = [i for i in range(count)]
#         self.count = count

#     def find(self, a):
#         """ Gets set id with path compression """
#         if a != self.arr[a]:
#             self.arr[a] = self.find(self.arr[a])
#         return self.arr[a]

#     def union(self, a, b):
#         """ Unions two sets """
#         parent_a = self.find(a)
#         parent_b = self.find(b)
#         if parent_a == parent_b:
#             return
#         self.arr[parent_b] = parent_a
#         self.count -= 1

# unionfind = UnionFind(n + m)

# for i in range(n):
#     for j in range(m):
#         if comparisons[i][j] == '=':
#             unionfind.union(i, n + j)

scores = [None] * (n+m)
marked = [False] * (n+m)
iscycle = False
def dfs(i):
    global iscycle
    if iscycle:
        return
    marked[i] = True
    haschildren = False
    for other_i, compare in enumerate(
                      comparisons[i] if i < n
                      else (row[i-n] for row in comparisons)):
        j = n+other_i if i < n else other_i
        left = i if i < n else j
        right = j if j >= n else i
        if ((left == i and compare == '>') or
            (right == i and compare == '<')):
            if marked[j]:
                iscycle = True
                break
            else:
                if scores[i] is not None:
                    scores[j] = scores[i] - 1
                dfs(j)
                if scores[i] is None:
                    # take number from first child if not assigned
                    scores[i] = scores[j] + 1
            haschildren = True
        elif compare == '=':
            if not marked[j]:
                dfs(j)
                haschildren = True
                if scores[i] is None:
                    scores[i] = scores[j]
    if not haschildren:
        scores[i] = 1  # a leave or last visisted in a connected component

                
for i in range(n+m):
    dfs(i)

def unify(scores):
    auxiliary = [None] * len(scores)
    count = len(set(scores))
    next_ = min(scores)
    for i in range(1, count+1):
        for j, e in enumerate(scores):
            if e == next_:
                auxiliary[j] = i
        next_ += 1
    return auxiliary

if not iscycle:
    scores = unify(scores)
    print("Yes")
    print(' '.join(str(i) for i in scores[:n]))
    print(' '.join(str(i) for i in scores[n:]))
else:
    print("No")
