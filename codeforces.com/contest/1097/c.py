#!python3
"""
1 <= n <= 10^5

Correct for each pair OR for concatenation of pairs ?

Pair: equal L = R

I1 BF
N*(N-1) / 2
(N-1)(n-2) / 2
..
4*3/2
2*1/2
Sum = n/2*1/2 * ( n*(n-1) + (n-1)(n-2) + .. + 4*3 + 2 * 1 ) ~~ n ^ 3

Recursive to iterate


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
        if -l in pairs:
            pairs[-l] += 1
        else:
            pairs[-l] = 1
    else:  # r > 0
        if r in pairs:
            pairs[r] += 1
        else:
            pairs[r] = 1

count = 0
for k in pairs:
    if k > 0:
        if -k in pairs:
            count += min(pairs[-k], pairs[k])
print(count)

