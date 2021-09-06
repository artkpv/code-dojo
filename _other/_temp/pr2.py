from heapq import heappush, heappop






#####################################################

def range(res, lo, hi, v):
    if not v:
        return
    if lo < v.key:
        range(res, lo, hi, v.left)
    if lo <= v.key <= hi:
        res.append(v.key)
    if v.key < hi:
        range(res, lo, hi, v.right)
'''
T: O(height * range)
S: O(range)
'''


'''
1. B-tree

2-3 tree. Grows up. Extension. Leaves - values. k-cells in a node. 

    x1 x2 x3 x4 .. x_k
<x1    x1<=.<x2   x2<=.<x3 ... 
x11 x12 x13 .. 
<x11 ... 


Insert: 
if full breaks and adds into a parent new cell and repeates for parent
T: O(log(k, n)) - height.
S: O(log(n) * n)

k^h = n

Find:
T: O(log(k, n))


'''

def shellS(arr):
    n = len(arr)
    gap = 1
    while gap < n:
        gap = gap * 3 + 1  # 1 4 13 40 121 .. 
    gap //= 3
    while gap >= 1:
        for i in range(gap, n):
            j = i
            while j-gap >= 0 and arr[j-gap] > arr[j]:
                arr[j-gap], arr[j] = arr[j], arr[j-gap]
                j -= gap
        gap //= 3
    return arr

'''
3 8 1 0 2 4 7 5   n=8

gap 1 4 13 4 1

0 2 1 3 8 4 7 5  
    i                  
    j

T: n^a/b
S: in place, not stable
'''

print(shellS([1, 2,58,1,22,30,1,2,4,8]))
print(shellS([]))
print(shellS([1]))
