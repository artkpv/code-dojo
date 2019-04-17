#!python3
"""
0 <= n <= 11
Correct parantheses of 2*n len.

0 -
1 - ()
2 - ()(), (())
3 - ((())), (()()),


Idea 1
( n times , ) n times.
First open, last close.

n-2 // 2 opens
n-2 // 2 closes
2n - 2

(2n-2)*(2n-3) ..  / (n-1)! (n-1)!

n = 3 , 4*3*2 / 2 / 2 = 6
n = 4 ,



"""


def isgood(a):
    opens = 0
    for i in a:
        if i == '(':
            opens += 1
        elif opens > 0:
            opens -= 1
        else:
            return False
    return opens == 0


def sort(a, lo, hi):
    for i in range(lo+1, hi+1):
        j = i
        while a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1


def permutations(a):
    """
    """
    yield a
    i = len(a)-2
    while 0 <= i:
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            sort(a, i+1, len(a)-1)
            if isgood(a):
                yield a
            i = len(a)-2
        else:
            i -= 1


n = int(input('').strip())
array = ['('] * n + [')'] * n
for p in permutations(array):
    print(''.join(p))

