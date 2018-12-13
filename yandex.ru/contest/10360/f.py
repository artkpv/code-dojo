#!python3

n = 1000
s = 1
k = 1
while k <= n:
    s += 4**(k-1)/3**(2*k-1)
    k+=1
print(s)

