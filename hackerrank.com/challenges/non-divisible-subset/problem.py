#!python3
"""
NEXT: измени с той интуицией что можно за О(n) сделать, т.к. нужно знать только 
количество тех чисел у которых одинаковый остаток от деления.

13 % 4 = 1
27 % 4 = 3

4
10 12 19 20 22 24 25

"""

n, k = [int(i) for i in input().strip().split(' ')]
A = list(set(int(i) for i in input().strip().split(' ')))
n = len(A)

S = [0] * k
for i in A:
    S[i%k] += 1

count = 0
# for i in range(int(k/2)):
#     if S[i] > S[k-i]:


# S = [ {A[0]%k : 1} ]
# 
# for i in range(1, n):
#     e = A[i]
#     a = e%k
#     b = (k-a)%k
#     for j in range(len(S)):
#         # a+b % k != 0 for any a,b in s
#         s = S[j]
#         if b in s:
#             s2 = s.copy()
#             s2.pop(b)
#             s2[a] = 1
#             S += [s2]
#         else:
#             if a in s:
#                 s[a] += 1
#             else:
#                 s[a] = 1
# print(max(sum(s[k] for k in s) for s in S))




"""
max_ = 0
for i in range(n):
    s = {i}
    for j in range(i+1, n):
        if not any(1 for p in s if (A[p]+A[j])%k == 0):
            s.add(j)
    if max_ < len(s):
        max_ = len(s)

print(max_)
"""

