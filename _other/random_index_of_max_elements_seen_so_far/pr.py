'''
https://www.careercup.com/question?id=5732335291465728

text
for each i , return rand index of max element seen so far. SHOULD be random probability to have this. 

I1. BF. Iter back and get max.
T: N * (N-1) / 2 
S: 1

I2. Keep max element indexes and return rand.
T: N
S: O(N)


Example 1
11 30 2 30 30 30 6 2 62 62 
0  1  1 3  4  5  5 5 8  8 
        1
'''

import random
def rand_index(arr):
    maxe = arr[0]
    indexes = [0]
    res = [0]
    for i, e in enumerate(arr[1:]):
        i += 1
        if e > maxe:
            maxe = e
            indexes = [i]
        elif e == maxe:
            indexes += [i]
        res +=[indexes[random.randint(0, len(indexes)-1)]]
    return res


def p(a):
    return '\t'.join(str(e) for e in a)
print(p([11, 30, 2, 30, 30, 30, 6, 2, 62, 62]))
print(p(rand_index([11, 30, 2, 30, 30, 30, 6, 2, 62, 62])))

