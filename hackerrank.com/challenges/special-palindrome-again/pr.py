#!python3

"""
1<=s <= 10^6
Spec. palindromic str: 1. all same; 2. all same except the middle one 
Palindromic s. can repeat!

1. BF. Each char - palindromic
Time: O(n*n), space O(n*n)

2. 
1 type: all same, m, count = m*(m+1)/2
2 type: l+1+r, l>1, l==r, count = l
count last 3 chars num:
 on char change or end:
   count 1 type
   count 2 type
Time: ~(n), Space: ~1

Ex1
aaaa  10
4 
|4 3 2 1 3 2 1 2 1 1| = 10
m, sum(m-k, k= m-1..0) = m + m-1 + m-2 + .. + 2 + 1 = m*(m+1)/2
3 : 1 2 3 = 6 = |3 2 2 1 1 1|
"""

n = int(input().strip())
assert(n > 0)
s = input().strip()
assert(len(s) == n)
l3 = l2 = 0
l1 = 1
i = 1
count = 0
while i <= len(s):
    if i == len(s) or s[i-1] != s[i]:  # change
        # count type 1:
        count += l1*(l1+1)/2
        # count type 2:
        if l2 == 1 and s[i-l1-l2-1] == s[i-1]:
            count += min(l1, l3)
        # next:
        l3 = l2
        l2 = l1
        l1 = 1
    else:
        l1 += 1
    i += 1
print(int(count))

