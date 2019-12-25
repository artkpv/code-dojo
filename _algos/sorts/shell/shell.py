#!python3
"""
w1ld [dog] inbox dot ru
"""

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]

gap = 1
while gap < n:
    gap = gap*3 + 1
gap //= 3

count = 0;
while gap > 0:
    for i in range(gap, n, 1):
        j = i
        while j-gap >= 0 and a[j-gap] > a[j]:
            a[j-gap], a[j] = a[j], a[j-gap]
            j -= gap
            count += 1
    gap //= 3

# print(' '.join(str(e) for e in a))
print('Exchanges:',count)

