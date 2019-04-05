#!python3
"""

I1
Move each num on its position if possible.

Time: n*n
Space: 1

E1
1 6 5 2 4 3
1 2 6 5 4 3
1 2 4 6 5 3
1 2 4 3 6 5
1 2 3 6 4 5
1 2 3 4 5 6

1 2 6 5 4 3
1 2 6 3 5 4
1 2 3 5 6 4
1 2 3 4 5 6

E2
1 2 3 5 4

1 3 5 2 4
1 3 2 4 5


"""

def cansort(a):
    for i in range(len(a)):
        min_ = min(a[i:])
        if a[i] == min_:
            continue
        for j in range(i+1, len(a)):
            if a[j] == min_:
                break
        assert(i < j)
        while j != i:
            if j - i == 1:
                if j + 1 >= len(a):
                    return False
                a[j-1], a[j], a[j+1] = a[j], a[j+1], a[j-1]
                j -= 1
            else:
                a[j-2], a[j-1], a[j] = a[j], a[j-2], a[j-1]
                j -= 2
    return True

for test in range(int(input().strip())):
    n = int(input().strip())
    a = [int(i) for i in input().strip().split(' ')]
    print("YES" if cansort(a) else "NO")
