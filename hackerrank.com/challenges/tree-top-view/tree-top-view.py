#!python3
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

from sys import stdout

def topView(root):
    view = [root]
    v = root.left
    while v:
        view.insert(0, v)
        v = v.left
    v = root.right
    while v:
        view.append(v)
        v = v.right
    print(' '.join(str(i.data) for i in view))
