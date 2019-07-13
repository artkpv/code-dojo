#!python3

n, m, r = [int(i) for i in input('').strip().split(' ')]
S = [int(i) for i in input('').strip().split(' ')]
B = [int(i) for i in input('').strip().split(' ')]

actions, remain = divmod(r, min(S))
gain = actions * max(B)
if gain - actions*min(S) > 0:
    print(gain + remain)
else:
    print(r)
