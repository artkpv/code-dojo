#!python3
n = int(input().strip())

radix = ord('z') - ord('a') + 1

class Node:
    def __init__(self):
        global radix
        self.next = [None] * radix
        self.count = 0
        self.words = 0

class Conference:
    def __init__(self):
        self.root = Node()

    def put_get(self, name):
        self._put(name, 0, self.root)
        return self._get(name, 0, self.root)

    def _put(self, name, i, node):
        c = ord(name[i]) - ord('a')
        next = node.next[c]
        if not next:
            next = Node()
            node.next[c] = next
        next.count += 1
        if i != len(name) - 1:
            self._put(name, i+1, next)
        else:
            next.words += 1

    def _get(self, name, i, node):
        c = ord(name[i]) - ord('a')
        next = node.next[c]
        if i == len(name) - 1:
            return name + (' ' + str(next.words) if next.words > 1 else '')
        elif next.count == 1:
            return name[0:i+1]
        else:
            return self._get(name, i+1, next)

c = Conference()
for i in range(n):
    print(c.put_get(input().strip()))

