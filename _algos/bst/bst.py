#!python3

"""
Binary Search Tree. With Hibbard's deletion. Not balanced.
"""

import unittest


class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def put(self, key):
        self.root = self._put(self.root, key)

    def _put(self, x, key):
        if x is None:
            return Node(key)
        if key < x.key:
            x.left = self._put(x.left, key)
        elif x.key < key:
            x.right = self._put(x.right, key)
        else:
            x.key = key
        return x

    def inorder(self, n=None):
        if not n:
            n = self.root
        if n.left:
            yield from self.inorder(n.left)
        yield n.key
        if n.right:
            yield from self.inorder(n.right)

    def preorder(self, n=None):
        if not n:
            n = self.root
        if not n:
            return None
        yield n.key
        if n.left:
            yield from self.preorder(n.left)
        if n.right:
            yield from self.preorder(n.right)

    def __repr__(self):
        r = []
        def printer(lvl, n):
            if not n:
                return
            if n.right:
                printer(lvl+1, n.right)
            r.append((' ' * lvl) + str(n.key))
            if n.left:
                printer(lvl+1, n.left)
        printer(0, self.root)
        return '<BST:\n' + '\n'.join(r) + '\n>'

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, n, key):
        """ Hibbard's eager deletion """
        if n.key > key:
            n.left = self._delete(n.left, key)
            return n
        elif n.key < key:
            n.right = self._delete(n.right, key)
            return n
        # Found. Delete:
        if not n.left and not n.right:
            return None
        elif not n.left or not n.right:
            return n.left or n.right
        # Has left and right.
        t = n
        n = self.min(t.right)
        n.right = self.delete_min(t.right)
        n.left = t.left
        return n

    def min(self, n=None):
        if not n:
            n = self.root
        while n.left:
            n = n.left
        return n

    def delete_min(self, n):
        if n and n.left:
            n.left = self.delete_min(n.left)
            return n
        return n.right if n else None


class Tests(unittest.TestCase):
    def test_deletion(self):
        """
             5
          2     7
         1 3   6  10
                 9  11
        """
        bst = BST()
        preorder = [5, 2, 1, 3, 7, 6, 10, 9, 11]
        for v in preorder:
            bst.put(v)
        print('Before', bst)
        self.assertEqual(list(bst.preorder()), preorder)
        bst.delete(7)
        self.assertEqual(list(bst.preorder()), [5, 2, 1, 3, 9, 6, 10, 11], repr(bst))
        bst.delete(9)
        self.assertEqual(list(bst.preorder()), [5, 2, 1, 3, 10, 6, 11], repr(bst))
        bst.delete(10)
        self.assertEqual(list(bst.preorder()), [5, 2, 1, 3, 11, 6], repr(bst))
        bst.delete(11)
        self.assertEqual(list(bst.preorder()), [5, 2, 1, 3, 6], repr(bst))
        bst.delete(6)
        self.assertEqual(list(bst.preorder()), [5, 2, 1, 3], repr(bst))
        bst.delete(2)
        self.assertEqual(list(bst.preorder()), [5, 3, 1], repr(bst))
        bst.delete(3)
        self.assertEqual(list(bst.preorder()), [5, 1], repr(bst))
        bst.delete(5)
        self.assertEqual(list(bst.preorder()), [1], repr(bst))
        bst.delete(1)
        self.assertEqual(list(bst.preorder()), [], repr(bst))


unittest.main()
