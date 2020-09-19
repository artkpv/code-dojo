#!python3
"""
NEXT: Fix test 6 (input6.txt)


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

class UnionFind:
    def __init__(self, count):
        self.arr = [i for i in range(count)]
        self.count = count

    def find(self, a):
        """ Gets set id with path compression """
        if a != self.arr[a]:
            self.arr[a] = self.find(self.arr[a])
        return self.arr[a]

    def union(self, a, b):
        """ Unions two sets """
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return
        self.arr[parent_b] = parent_a
        self.count -= 1

def dfs(v, level):  # v - vertex
    """
    Visit graph of assessments using comparision table.
    Where w adjecent of v for v > or = w.
    """
    global iscycle
    print(' ' * level, 'dfs',v)
    if iscycle:
        return
    marked[v] = True  # to mark all vertices
    visited[v] = True  # to detect cycles
    haschildren = False
    for othervertex, compare in enumerate(
                      comparisons[v] if v < firstnum
                      else (row[v-firstnum] for row in comparisons)):
        w = firstnum+othervertex if v < firstnum else othervertex
        left = v if v < firstnum else w
        right = w if w >= firstnum else v
        if ((left == v and compare == '>') or
            (right == v and compare == '<')):
            if unionfind.find(w) == unionfind.find(v):
                # in one component '=' but now with '>'
                # thus it is cycle
                iscycle = True
                break
            if not marked[w]:
                if scores[v] is not None:
                    scores[w] = scores[v] - 1
                dfs(w, level+1)
                if scores[v] is None:
                    # take number from first child if not assigned
                    scores[v] = scores[w] + 1
            else:
                if visited[w]:
                    # print('cycle found for ', v, '>', w)
                    iscycle = True
                    break
                if scores[v] is None and scores[w] is not None:
                    scores[v] = scores[w] + 1
            haschildren = True
        elif compare == '=':
            if not marked[w]:
                dfs(w, level+1)
                haschildren = True
                if scores[v] is None:
                    scores[v] = scores[w]
    visited[v] = False
    if not haschildren and scores[v] is None:
        scores[v] = 1  # a leave


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

#
# RUN
#
firstnum,secondnum = [int(i) for i in input().strip().split(' ')]
comparisons = []
for i in range(firstnum):
    comparisons += [input().strip()]

unionfind = UnionFind(firstnum + secondnum)
for i in range(firstnum):
    for j in range(secondnum):
        if comparisons[i][j] == '=':
            unionfind.union(i, firstnum + j)

scores = [None] * (firstnum+secondnum)
marked = [False] * (firstnum+secondnum)
iscycle = False

for i in range(firstnum+secondnum):
    visited = [False] * (firstnum+secondnum) # to find cycle
    dfs(i, 0)


if not iscycle:
    scores = unify(scores)
    print("Yes")
    print(' '.join(str(i) for i in scores[:firstnum]))
    print(' '.join(str(i) for i in scores[firstnum:]))
else:
    print("No")
