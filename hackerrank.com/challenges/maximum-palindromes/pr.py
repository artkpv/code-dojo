#!python3
"""

1 <= s <= 10^5
1 <= q <= 10^5
1 <= l <= r <= |s|

s[i] - lowercase English


Idea 1
ss substring, find num of max palindromes

for w in n..2:
    count chars  # ~N
    if <=1 odd chars - can do else not
    k - num of even chars
    number of palindroms = k!/chars1!/chars2! by MODULO  # ~N/2

Time: ~(N*N*N)
Space: ~1


Idea 2
Preprocess  ~N
count[i][] - num of chars till i-th

Then count[j][] - count[i][] - num of current; ~ RADIX = 26

Time: O(N*N)
Space: ~N*26


Ex
madamimadam
m 4
a 4
d 2
i 1
11 max length
5!/2/2 = 30 - palindroms of max length ,


"""

MODULO = 10**9 + 7


def getcharinx(char):
    return ord('z') - ord(char)


def factorial(n, k, mod):
    assert n >= k
    result = 1
    while n >= k:
        result = (result * n) % mod
        n -= 1
    return result


class Palindromer(object):
    def __init__(self, s):
        radix = ord('z') - ord('a') + 1
        # number of chars occurencies till i-th position including
        self.count = []
        count_at_i = tuple(0 for _ in range(radix))
        for char in s:
            myinx = getcharinx(char)
            count_at_i = tuple(
                e + (1 if myinx == i else 0)
                for i, e in enumerate(count_at_i))
            self.count += [count_at_i]

    def ask(self, left, right):
        if left == right:
            return 1

        if left == 0:
            charscount = self.count[right]
        else:
            charscount = tuple(
                rightel - leftel
                for leftel, rightel
                in zip(self.count[left-1], self.count[right])
            )

        evens = {i: e for i, e in enumerate(charscount)
                 if e % 2 == 0 and e > 0}
        odds = {i: e for i, e in enumerate(charscount)
                if e % 2 == 1 and e > 0}
        if odds:
            inx = max(odds, key=lambda k: odds[k])
            assert inx not in evens
            if odds[inx] > 1:
                evens[inx] = odds[inx] - 1

        # TODO get AMOUNT of max palindroms. Use odds

        assert len(evens) > 0

        sumevens = sum(evens[k] for k in evens)
        sumevens //= 2
        palindromes = factorial(sumevens, 1, MODULO)
        for charinx in evens:
            if evens[charinx]//2 > 1:
                palindromes //= factorial(evens[charinx]//2, 1, MODULO)

        print(self.count)
        print(evens)
        print(odds)
        print(palindromes)

        return palindromes


s = input('').strip()
palindromer = Palindromer(s)
for query in range(int(input('').strip())):
    l, r = [int(i) for i in input('').strip().split(' ')]
    l -= 1
    r -= 1
    print(palindromer.ask(l, r))
