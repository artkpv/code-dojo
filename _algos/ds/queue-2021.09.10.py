
class Q:
    class Node:
        def __init__(self, v):
            self.next = None
            self.v = v

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, v):
        n = Q.Node(v)
        if not self.first:
            assert not self.last
            self.first = self.last = n
        else:
            self.last.next = n
            self.last = n

    def dequeue(self):
        if not self.first:
            return None
        v = self.first.v
        if self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
        return v



q = Q()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
assert 1 == q.dequeue()
assert 2 == q.dequeue()
assert 3 == q.dequeue()
assert 4 == q.dequeue()
assert 5 == q.dequeue()

print("PASS")
