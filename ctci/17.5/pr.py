#!python3
"""
E1
010
2

E2
0101
4

E3
00011
4

E4
0101001
6

E5
0111110
2

E6
0110110
4

E7
000
0

"""

s = [1 if c.isalpha() else 0 for c in input().strip()]
n = len(s)
ln = sum(s)
i = 0
while n > 0 and ln != n - ln:
    nn = n - ln
    if (s[i] == 1 and ln > nn) or (s[i] == 0 and ln < nn):
        if s[i] == 1:
            ln -= 1
        i += 1
    else:
        if s[i+n-1] == 1:
            ln -= 1
    n -= 1
    # print(s[i:i+n], n, ln)
print(n)



