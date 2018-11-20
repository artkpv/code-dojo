
"""
Ex1
5 4
In:  1 2 3 4 5
Out: 4 5 1 2 3

1 2 3 4 5 | n/2 < d, n-d: odd
1 5 3 4 2
4 5 3 1 2
4 5 2 1 3 | 1,2 not on their places
4 5 1 2 3



Ex2
1 2 3 4 5 | ~ n*d, n**2
2 3 4 5 1

Ex3
8 4
1 2 3 4 5 6 7 8  | n/2 == d
1 2 3 8 5 6 7 4
1 2 7 8 5 6 3 4
1 6 7 8 5 2 3 4
5 6 7 8 1 2 3 4

Ex4
8 6
1 2 3 4 5 6 7 8 | n/2 < d
1 8 3 4 5 6 7 2
7 8 3 4 5 6 1 2 | 1-2 on its places 3-6 untouched
7 8 3 4 5 2 1 6
7 8 3 4 1 2 5 6 | putting exchanging 1 and 2 all the way to left
7 8 3 2 1 4 5 6
7 8 1 2 3 4 5 6

Ex5
8 2
1 2 3 4 5 6 7 8 | n/2 > d
1 2 3 4 5 8 7 6
1 2 3 4 7 8 5 6
1 2 3



"""
n, d = [int(i) for i in input().strip().split(' ')]
A1 = [int(i) for i in input().strip().split(' ')]
if d == 0:
    print(' '.join(str(i) for i in A1))
    exit()

# Solution 1: ~(n) time, ~(n) space (not in place)
A2 = [0] * n
for i in range(n):
    a1_i = n - i - 1  # n-1 .. 0
    a2_i = n - i - 1 - d
    A2[a2_i] = A1[a1_i]
print(' '.join(str(i) for i in A2))



