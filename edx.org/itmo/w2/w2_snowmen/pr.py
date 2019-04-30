#!/usr/bin/pypy
"""
n <= 10^6
1 <= m <= 1000


I1 BF.
10^6 stacks
Time: O(N*N)  to clone!

I2
Build tree. Like a trie. Values - snowman mass.

I3
Array of (parent, mass).
Add: parent mass + mass
Remove: parent = parent parent
Total mass: sum by mass
Time: ~(n)
Space: ~(n)


E1
8
0 1
1 5
2 4
3 2
4 3
5 0
6 6
1 0
> 74

sm[0] = 0,0
sm[1] = 0,1
sm[2] = 1,6
sm[3] = 2,10
sm[4] = 3,12
sm[5] = 4,15
sm[6] = 3,12
sm[7] = 6,18
sm[8] = 0,0


E2
4
0 1
0 2
2 0
1 1

0 1 2 0 2 > 5

E3
5
0 2
1 2
2 2
3 0
4 0

0 2 4 6 4 2
> 18

0 0,0
1 0,2
2 1,4
3 2,6
4 1,4
5 0,2


E4
Max
1e6
i 1000

1e6*1000 + (1e6-1)*1000 + .. =


"""
import sys
fr = open('input.txt')
fw = open('output.txt', 'w')

n = int(fr.readline().strip())
sm = [None] * (n+1)  # snowmen
sm[0] = (0, 0)  # parent, mass
for op in range(n):  # op - operation
    t, m = [int(i) for i in fr.readline().strip().split(' ')]
    if m > 0:
        sm[op+1] = (t, sm[t][1] + m)
    else:
        sm[op+1] = sm[sm[t][0]]
fw.write(str(sum(i[1] for i in sm)) )

