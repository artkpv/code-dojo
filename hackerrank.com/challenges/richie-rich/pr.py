#!python3
"""
NEXT:
    fix this
    3 moves and 092282
    Need to substitude to max at first place
    and not waste moves on subst on less



0 < s <= 10^5
0 <= k <= 10^5
largest polindromic num ? or -1


Idea 1

u - unmatching = num of left != right pairs

1) k < u => -1
2) we can
    moves left = k
    if k - 2 >= u - 1:
        make both 9
    else:
        make one
3) if moves left:
    change to 9th from left

Time: ~(n + n + n)
Space: ~(n)


Ex1
1 3943 > 3993

Ex2
3 092282 > 992299

Ex3
1 0011 > -1

"""


def getpolyndrom(s, k):
    unmatch = sum(1 if e != s[-i-1] else 0
                  for i, e in enumerate(s[:len(s)//2]))
    if unmatch > k:
        return None

    # make polyndrom:
    for i, e in enumerate(s[:len(s)//2]):
        assert unmatch <= k
        candoboth = unmatch - 1 < k - 2
        if e != '9' and s[-i-1] != '9' and candoboth:
            # substitude both
            s[i] = '9'
            s[-i-1] = '9'
            k -= 2
        else:  # substitude one
            x = s[i] if s[i] > s[-i-1] else s[-i-1]
            s[i] = x
            s[-i-1] = x
            k -= 1
        unmatch -= 1
        print(s)

    assert unmatch == 0

    if k == 0:
        return s

    # make even greater polyndrom:
    for i, e in enumerate(s[:len(s)//2]):
        if k == 0:
            break
        if e != '9':
            tosubstitude = 2 if s[-i-1] != '9' else 1
            if k - tosubstitude < 0:
                continue
            k -= tosubstitude
            s[i] = '9'
            s[-i-1] = '9'

    for i in range(len(s)//2-1, -1, -1):  # from middle to outer
        if k == 0:
            break
        e = s[i]
        if s[-i-1] != '9':
            tosubstitude = 2 if e != '9' else 1
            if k - tosubstitude < 0:
                continue
            k -= tosubstitude
            s[i] = '9'
            s[-i-1] = '9'

    if len(s) % 2 == 1 and k > 0:
        s[len(s)//2] = '9'

    return s


n, k = [int(i) for i in input('').strip().split(' ')]
s = [c for c in input('').strip()]
poly = getpolyndrom(s, k)
print(''.join(poly) if poly else '-1')
