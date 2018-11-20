#!python3
"""
https://contest.yandex.ru/algorithm2018/contest/7491/problems/E/
"""

n, q = [int(i) for i in input().strip().split(' ')]
A = input().strip().split(' ')
B = set(input().strip().split(' '))  # should be distinct

intervals = 0
for i in range(n):
    found = set()
    for j in range(i, n):
        if A[j] in B:
            found.add(A[j])
        if len(found) == q:  # all found
            intervals += n - j
            break
        tofind = len(B) - len(found)
        left = n - j - 1
        if tofind > left:
            break
    allFound = len(found) == len(B)
    if not allFound:
        break
print(intervals)


