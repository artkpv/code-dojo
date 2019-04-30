#!python3
"""
I1
a b : D : { a:|a-b|, b:|a-b|, middle: min(a,b) +  abs( (a-b)/2 ) if int }

a b c : c =


Ex
1 4 4 7 4 1
1 4        1,3 4,3
1 4 4
1 4 4 7    4,3
1 4 4 7 4 1

Ex2
2 2 5 2 5
2      (0)
2 2 5   2,3  5,3
2 2 5 2 5
3

Ex3
1 3 3 7
1 3 3    1,2  3,2
1 3 3 7  > -1

"""


def getvariants(variants, x):
    left = []
    for point, diff in variants:
        if (x - diff == point
                or x + diff == point
                or x == point):
            left += [(point, diff)]
    return left


n = int(input('').strip())
A = [int(i) for i in input('').strip().split(' ')]

a = A[0]
variants = None
i = 1
while i < len(A):
    if A[i] != a:
        b = A[i]
        variants = [(a, abs(a - b)), (b, abs(a - b))]
        diff, remainder = divmod(max(a, b) - min(a, b), 2)
        if remainder == 0:
            variants += [(min(a, b)+diff, diff)]
        break
    i += 1

if not variants:
    print(0)
    exit()
else:
    for x in A[i+1:]:
        variants = getvariants(variants, x)
        if not variants:
            break
    if not variants:
        print(-1)
    else:
        print(min(diff for point, diff in variants))
