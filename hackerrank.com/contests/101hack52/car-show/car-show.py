#!python3

import sys
sys.setrecursionlimit(10000)

D = {}

def get_valid_choices(a, l, r):
    global D
    if l > r:
        return 0
    if l == r:
        return 1

    if (l, r) not in D:
        # choices when it starts at l plus not at l
        # choices with l:
        s = set()
        s.add(a[l])
        for i in range(l+1, r+1):
            if a[i] in s:
                break
            s.add(a[i])
        count = len(s)

        # choices without l:
        count += get_valid_choices(a, l+1, r)
        D[(l, r)] = count
    return D[(l, r)]

if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    A = list(map(int, input().strip().split(' ')))
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        print(get_valid_choices(A, l-1, r-1))
