#!python3
"""
http://codeforces.com/contest/1131/problem/D

Not solved (2019-2-28). Looks like NP-hard problem. But how to solve it via BF? Iterating candidates till they exausted?


n , m 
cmp i with j
a_ij

I1
dfs on two sets

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

1,1  ,-1   1,
 ,0  ,0  ,0

E3
2 2
< >
< >

1,1  , 
2,   ,0

a1 > b1 and a1 > b2
a2 < b1 and a2 > b2

a1, a2, b1, b2 ?

a1=1 < b1, a2 < b1 



Ex4
3 2
==
=<
==
   1,11,1
1,1 =  =
 ,  =  <
 ,  =  =

"""

n,m = [int(i) for i in input().strip().split(' ')]
comparisons = []
for i in range(n):
    comparisons += [input().strip()]

class Node:
    def __init__(self):
        self.min = None  
        self.max = None  

first = [Node() for _ in range(n)]
second = [Node() for _ in range(n)]

# to balace around first day:
first[i].max = 1
first[i].min = 1


def eq(a, b):
    """ Try to make a == b """
    # can be balanced:
    if b.min and a.max and a.max < b.min:
        return False
    if b.max and a.min and b.max < a.min:
        return False
    # balance:
    a.min = b.min = (a.min or b.min)
    a.max = b.max = (a.max or b.max)
    return True


def lt(a, b):
    """ Try to make a < b """
    # is balanced:
    if b.min and a.max and a.max < b.min:
        return False
    if b.max and a.min and b.max < a.min:
        return False
    # balance:
    if a.min:
        b.min = a.min + 1
    return True

def gt(a, b):
    """ Try to make a > b """
    # is balanced:
    if b.min and a.max and a.max < b.min:
        return False
    if b.max and a.min and b.max < a.min:
        return False
    # balance:
    if a.max:
        b.max = a.max - 1
    return True

balance_actions = {'=': eq, '<': lt, '>': gt}
for i in range(n):
    for j in range(m): 
        comparison = comparisons[i][j]
        if not balance_actions[comparison](first[i], second[j]):
            # could not balance so break
            isbalanced = False
            break
    else:
        isbalanced = True
    if not isbalanced:
        break

# Min and max for all marks are set or it is un-balanced.
# So try to find min absolute marks satisfying this condition.
while isbalanced:
    first_copy = first.copy()
    second_copy = second.copy()
    for i in range(n):
        mark = first_copy[i]
        if mark.min < mark.max:
            mark.max = mark.min
            break
    else:
        isbalanced = False


print('YES' if isbalanced else 'NO')
if isbalanced:
    # now add absolute value to get 1 based marks:
    min_value = min(min(i.min for i in first), min(i.min for i in second))
    for day in first:
        day.min += min_value
    for day in second:
        day.min += min_value
    print(' '.join(str(i.min) for i in first))
    print(' '.join(str(i.min) for i in second))