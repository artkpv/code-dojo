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


"""


def nexts(ss):
    n = len(ss)
    if n == 1:
        return None
    s = [ord(c) for c in ss]

    i = n-1
    while i > 0 and s[i-1] >= s[i]:
        i -= 1

    if i == 0:
        return None

    j = i
    while j < n and s[i-1] < s[j]:
        j += 1
    j -= 1

    t = s[i-1]
    s[i-1] = s[j]
    s[j] = t
    return ''.join(chr(o) for o in s[:i] + sorted(s[i:]))


t = int(input().strip())
for i in range(t):
    s = input().strip()
    print(nexts(s) or 'no answer')
