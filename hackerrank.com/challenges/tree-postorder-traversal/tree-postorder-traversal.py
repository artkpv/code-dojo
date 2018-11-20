
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
from sys import stdout
def postOrder(v):
    if v.left:
        postOrder(v.left)
    if v.right:
        postOrder(v.right)
    stdout.write(str(v.data) + ' ')
