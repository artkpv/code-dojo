'''
Trie:
- Three children: less, equal, greater
- Node - a char
- Stops when all chars found or miss

Given n strings, of w width, R radix.
Time: search O(w), insert ~w
Space: R*w .. R*w*n
'''


class Trie:
    class Node:
        def __init__(self, c):
            self.l = None
            self.m = None
            self.r = None
            self.c = c
            self.count = 0

    def __init__(self):
        self.root = None

    def insert(self, s):
        if not s:
            return
        def _insert(i, n):
            if i >= len(s):
                return n
            if not n:
                n = Trie.Node(s[i])
            if n.c == s[i]:
                if i == len(s) - 1:
                    n.count += 1
                else:
                    n.m = _insert(i+1, n.m)
            elif n.c < s[i]:
                n.r = _insert(i, n.r)
            else:
                assert n.c > s[i]
                n.l = _insert(i, n.l)
            return n
        self.root = _insert(0, self.root)

    def contains(self, s):
        if not s:
            return True
        n = self.root
        i = 0
        while i < len(s) and n:
            if n.c == s[i]:
                n = n.m
                i += 1
            elif n.c < s[i]:
                n = n.r
            else:
                assert n.c > s[i]
                n = n.l
        if i == len(s):
            return True
        return False
    
    def __str__(self):
        def _traverse(s, l, n):
            if not n:
                return s
            s = _traverse(s, l + 1, n.l)
            s += '\n' + (' ' * l) + n.c
            s = _traverse(s, l, n.m)
            s = _traverse(s, l + 1, n.r)
            return s
        s = _traverse('< Trie:', 0, self.root)
        s += '\n>'
        return s


trie = Trie()
trie.insert('bb')
trie.insert('ee')
trie.insert('cc')
trie.insert('aa')
assert trie.contains('aa')
assert trie.contains('bb')
assert trie.contains('cc')
assert trie.contains('cc')
assert trie.contains('ee')
print(trie)
print('PASS')
