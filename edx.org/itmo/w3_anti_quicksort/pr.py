#!python3
"""
1<=n<=10^6

I1 QS reversed:


E1
3 4 5 2 1

0 4 2+2  3 4 1 2 5
0 3 1+3  3 2 1 4 5
0 2 

1 2 3 4 5
2 1 3 4 5
2 3 1 4 5
2 4 1 3 5
2 4 5 3 1


        2 4 5 3 1
0 4  5  2 4 1 3 5  8
0 3  4  2 3 1 4 5  7
0 2  3  2 1 3 4 5  6
0 1  2  1 2 3 4 5  4


2 3 1
3  5   2 1 3
  5

"""
n = int(open('input.txt', 'r').readline())
a = list(i+1 for i in range(n))

l = 0
r = 2
while r < n:
    m = (l+r)//2
    a[m], a[r] = a[r], a[m]
    r += 1

open('output.txt', 'w').write(' '.join(str(i) for i in a))