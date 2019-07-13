#!python3
"""
2 <= n <= 100 000

p1
p2
p3 
... 

sum (pi) <= 100 000
beauty res (p1*p2*p3*p4..) <= 10^9

I1 BF

a1 a2 a3 a4

(a1+a2*a1+1) = b1
(b1+a3*b1+1) = b2

E1
a b a
bab a
abaaaba 3

abaaaba

E2
bnn a
abanana 1

E3
a b c

"""

n = int(input().strip())
a = []
for i in range(n):
    a += [input().strip()]

def next_(a):
    n = len(a)
    indexes = [0] * n
    while indexes[0] < len(a[0]):
        for str_i in range(n-1, -1, -1):
            for chr_i, e in enumerate(a[str_i]):



beauty = 0
while True:
    i = len(a)-1






