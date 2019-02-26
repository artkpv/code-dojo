#!python3
"""
n , m 
cmp i with j
a_ij

I1

E1
3 4
>>>>
>>>>
>>>>

E2
3 3
>>>
<<<
>>>

1  1  1
-1 -1 -1
>  >  >

E3
2 2
< >
< >

b2 a1 a2 b1
1 -1
1 -1
"""

n,m = [int(i) for i in input().strip().split(' ')]
comparisons = []
for i in range(n):
    comparisons += [input().strip()]
a_marks = [0] * n
b_marks = [0] * m
def order(comparisons, a_marks, b_marks, a, b):
    """
    TODO
    Recursively try to balance all marks.

    Compare two marks - a ? b, update recursively those that before or after updated ones.
    """
    compare = comparisons[a][b]
    if compare == '>':
        if not a_marks[a] > b_marks[b]:
            if a_marks[a] != 0 and b_marks[b] != 0:
                return False
            else:
                if b_marks[b] == 0:
                    b_marks[b] = 1
                a_marks[a] = b_marks[b] + 1
    elif compare == '<':
        if not a_marks[a] < b_marks[b]:
            if a_marks[a] != 0 and b_marks[b] != 0:
                return False
            else:
                if a_marks[a] == 0:
                    a_marks[a] = 1
                b_marks[b] = a_marks[a] + 1
    elif compare == '=':
        pass

    else:
        raise Exception('Invalid input')




