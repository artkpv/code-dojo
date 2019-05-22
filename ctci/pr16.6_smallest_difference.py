#!python3

a = sorted(int(i) for i in input().strip().split(' '))
b = sorted(int(i) for i in input().strip().split(' '))

if len(a) == 0 or len(b) == 0:
    exit()

sd = abs(a[0] - b[0])
i, j = 0, 0
while i < len(a) and j < len(b):
    if abs(a[i] - b[j]) < sd:
        sd = abs(a[i] - b[j])
    if a[i] > b[j]:
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        break

print(sd)

