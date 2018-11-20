#!python3
"""
lex. or.
bigger - later in lex. or.
swap 1 or all
must be bigger, smallest
'no answer' - not possible
T <= 10^5
1 <= |w| <= 100, a..z


1) BF: T ~(!N*!N*N), S ~(N!)

2) insert. sort from right, till found. T: O(N*N) S: O(1)

Ex:
12 -> 21
21 -> no answer
22 -> no answer

1543 -> 3154

dkhc -> hcdk
[100, 107, 104, 99]
2 4 3 1 -> 3 1 2 4

hdkc
3 2 4 1


NEXT:
    - подумай о примере в котором не работает постановка наименьшего справа на первое место меньше его.

"""


def nexts(s):
    n = len(s)
    if n == 1:
        return None
    s = [ord(c) for c in s]

    i, j = n-1, n-2
    found = False
    while i > 0:
        j = i - 1
        while j >= 0:
            if s[j] < s[i]:
                found = True
                break
            j -= 1
        if found:
            break
        i -= 1

    if not found:
        return None

    while j < i:
        t = s[i]
        s[i] = s[i-1]
        s[i-1] = t
        i -= 1

    i += 1

    s = s[:i] + sorted(s[i:])

    return ''.join(chr(o) for o in s)

t = int(input().strip())
for i in range(t):
    s = input().strip()
    print(nexts(s) or 'no answer')
