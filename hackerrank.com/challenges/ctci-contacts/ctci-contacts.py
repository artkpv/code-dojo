#!python3

Base = ord('a')
R = ord('z') - Base + 1  # radix from statement

class Trie:
    class Node:
        def __init__(self):
            global R
            self.size = 0
            self.next = [None] * R

    def __init__(self):
        self.root = Trie.Node()

    def add(self, s):  # s - string
        global Base
        if s and len(s) > 0:
            i = 0
            v = self.root  # vertex
            while i < len(s):
                w = v.next[ord(s[i]) - Base]
                if not w:
                    w = Trie.Node()
                    v.next[ord(s[i]) - Base] = w
                w.size += 1
                v = w
                i += 1

    def find(self, p):  # p - prefix
        global Base
        i = 0
        v = self.root
        while v != None and i < len(p):
            v = v.next[ord(p[i]) - Base]
            i += 1
        return v.size if v else 0


n = int(input().strip())
t = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        t.add(contact)
    if op == 'find':
        print(t.find(contact))

