#!python3
"""

I1. Stack. O(1)
"""
fr = open('input.txt')
fw = open('output.txt', 'w')
n = int(fr.readline().strip())
notation = fr.readline().strip().split(' ')
s = []
for el in notation:
    if el == '+':
        s += [int(s.pop()) + int(s.pop())]
    elif el == '-':
        b = int(s.pop())
        a = int(s.pop())
        s += [a - b]
    elif el == '*':
        s += [int(s.pop()) * int(s.pop())]
    else:
        s += [int(el)]

fw.write(str(s[0]) + "\n")



