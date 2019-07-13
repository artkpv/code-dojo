#!python3
n = int(input().strip())
t = input().strip()
i = 1
j = 0
res = []
while j < n:
    res += t[j]
    j += i
    i += 1
print(''.join(res))

