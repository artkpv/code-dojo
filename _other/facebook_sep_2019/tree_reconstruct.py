#!/bin/python3

import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rebuild_tree(inorder, lorder):
    assert len(inorder) == len(lorder)
    n = len(inorder)
    def _traverse(ilo, ihi, llo, lhi):
        if ilo > ihi:
            return None
        ioi = ilo
        loi = llo
        while inorder[ioi] != lorder[loi]:
            assert loi < n
            if ioi == ihi + 1:
                ioi = ilo
                loi += 1
            else:
                ioi += 1
        node = Node(inorder[ioi])
        node.left = _traverse(ilo, ioi-1, loi+1, lhi)
        node.right = _traverse(ioi+1, ihi, loi+1, lhi)
        return node

    return _traverse(0, n-1, 0, n-1)

"""
0 1 2 3 4 5  6  7
2 4 3 5 9 8  10 11   # inorder
5 2 8 3 9 10 4  11   # level order

0 7 0 7   3 0      5
 0 2 1 7   0 1      5 2
  1 2 2 7   2 3      5 2 3 4..

 4 7 1 7

"""
class Test(object):
    def test_one(self):
        """
           5
          / \
         2   8
          \   |  \
           3   9  10
          /        \
         4          11
        """
        root = rebuild_tree(
            [2, 4, 3, 5, 9, 8, 10, 11],   # inorder
            [5, 2, 8, 3, 9, 10, 4, 11]    # level order
        )
        self.assertEqual(root.val, 5)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 8)
        n = root.left
        self.assertEqual(n.right.val, 3)
        self.assertEqual(n.right.left.val, 4)
        n = root.right
        self.assertEqual(n.left.val, 9)
        self.assertEqual(n.right.val, 10)
        self.assertEqual(n.right.right.val, 11)

unittest.main()
