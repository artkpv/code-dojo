""" 

Finds a successor for a node in Binary Search Tree.

Author: Artyom K. <wild [dog] inbox [dot] ru

"""

#!python3


def successor(node):
    succ = node.right
    while succ and succ.left:
        succ = succ.left
    if not succ:
        x = node
        while x.parent and x.parent.left != x:
            x = x.parent
        if x.parent and x.parent.left == x:
            succ = x.parent
    return succ

class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        if left:
            left.parent = self
        self.right = right
        if right:
            right.parent = self
        self.parent = None


################  TESTS  

def test1():
    n = Node()
    root = Node(n, Node()) 
    assert successor(n) == root

test1()


def test2():
    n = Node()
    root = \
    Node(
        Node(
            Node(),
            n
            ),
        Node()
    )
    assert successor(n) == root

test2()


def test3():
    succ = Node()
    n = Node(
        Node(),
        Node(Node(succ), Node())
    )
    root = \
    Node(
        Node(
            Node(),
            n
            ),
        Node()
    )
    assert successor(n) == succ

test3()
    

print('done')
