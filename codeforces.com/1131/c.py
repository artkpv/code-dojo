#!python3
"""

I0 BF. 100!

I1
sort
i+6 i+4 i+2 i i+1 i+3 i+5 i+7
inconv. = max(a[i+2]-a[i])
n log n + n 

5
2 1 1 3 2
3 2 1 1 2

4
1 2 3 4
3 1 2 4  incv=2

1 3 5 7  ..  6 4 2 


"""
n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
assert(len(a) == n)
a = sorted(a)
aux = [None] * n
left = 0
right = n-1
for i,e in enumerate(a):
    if i % 2 == 0:
        aux[right] = e
        right -= 1
    else:
        aux[left] = e
        left += 1
print(' '.join(str(i) for i in aux))