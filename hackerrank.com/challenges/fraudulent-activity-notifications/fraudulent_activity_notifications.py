#!python3

"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

1<=n<=2*10^5
1<=d<=n
0<=expenditure[i]<=200
notice for: d + 1 <= day <= n
median: odd - middle, even - middle_two/2
notice if exp >= median*2

1) Sort d elements at left and pick median. T: O(n*n*log(n)) S: O(1)

2) For each i find median at left using partition select. COPY elements for sort...
T: O(n*d*d), S: O(d)

3) BST. Balanced? Random adding?

4) Two heaps? Min heap, max heap. Remove: O(log(d/2)). Add: O(log(d/2)). Median: O(1). 
T: O(n*log(d/2)), S: O(d).
REMOVAL not in log(d), how to remove quickly some element in heap? 

"""

import heapq

class MedianTracker:
    def __init__(self, *args, **kwargs):
        self.left = []
        self.right = []
        return super().__init__(*args, **kwargs)

    def add(self, n):
        if len(self.left) > 0 and self.right[0] <= n:
            heapq.heappush(self.right, n)
        else:
            heapq.heappush(self.left, -n)
            
        # balance:
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, - heapq.heappop(self.right))
        elif len(self.left) > len(self.right):
            heapq.heappush(self.right, - heapq.heappop(self.left))

    def remove(self, n):
        # print(n)
        # print(self.left, self.right)
        if self.right[0] <= n:
            self.right.remove(n)
        else:
            self.left.remove(-n)

    def median(self):
        cmp = len(self.left) - len(self.right)
        if cmp < 0:
            return self.right[0]
        elif cmp > 0:
            return -self.left[0]
        else:
            return (self.right[0] - self.left[0])/2

n, d = [int(i) for i in input().strip().split(' ')]
days = [int(i) for i in input().strip().split(' ')]

noticies = 0
mt = MedianTracker()
for i, day in enumerate(days):
    if i > 0: 
        mt.add(days[i-1])
    if d + 1 < i + 1:
        mt.remove(days[i-d-1])

    if d + 1 <= i + 1:
        median = mt.median()
        if median * 2 <= day:
            noticies += 1
print(noticies)

