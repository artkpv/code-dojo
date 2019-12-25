#!python3

class Queue:
    def __init__(self, capacity=10):
        self.first = 0
        self.count = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def enqueue(self, e):
        if self.count == self.capacity:
            raise Exception('Queue is full')
        self.array[(self.first+self.count)%self.capacity] = e
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        e = self.array[self.first]
        self.first = (self.first+1)%self.capacity
        self.count -= 1
        return e

if __name__ == '__main__':
    # Test 1
    q = Queue()
    assert(q.count == 0)
    q.enqueue(1)
    assert(q.count == 1)
    assert(q.dequeue() == 1)
    assert(q.count == 0)
    for i in range(10):
        q.enqueue(i)
    assert(q.count == 10)

    # Test 2
    q2 = Queue(1)
    assert(q2.dequeue() == None)

    print('all tests pass')
