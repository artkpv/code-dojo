#!python3

n1, n2, n3 = [int(i) for i in input('').strip().split(' ')]
cylindres = [
    [int(i) for i in input('').strip().split(' ')],
    [int(i) for i in input('').strip().split(' ')],
    [int(i) for i in input('').strip().split(' ')]
]
sums = [0] * 3
for i, c in enumerate(cylindres):
    c.reverse()
    sums[i] = sum(c)

while not (sums[0] == sums[1] == sums[2]):
    i = sums.index(max(sums))
    sums[i] -= cylindres[i].pop()

print(sums[0])


