"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
from sys import stdout
def inOrder(v):
    if v.left:
        inOrder(v.left)
    stdout.write(str(v.data) + ' ')
    if v.right:
        inOrder(v.right)

