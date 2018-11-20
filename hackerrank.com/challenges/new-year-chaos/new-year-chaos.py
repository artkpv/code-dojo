#!python3

"""
https://www.hackerrank.com/challenges/new-year-chaos/problem

1 2 5 3 7 8 6 4


1 2 3 5 7 8 6 3   0 0 0 1 0 0 0 0

"""

def swap(q, i, j):
    t = q[i]
    q[i] = q[j]
    q[j] = t

def get_min_bribes(q, n):
    bribes = [0] * (n+1)
    for i in range(n-1, -1, -1):
        for j in range(i, n-1):
            if q[j] < q[j+1]:
                break
            if bribes[q[j]] >= 2:
                return -1
            swap(q, j, j+1)
            bribes[q[j+1]] += 1
    return sum(bribes)

t = int(input().strip())
for test in range(t):
    n = int(input().strip())
    q = [int(i) for i in input().strip().split(' ')]
    b = get_min_bribes(q, n)
    print(b if b != -1 else 'Too chaotic')
