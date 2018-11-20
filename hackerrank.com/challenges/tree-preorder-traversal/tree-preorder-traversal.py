
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys
def preOrder(v):
    sys.stdout.write(str(v.data) + ' ')
    if v.left:
        preOrder(v.left)
    if v.right:
        preOrder(v.right)
