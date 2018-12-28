#!python3
"""

Ex1
+ 10    10
+ 9     9
+ 8     8
+ 7

Ex2
+ 1     1
+ 10    1 10
+ 2     1 2
-       2
-       2
-       None



"""

from collections import deque

class QueueWithMin:
    def __init__(self):
        self.arr = deque()
        self.minarr = deque()
    
    def enqueue(self, n):
        self.arr.append(n)
        counter = 1
        while self.minarr and self.minarr[-1][0] >= n:
            counter += self.minarr[-1][1]
            self.minarr.pop()
        self.minarr.append((n, counter))

    def dequeue(self):
        if not self.arr:
            return None
        n = self.arr[0]
        self.arr.popleft()
        counter = self.minarr[0][1]
        counter -= 1
        if counter == 0:
            self.minarr.popleft()
        else:
            self.minarr[0] = (self.minarr[0][0], counter)
        return n
    
    def get_min(self):
        return self.minarr[0][0] if self.minarr else None


if __name__ == '__main__':
    import sys
    from edx_io import edx_io
    with edx_io() as io:
        n = io.next_int()
        queue_with_min = QueueWithMin()
        for operation in range(n):
            op = io.next_token().decode()
            if op == "+":
                queue_with_min.enqueue(io.next_int())
            elif op == "-":
                queue_with_min.dequeue()
            elif op == "?":
                io.write("%d\n" % queue_with_min.get_min())

    # fr = open('input.txt' if not sys.argv else sys.argv[1], 'r')
    # fw = open('output.txt', 'w')

    # n = int(fr.readline().strip())
    # queue_with_min = QueueWithMin()
    # for operation in range(n):
    #     op = fr.readline().strip().split(' ')
    #     if op[0] == "+":
    #         queue_with_min.enqueue(int(op[1]))
    #     elif op[0] == "-":
    #         queue_with_min.dequeue()
    #     elif op[0] == "?":
    #         fw.write("%d\n" % queue_with_min.get_min())
