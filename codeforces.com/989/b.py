#!python3
"""
17 10
..1.100..1..0.100
"""

n,p=[int(i) for i in input().strip().split(' ')]
s = [i for i in input().strip()]
i = 0
is_not_p = False
while i < n-p:
    if s[i] != s[i+p] or s[i] == '.' or s[i+p] == '.':
        if s[i] == '.':
            s[i] = '0' if s[i+p] == '1' else '1'
        if s[i+p] == '.':
            s[i+p] = '0' if s[i] == '1' else '1'
        is_not_p = True
        break
    i += 1

if not is_not_p:
    print('No')
else:
    while i < n:
        if s[i] == '.':
            s[i] = '0'
        i += 1

    print(''.join(s))
