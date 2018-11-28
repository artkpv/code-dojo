#!python3

"""
2 <= n <= 10^5
one swap
longest subsequent of G
subsequent - adj ones
k - G ones

1)
BF
num of swaps = (n-k)*k
Time O(n*n*n)

2)
A - longest ending at i w/o S
B - longest ending at i w/ one S



Ex 1
----1--1  -> 6


"""

n = int(input().strip())
s = input().strip()
a = [0] * n
b = [0] * n
a[0] = 1 if s[0] == 'G' else 0
b[0] = a[0]

max_ = 0
for i in range(1, n):
    if s[i] == 'G':
        a[i] = a[i-1] + 1
        b[i] = b[i-1] + 1
    else:
        if b[i-1] > 0 and b[i-1] > a[i-1]:
            if b[i-1] > max_:
                max_ = b[i-1]
            b[i] = a[i-1] + 1
            a[i] = 0
        elif b[i-1] > 0:
            assert(b[i-1] == a[i-1])
            if a[i-1] > max_:
                max_ = a[i-1]
            b[i] = a[i-1] + 1
            a[i] = 0
        else:
            b[i] = 0
            a[i] = 0
if b[n-1] > max_:
    max_ = b[n-1] + (0 if a[n-1] == b[n-1] else -1)

print(max_)



