#!python3

"""
3 <= n <= 10^7
1 <= m <= 2* 10^5
0<=k <= 10^9


Idea 1
Add m times, k to n values. Keep max.
Time: O(m*n) = ~10**12
Space: O(1)

Idea 2
Find somehow from intersection.
l r k
If k the same then result -> n_i with max intersections.
How to find intersected intervals on x point?
    Sort by l.  O(m*log(m))
    Go from left to right adding / removing intervals.  O(m * 2*log(m))
    Maintain min heap with r coordinates. And keep a sum as doing that.

Time: O(m*log(m) + m*2*log(m)) = O(m*log(m))
Space: m sorted intervals + m - heap


Example 1
5 3
1 2 100
2 5 100
3 4 100

sum_ max_ queue
0    0    []
100  100  (2 100)
200  200  (2 100) (5 100)
100  200  (5 100) (4 100)
> 200

Example 2
10
1 5 3
4 8 7
6 9 1

sum_ max_ queue
0    0    []
3    3    (5 3)
10   10   (5 3) (8 7)
8    10   (8 7) (9 1)
> 10


Example 3
10
1 10 100

0 0 []
100 100 (10 100)
> 100


Example 4
10
1 10 1
2 9  2
3 8  3
4 7  4
5 6  5
6 6  6    Max expected = 21

0 0 []
1 1 (10 1)
3 3 (9 2) (10 1)






"""
import heapq

n, m = [int(i) for i in input('').strip().split(' ')]
intervals = []
for _ in range(m):
    intervals += [tuple(int(i) for i in input('').strip().split(' '))]

intervals.sort(key=lambda e: e[0])
queue = []  # priority queue
max_ = 0
sum_ = 0
for l, r, k in intervals:
    while queue and queue[0][0] < l:
        sum_ -= queue[0][1]
        heapq.heappop(queue)
    heapq.heappush(queue, (r, k))
    sum_ += k
    if sum_ > max_:
        max_ = sum_

# no use to empty queue as this will only lower sum_

print(max_)
