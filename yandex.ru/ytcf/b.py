#!python3
n = int(input().strip())
p = []
for i in range(n):
    p += [tuple(int(k) for k in input().strip().split(' '))]

def line_hash(p1, p2):
    l = p1[0] - p2[0]
    m = p1[1] - p2[1]
    n = p1[2] - p2[2]
    x = -l*p1[2]/n + p1[0]
    y = -m*p1[2]/n + p1[1]
    a = l/m
    b = l/n
    return (x, y, a, b)

m = 0  # min queue
queues = dict()  # queues
for i in range(n-2):
    for j in range(i+1, n-1):
        h = line_hash(p[i], p[j])
        for k in range(j+1, n):
            h2 = line_hash(p[i], p[k])
            if h == h2:
                if h in queues:
                    queues[h] += 1
                else:
                    queues[h] = 3
                
                if queues[h] < m:
                    m = queues[h]

print(m)
