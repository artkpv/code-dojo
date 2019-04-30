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


def getmiddle(a, b):
    assert a != b
    middle, remainder = divmod(max(a, b) - min(a, b), 2)
    if remainder > 0:
        return None
    return (a + middle, middle)


def getvariants(D, a):

    for point in list(D.keys()):
        diff = D[point]
        if (a - diff != point
                and a + diff != point
                and a != point):
            del D[point]
    return D


n = int(input('').strip())
A = [int(i) for i in input('').strip().split(' ')]

# find:
D = {A[0]: None}
for a in A[1:]:
    D = getvariants(D, a)
    if not D:
        break

# output:
values = list(D.values())
if len(values) == 1 and values[0] is None:
    values[0] = 0
print(-1 if not values else min(values))



a = A[0]
b = None
for i in range(1, len(A)):
    if A[i] != a:
        b = A[i]
        break

if b is None:
    print(0)
    exit()
else:
    D = {a: abs(a - b), b: abs(a - b)}
    middle = getmiddle(a, b)
    if middle is not None:
        D[middle[0]] = middle[1]

    for b in A[i+1:]:
        D = getvariants(D, b)
        if not D:
            break
    if not D:
        print(-1)
    else:
        print(min(D.values()))
