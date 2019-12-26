#!python3

"""
Ternary Search Trie
"""

class Node:
    def __init__(self, ch):
        self.left = None
        self.right = None
        self.middle = None
        self.value = None
        self.ch = ch

class TST:
    def __init__(self, R):
        self.nodes = [None] * R
        self.R = R

    def _char_at(self, key, i):
        ch = ord(str.lower(key[0])) - ord('a')
        ch %= self.R
        return ch

    def _put(self, node, key, i, value):
        if node == None:
            node = Node(key[i])
        if i == len(key) - 1:
            node.value = value
            return node
        elif key[i] < node.ch:
            node.left = self._put(node.left, key, i, value)
        elif key[i] > node.ch:
            node.right = self._put(node.right, key, i, value)
        else:  # ch == key[i]
            node.middle = self._put(node.middle, key, i+1, value)
        return node

    def put(self, key, value):
        if not key:
            return
        ch = self._char_at(key, 0)
        self.nodes[ch] = self._put(self.nodes[ch], key, 0, value)

    def search(self, key):
        ch = self._char_at(key, 0)
        return self._search(self.nodes[ch], key, 0)

    def _search(self, node, key, i):
        if node != None:
            if i == len(key) - 1:
                return node.value
            elif key[i] < node.ch:
                return self._search(node.left, key, i)
            elif key[i] > node.ch:
                return self._search(node.right, key, i)
            else:  # ch == key[i]
                return self._search(node.middle, key, i+1)
        return None

    def _inorder(self, arr, node, s):
        if node == None:
            return
        self._inorder(arr, node.left, s)
        if node.value:
            arr += [(''.join(s + [node.ch]), node.value)]
        self._inorder(arr, node.middle, s + [node.ch])
        self._inorder(arr, node.right, s)

    def inorder(self, arr):
        for i,e in enumerate(self.nodes):
            self._inorder(arr, e, [])

    def print(self):
        arr = []
        self.inorder(arr)
        print(arr)


if __name__ == '__main__':
    radix = ord('z') - ord('a') + 1
    tst = TST(radix)
    tst.put('she', 1)
    assert(tst.search('she') == 1)
    tst.put('shell', 2)
    assert(tst.search('shell') == 2)
    assert(tst.search('shel') == None)
    tst.put('abc', 3)
    assert(tst.search('a') == None)
    assert(tst.search('ab') == None)
    assert(tst.search('abc') == 3)
    tst.print()
