'''
Given string S, S_i = {H, T}, find least number of flips to make it S_i = H, S_j = T, i < j. 
len(S) < 10**5
Examples:
HHTH -> 1 (HHTT)
HTHT -> 1 (HTTT)
HHTTHHT -> 2 (HHHHHHT)


I1 BF. Min { for each pos count tails on left and heads on right to flip }
T: N*N
S: 1

I2 Store num of heads to the right. heads[i] number of H 
T: N
S: N

flips = (n - heads[i-1]) + (heads[-1] - heads[i-1])
'''


def headstails(s):
    if not s:
        return 0
    n = len(s)
    heads = [0] * (n+1)
    heads[0] = 1 if s[0] == 'H' else 0
    for i in range(1, n):
        heads[i] = heads[i-1] + (1 if s[i] == 'H' else 0)
    heads[-1] = heads[-2] # Extra is T.
    res = heads[-1]
    for i in range(1, n+1):
        res = min(res, i - heads[i-1] + heads[-1] - heads[i-1])
    return res


assert headstails('HHHHHH') == 0
assert headstails('HTHT') == 1
assert headstails('TTHT') == 1
assert headstails('TTHH') == 2
assert headstails('TTTH') == 1
assert headstails('') == 0
assert headstails('H') == 0
assert headstails('T') == 0
assert headstails('HTTTH') == 1
assert headstails('HTHTHTHTHT') == 4
assert headstails('HHTTTHH') == 2

print('pass')
