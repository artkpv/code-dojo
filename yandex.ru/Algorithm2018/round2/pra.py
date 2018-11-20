#!python3


def swap(a, i, j):
    t = s[i]
    s[i] = s[j]
    s[j] = t

s = input().strip()
n = len(s)

a = []
for i in range(n):
    for j in range(i+1, n):
        if s[j] == s[i]:
            continue
        # swap and check it
        swap(a, i, j)




