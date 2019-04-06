#!python3
"""
1 <= s <= 1000
s[i] -- a..z, 26
abcdefghijklmnopqrstuvwxyz

26*25 = 1300/2 = 650

I1
BF. All pairs. 26*25
Time: O(26*25*n)
Space: C

"""
n = int(input(''))
s = input('').strip()
if len(s) == 1:
    print(0)
    exit()
chars = set(s)
longest = 0
for a in chars:
    for b in chars - set([a]):
        prev = None
        count = 0
        found = True
        for i, e in enumerate(s):
            if e in (a, b):
                if not prev:
                    prev = e
                elif prev == (b if e == a else a):
                    prev = e
                else:
                    found = False
                    break
                count += 1
        if found and count > longest:
            longest = count
print(longest)
