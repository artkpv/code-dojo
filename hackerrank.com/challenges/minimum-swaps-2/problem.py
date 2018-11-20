#!python3
"""
https://www.hackerrank.com/challenges/minimum-swaps-2
"""

n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

sarr = sorted(arr)
isarr = {}
for i,e in enumerate(sarr):
    isarr[e] = i

swaps = 0
for i in range(n):
    while sarr[i] != arr[i]:
        j = isarr[arr[i]]
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        swaps += 1

print(swaps)
