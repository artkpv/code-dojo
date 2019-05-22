#!python3


def urlify(s, m):
    i = m - 1
    j = len(s)
    while i >= 0:
        if s[i] == ' ':
            s[j-3], s[j-2], s[j-1] = '%', '2', '0'
            j -= 3
        else:
            s[j-1] = s[i]
            j -= 1
        i -= 1


n = int(input().strip())
m = int(input().strip())
s = [c for c in input().strip()] or []
s += [' '] * (n - len(s))
urlify(s, m)
print(''.join(s))

"""
Ex1
"Mr John Smith    "
 012345678901234567

"Mr Jogn   %20Smith"
 012345678901234567
i: 16 12 11 10 .. 7 6
j: 17 16 15 13 10 ..


"""
