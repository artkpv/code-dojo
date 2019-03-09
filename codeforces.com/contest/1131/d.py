#!python3
"""
http://codeforces.com/contest/1131/problem/D

Not solved (2019-2-28). Looks like NP-hard problem. But how to solve it via BF? Iterating candidates till they exausted?


n , m 
cmp i with j
a_ij

IDEA ?
Run detection of connected components on graph with cycles ('=' compare). And detect contradictions, bad cycles.
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

E2
3 3
>>>
<<<
>>>

E3
2 2
< >
< >

Ex4
3 2
==
=<
==

"""

n,m = [int(i) for i in input().strip().split(' ')]
comparisons = []
for i in range(n):
    comparisons += [input().strip()]

# THE BELOW IS A TRY OF IDEA 1. CC on graph. Does not work
# as it is unclear how to effectively form CC.

class UnionFind:
    def __init__(self, count):
        self.arr = [i for i in range(count)]
        self.count = count
    
    def find(self, a):
        """ Gets set id with path compression """
        while a != self.arr[a]:
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

    def unify(self):
        for i in range(self.count):
            for replace_i, replace_e in enumerate(self.arr):
                if replace_e > i:
                    self.arr[replace_i] = i
                    for j in range(replace_i + 1, len(self.arr)):
                        if self.arr[j] == replace_e:
                            self.arr[j] = i
        assert(min(self.arr) == 0)
        assert(max(self.arr) == self.count - 1)
        assert(len(set(self.arr)) == self.count)

unionfind = UnionFind(n + m)

# distinguish already connected :
# for i in range(n):
#   for j in range(m):
#       if comparisons[i][j] == '=':
#           unionfind.union(i, n + j)

order = []
marked = [False] * (n+m)
stack = [False] * (n+m)  # to detect cycles
def dfs(inx):
    """ Gets topological sort into 'order'. And detects bad cycles. """
    marked[inx] = True
    stack[inx] = True
    for i, compare in enumerate(
                      comparisons[inx] if inx < n 
                      else (row[inx] for row in comparisons)):
        other_inx = i if inx < n else n + i
        if compare = '>' or compare = '=':  # adjacent
            if not marked[other_inx]:
                dfs(other_inx)
                # if not dfs(other_inx):
                #     return False
            # elif stack[other_inx]:
                # Detect bad cycles. Like: (a1 > ... = a1) or (a1 = ... > a1) or (a1 = b1 > ... = a1) etc
                # if compare = '>':
                #     return unionfind.find(inx) != unionfind.find(other_inx)
                # elif compare = '=':
                #     return unionfind.find(inx) == unionfind.find(other_inx)
    order.append(inx)
    return True

# get reversed post order (topological order):
for inx in range(n+m):
    stack = [False] * (n+m) 
    nocycles = dfs(inx)
    if not nocycles:
        break

if not nocycles:
    print("No")
    exit()

def dfs_reversed(inx):
    """ Updates unionfind with connected components reached on this dfs run """
    marked[inx] = True
    for i, compare in enumerate(
                      comparisons[inx] if inx < n 
                      else (row[inx] for row in comparisons)):
        other_inx = i if inx < n else n + i
        if compare == '=' or compare = '<':  # reversed adjacent
            if not marked[other_inx]:
                unionfind.union(inx, other_inx)
                dfs_reversed(other_inx)

marked = [False] * (n+m)
while order:
    inx = order.pop()
    dfs_reversed(inx)

print("Yes")
print(' '.join(str(i) for i in unionfind.arr[:n]))
print(' '.join(str(i) for i in unionfind.arr[n:]))