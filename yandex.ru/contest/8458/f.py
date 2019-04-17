#!python3
"""
k <= 1024
len a[i]  <= 10*k
n == sum (len(a[i]))


max: k*10*k = 2^20*10 = 2^23 numbers. 1 byte per number. 10 MB



k*log(k)*n


"""

k = int(input('').strip())
MAX = 100
counts = [0] * (MAX+1)
result_len = 0
for i in range(k):
    line = [int(i) for i in input('').strip().split(' ')]
    result_len += line[0]
    for e in line[1:]:
        num = int(e)
        counts[num] += 1

for num, count in enumerate(counts):
    if count > 0:
        print((str(num) + ' ') * count, end='')
print('\n')
