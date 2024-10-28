'''
a,b,c < 10^6
n <= 10^18

a b 
b c 
a c


s_n / a / b = q

gcd(a,b) * lcm(a,b) = a * b
lcm = a * b / gcd

for a, b:
if gcd(a,b) > 1: then only take a 
if gcd(a,b) = 1: 


I1
a b 

iter all n check if divs by a and b . 

T: 10^18


I2
Merge 3 sequences 
a b 
b c 
c a

to gen 

'''

import math
def solve():
    a,b,c = [int(i) for i in input().strip().split(' ')]
    n = int(input().strip())

    seq = [math.lcm(a,b), math.lcm(b,c), math.lcm(c,a)]
    seq_m = [a*b, b*c, c*a]
    seq_other = [c, a, b]

    ans = -1
    while n > 0:
        if ans > 10**18:
            return -1
        i = seq.index(min(seq))
        if seq[i] % seq_other[i] > 0:
            n -= 1
            ans = seq[i]
        seq[i] += seq_m[i]
    
    return ans


if __name__ == "__main__":
    print(solve())