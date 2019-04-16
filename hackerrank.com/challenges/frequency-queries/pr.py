#!python3
"""
1 <= q <= 10^6
1 <= x,y,z <= 10^9
1 add, 2 delete one, 3 check if with that frequency

Idea 1
Two dictionaries
Numbers to frequency
Frequencies to numbers

add - incr in dic, remove / add in the set
delete decr in dic, remove / add in the set
query - if in the set

Time: ~(1)   ????   Hash(1..10^9)  !!
Space ~ n + n


Idea 2

"""

items = {}
counts = {}
out = []
for query in range(int(input('').strip())):
    operation, item = [int(i) for i in input('').strip().split(' ')]
    if operation == 1:
        old = items.get(item, 0)
        new = old + 1
        items[item] = new
        counts[old] = max(0, counts.get(old, 0) - 1)
        counts[new] = counts.get(new, 0) + 1

    elif operation == 2:
        old = items.get(item, 0)
        new = max(0, old - 1)
        items[item] = new
        counts[old] = max(0, counts.get(old, 0) - 1)
        counts[new] = counts.get(new, 0) + 1

    elif operation == 3:
        out += [True if counts.get(item, 0) > 0 else False]

print('\n'.join('1' if b else '0' for b in out))


"""

Example 1
8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2

i  items  counts
0  5-1    1-1
1  5-1 6-1   1-2
2  > 0
3  5-1 6-1 10-1   1-3
4  5-1 6-1 10-2   1-2 2-1
5  5-1 6-2 10-2   1-1 2-2
6  5-0 6-2 10-2   1-0
"""


"""
Explicit Way
MEMORY ERROR

MAX_ITEM = 10**9
MAX_FREQ = 10**6
items = [0] * MAX_ITEM
counts = [0] * MAX_FREQ
for query in range(int(input('').strip())):
    operation, item = [int(i) for i in input('').strip().split(' ')]
    if operation == 1:
        old = items[item-1]
        new = old + 1
        items[item-1] = new
        counts[old] = max(0, counts[old] - 1)
        counts[new] = counts[new] + 1

    elif operation == 2:
        old = items[item-1]
        new = max(0, old - 1)
        items[item-1] = new
        counts[old] = max(0, counts[old] - 1)
        counts[new] = counts[new] + 1

    elif operation == 3:
        print(1 if counts[item] > 0 else 0)



"""
