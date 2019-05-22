#!python3

import unittest


def reverse(head):
    x = head
    prev = None
    while x:
        next_ = x.next
        x.next = prev
        prev = x
        x = next_
    return prev


class Node(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

    def __eq__(self, other):
        return other and self.val == other.val

    def __repr__(self):
        return '<Node %s>' % str(self.val)


class ReverseLLCase(unittest.TestCase):
    def test_no_node(self):
        self.assertEqual(reverse(None), None)

    def test_one_node(self):
        self.assertEqual(reverse(Node(1)), Node(1))

    def test_two_nodes(self):
        out = reverse(Node(1, Node(2)))
        self.assertEqual(out, Node(2, Node(1)))

    def test_three_nodes(self):
        out = reverse(Node(1, Node(2, Node(3))))
        self.assertEqual(out, Node(3, Node(2, Node(1))))


if __name__ == '__main__':
    unittest.main()
