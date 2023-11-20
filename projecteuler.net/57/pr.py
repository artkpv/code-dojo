
mem = {}
n = 5
d = 2
count = 0
N = 1000
for _ in range(N-1):
    #print(n, d, f"{n + d}/{n}")
    if len(str(d + n)) > len(str(n)):
        count += 1
    t = 2 * n + d
    d = n
    n = t
print(count)







