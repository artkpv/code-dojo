
'''
Size - nodes in a tree. 
BST - tree with two children most, left - less than, right greater than.
'''

def size(n):
    if not n:
        return 0
    return n.size

def rank(n, x):
    if not n:
        return 0
    if n.key < x:
        return 1 + size(n.left) + rank(n.right, x)
    elif n.key == x:
        return size(n.left)
    return rank(n.left, x)

def contains(n, x):
    if not n:
        return False
    if n.key == x:
        return True
    elif x < n.key:
        return contains(n.left, x)
    return contains(n.right, x)

def count(n, lo, hi):
    if contains(n, hi):
        return 1 + rank(n, hi) - rank(n, lo)
    return rank(n, hi) - rank(n, lo)

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.size = size(left) + size(right) + 1

root = Node(10,
         Node(5, 
              Node(1),
              Node(7)
         ),
         Node(15,
              Node(12),
              Node(17))
         )

assert(count(root, 1, 2) == 1)
assert(count(root, 1, 17) == 7)
assert(count(root, 7, 15) == 4)
assert(count(root, -1, 0) == 0)
assert(count(root, 18, 100) == 0)
print("All tests pass")

