#!python3
"""
Using two stacks for one queue.

Enqueue stack - ES:
Dequeue stack - DS:

ES_M - min for ES
DS_M - min for DS

Time for N operations: ~N amortized
Space: 2N
"""

from collections import deque

INF = 9e9

class QueueWithMin:
    def __init__(self):
        self.es = []  # enqueue stack
        self.ds = []  # dequeue stack
        self.es_m = []  # min for enqueue stack
        self.ds_m = []  # min for dequeue stack
    
    def enqueue(self, n):
        if self.es_m:
            self.es_m += [min(self.es_m[-1], n)]
        else:
            self.es_m += [n]
        self.es += [n]

    def dequeue(self):
        if not self.ds:
            self.ds += [self.es.pop()]
            self.ds_m += [self.ds[-1]]
            while self.es:
                self.ds += [self.es.pop()]
                self.ds_m += [min(self.ds_m[-1], self.ds[-1])]
            self.es_m = []
        self.ds.pop()
        self.ds_m.pop()

    def get_min(self):
        return min(self.ds_m[-1] if self.ds_m else INF, self.es_m[-1] if self.es_m else INF)


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
