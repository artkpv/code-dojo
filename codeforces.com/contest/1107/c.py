#!python3

n, k = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
s = input().strip()
res = 0
j = 0
for i in range(1, n):
    ai, si = a[i], s[i]
    if si != s[i-1]:
        res += sum(sorted(a[j: i])[-k:])
        j = i
res += sum(sorted(a[j:])[-k:])

print(res)
    




