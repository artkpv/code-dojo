#!python3

import sys

sys.setrecursionlimit(1024*2)


class Node(object):
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


class BT(object):
    def __init__(self, count):
        assert count > 0
        self._nodes = [None] * count
        self._root = Node(1)
        self._nodes[0] = self._root

    def _get_node(self, num):
        if not self._nodes[num-1]:
            self._nodes[num-1] = Node(num)
        return self._nodes[num-1]

    def add(self, node_num, left, right):
        root = self._get_node(node_num)
        if left:
            root.left = self._get_node(left)
        if right:
            root.right = self._get_node(right)

    def _inorder(self, node, depth, k):
        if depth % k == 0:
            node.left, node.right = node.right, node.left
        if node.left:
            self._inorder(node.left, depth+1, k)
        print(node.num, end=' ')
        if node.right:
            self._inorder(node.right, depth+1, k)

    def swap_print(self, k):
        self._inorder(self._root, 1, k)
        print('')


n = int(input('').strip())
tree = BT(n)
for node in range(1, n+1):
    left, right = [int(i) for i in input('').strip().split(' ')]
    left = left if left != -1 else None
    right = right if right != -1 else None
    tree.add(node, left, right)

for query in range(int(input('').strip())):
    k = int(input('').strip())
    tree.swap_print(k)
