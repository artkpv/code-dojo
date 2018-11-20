n = int(input().strip())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = len(alpha)
for i in range(n):
    k = int(input().strip())
    out = []
    while True:
        k, r = divmod(k - 1, m)
        out.insert(0, alpha[r])
        if k == 0:
            break
    print(''.join(out))



