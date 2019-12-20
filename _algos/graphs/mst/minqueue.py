import heapq
class MinPQ:
    """ Minimum priority queue with decrease key """
    def __init__(self):
        self.a = []

    def add(self, weight, value):
        heapq.heappush(self.a, (weight, value))

    def pop(self):
        if self.a:
            return heapq.heappop(self.a)[1]
        return None

    def contains(self, v):
        return v in (i[1] for i in self.a)

    def decrease(self, weight, value):
        for i,e in enumerate(self.a):
            if e[1] == value:
                break
        del self.a[i]
        heapq.heapify(self.a)
        heapq.heappush(self.a, (weight, value))

    def __len__(self):
        return len(self.a)

    def __repr__(self):
        return str(self.a)