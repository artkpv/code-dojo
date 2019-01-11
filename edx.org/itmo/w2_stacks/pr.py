#!/usr/bin/env pypy
"""
1<=N<=1e6 cups
0 <= a_i <= 100
Cup: >0 filled; 0 empty
Empty - at bottom of smallest or new if no
Fill - new

I1 Naive
sorted list of stacks by height (height, stack)
Insert: swap with last that less O(n)
Time: O(n^2)  Space: ~n

I2
The same but store number of stacks: (height, stacks num)
Example: 1,2 3,1 > 1,1 2,1 3,1 > 2,2 3,1 > 2,1 3,2 < 1,1 2,1 3,2 ..
Time: ~(N) Space: O(N)

Ex1
5
1 0 0 2 0

2
3 1
2 1

Ex2
7
0 1 0 2 0 3 0 0

1,1


"""

fr = open('input.txt')
fw = open('output.txt', 'w')

n = int(fr.readline().strip())
a = [int(i) for i in fr.readline().strip().split(' ')]
s = []
for i,e in enumerate(a):
    if e > 0:
        if s and s[-1][0] == 1:
            s[-1][1] += 1
        else:
            s += [[1,1]]
    else:
        if not s:
            s += [[1,1]]
        else:
            h = s[-1][0] + 1
            s[-1][1] -= 1
            if len(s) == 1 or s[-2][0] != h:
                old = s.pop()
                s += [[h, 1]]
                s += [old]
            else:
                s[-2][1] += 1

            if s[-1][1] == 0:
                s.pop()

fw.write("%d\n" % len(s))
for i,e in enumerate(s):
    fw.write("%d %d\n" % (e[0], e[1]))








