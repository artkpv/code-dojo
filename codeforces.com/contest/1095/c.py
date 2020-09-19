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


15 = 8 + 7 = 8 + 4 + 3 = 8 + 4 + 2 + 1 = 2**3 + 2**2 + 2**1 + 2**0  | base power two


16 = 8 8 


28,5
> 16,3     12,2
> 8 4 4    8 4


5* 3/4 =3.7   3.7 + 1.3
"""

import math

# d = {}
# def f_old(n, k, res):
#     if (n,k) in d:
#         d_nk = d[(n,k)]
#         res += res[d_nk[0]:d_nk[1]+1]
#         return
#     if n == 0:
#         return
#     if n > k:
#         return

#     i = len(res)
#     log2 = math.log(n, 2)
#     nearest_power = 2**int(log2)
#     remain = n - nearest_power
#     if remain == 0:
#         if k == 1:
#             res += [n]
#         else:
#             f(n//2, k//2, res)
#             f(n//2, k - k//2, res)
#     else:
#         kk = k * remain/nearest_power
#         f(remain, kk, res)
#         f(nearest_power, k - kk, res)

#     d[(n,k)] = (i, len(res)-1)


def last_power_2(n):
    log2 = math.log(n, 2)
    return 2**int(log2)

def f(res):
    i = 0
    while i < len(res):
        n = res[i]
        a = last_power_2(res[i])
        if n - a == 0:
            break
        else:
            if i + 1 == len(res): 
                # Example: 11 2 > 8 3 ?
                return False
            else:
                res[i] = a
                res[i+1] = n-a
        i += 1

    if i < len(res):
        # fill remaining:
        j = 0
        i += 1
        while j < len(res) and i < len(res):
            if res[j] == 1:
                j += 1
            else: 
                m = res[j]
                res[i] = m//2
                res[j] = m//2
                i += 1
        return True


n, k = [int(i) for i in input().strip().split(' ')]
res = [0] * k
res[0] = n

if n >= k and f(res):
    print("YES")
    assert(sum(res) == n)
    print(" ".join(str(i) for i in res))
else:
    print("NO")


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

