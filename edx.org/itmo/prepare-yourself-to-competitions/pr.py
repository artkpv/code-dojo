#!python3
"""
2<=n<=100
0<= p_i, t_i < 1000
either p_i or t_i
at least one p_i and one t_i
< max ability

1)

Ex1
5
5 6 7 8 9  > 32=35-3
2 1 2 2 3




"""

with open('input.txt') as f:
    n = int(f.readline().strip())
    p = [int(i) for i in f.readline().strip().split(' ')]
    t = [int(i) for i in f.readline().strip().split(' ')]
    taken_t = 0
    taken_p = 0
    t_max_i = 0
    p_max_i = 0
    sum_ = 0
    for i in range(n):
        if p[i] > t[i]:
            sum_ += p[i]
            taken_p += 1
        else:
            sum_ += t[i]
            taken_t += 1
        if t[i] >= p[i] and t[i] - p[i] < t[p_max_i] - p[p_max_i]:
            p_max_i = i
        if p[i] >= t[i] and p[i] - t[i] < p[t_max_i] - t[t_max_i]:
            t_max_i = i
    if taken_t == n:
        sum_ -= t[p_max_i]
        sum_ += p[p_max_i]
    if taken_p == n:
        sum_ -= p[t_max_i]
        sum_ += t[t_max_i]


    with open('output.txt', mode='w') as fw:
        fw.write(str(sum_))


