#!python3
"""
k <= 1024
len a[i]  <= 10*k
n == sum (len(a[i]))


max: k*10*k = 2^20*10 = 2^23 numbers. 1 byte per number. 10 MB



k*log(k)*n


"""

k = int(input('').strip())
arrays = []
for i in range(k):
    line = [int(i) for i in input('').strip().split(' ')]
    arrays += [line[1:]]

