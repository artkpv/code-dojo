'''


  
'''

def size(n):
    if not n:
        return 0
    return n.size

def rank(k, n):
    if not n:
        return 0
    if n.k == k:
        return size(n.l)
    elif n.k < k:
        return size(n.l) + 1 + rank(k, n.r)
    return rank(k, n.l)

def select(r, n):
    if not n:
        return -1
    nr = size(n.l)
    if r == nr:
        return n.k
    elif r < nr:
        return select(r, n.l)
    return select(r - 1 - size(n.l), n.r)

class Node:
    def __init__(self, k, l=None, r=None):
        self.l = l
        self.r = r
        self.k = k
        self.size = 1 + size(l) + size(r)

'''
      5
   3       7
 1  4     6  8
'''
root = Node(
    5,
    Node(
        3,
        Node(1),
        Node(4)
    ),
    Node(
        7,
        Node(6),
        Node(8)
    )
)

assert rank(4, root) == 2
assert rank(6, root) == 4, rank(6, root)
assert rank(8, root) == 6
assert rank(1, root) == 0

assert select(2, root) == 4
assert select(4, root) == 6
assert select(6, root) == 8
assert select(0, root) == 1
assert select(10, root) == -1
print('hooray')
