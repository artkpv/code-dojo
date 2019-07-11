#!python3

from collections import Counter

n = int(input().strip())
s = input().strip()

c = Counter(s)
if c['0'] == c['1']:
    print(2)
    print(s[:1], s[1:])
else:
    print(1)
    print(s)




