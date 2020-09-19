#!python3
"""
1 <= n <= 10^5
sum of chars <= 5*10^5
Find max correct pairs num.
Pair: concats into valid seq.

I1 BF
choose one pair, then second, then third:
N*(N-1) / 2
(N-1)(n-2) / 2
..
4*3/2
2*1/2
Sum = 1/2 * ( n*(n-1) + (n-1)(n-2) + .. + 4*3 + 2 * 1 ) ~~ n ^ 3


I2
Make groups. Like 2 sum
Put into map -L and R and choose max pairs.
Time: ~ n


E1
7
)()) 2 0    1
) 1 0       2
(( 0 2      1
(( 0 2
( 0 1       2
) 1 0
) 1 0
Out:  2


E2
(
)
)( -- invalid




"""
def count_seq(line):
    o, c = 0, 0  # opens, closes
    for i,e in enumerate(line):
        if e == ')':
            if o > 0:
                o -= 1
            else:
                c += 1
        else:  # e == '('
            o += 1
    return c, o

n = int(input().strip())
pairs = {}
for seqence_num in range(1, n+1):
    line = input().strip()
    l, r = count_seq(line)
    can_make_pair = l == 0 or r == 0
    if not can_make_pair:
        continue
    if l > 0:
        pairs[-l] = pairs[-l] + 1 if -l in pairs else 1
    elif r > 0:
        pairs[r] = pairs[r] + 1 if r in pairs else 1
    else:  # l == 0 and r == 0
        pairs[0] = pairs[0] + 1 if 0 in pairs else 1

count = 0
for k in pairs:
    if k > 0:
        if -k in pairs:
            count += min(pairs[-k], pairs[k])
count += pairs[0] // 2 if 0 in pairs else 0

print(count)

