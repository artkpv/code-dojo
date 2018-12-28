#!python3

"""

1.
n_ones
if k < n_ones: 
    NO

[2] * (k)


Ex1
9 = b1001
b0111+10
b0101+100

Ex2
b1010101
b0110101+0100000

Ex3
b10001 > b01111 + b00011

Ex4
13 > b1101
0101+0100
0011+0010+0010+0010
10 > 1 + 1 
100 > 2^4 > 1 1 1 1

8  1 
4  1 2 
2  1 2 2

---
разлагать в дерево на столкьо на сколько нужно

8
4 4 
2 2 2 2 
1 1 1 1 1 1 1 1 

глубина дерева 

"""

import math

d = {}

def f(n, k, res):
    if (n,k) in d:
        d_nk = d[(n,k)]
        res += res[d_nk[0]:d_nk[1]+1]
        return
    if n == 0:
        return
    assert(n >= k)
    assert(not (n > 1 and n % 2 == 1 and k == 1))
    i = len(res)
    if k == 1:
        p = math.log(n, 2)  # pow
        assert(round(p,0) == p)
        res += [n]
    elif n % 2 == 1:
        res += [1]
        n -= 1
        k -= 1
        f(n, k, res)
    elif k % 2 == 1:
        res += [2]
        k -= 1
        n -= 2
        f(n, k, res)
    else:
        f(n//2, k//2, res)
        f(n//2, k//2, res)
    d[(n,k)] = (i, len(res)-1)


n, k = [int(i) for i in input().strip().split(' ')]
res = []
if not (n < k or (k == 1 and n > 1 and n % 2 == 1)):
    f(n, k, res)

if res:
    print("YES")
    print(" ".join(str(i) for i in res))
else:
    print("NO")

print(d)

# res = []
# while n > 0 and k > 1:
#     q, r = divmod(n, 2)
#     if r == 0:
#         if q == 1:
#             res += [1, 1]
#             n = 0
#             k -= 2
#         else:
#             res += [2]
#             n = q
#             k -= 1
#     else:  # r == 1
#         res += [1]
#         n -= 1
#         k -= 1


# if not (n == 0 and k == 0):
#     print("NO")
# else:
#     print("YES")
#     print(" ".join(str(i) for i in res))

