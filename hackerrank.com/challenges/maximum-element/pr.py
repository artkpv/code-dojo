#!python3
"""
1 x   Push x at stack
2     Pop
3     Print max

N <= 10^5

Idea 1
stack + heapq

Time: Push - O(n*log(n)); pop O(n*n); print O(1)
Space: O(n)


Idea 2
Stack item has heap index
Heap.push() : use heap index

Time: pop O(n*log(n))
Space: O(n)


Idea 3

"""

from heapq import heappush, heapify

stack = []
heap = []
for _ in range(int(input('').strip())):
    query = input('').strip().split(' ')
    if query[0] == '1':
        item = int(query[1])
        stack += [item]
        heappush(heap, -item)
    elif query[0] == '2':
        if stack:
            item = stack[-1]
            del stack[-1]
            del heap[heap.index(-item)]
            heapify(heap)
    elif query[0] == '3':
        print(-heap[0])

"""
Example
Stack: 26
Heap: 26
print  26
"""
