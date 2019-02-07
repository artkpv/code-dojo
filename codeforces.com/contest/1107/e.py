#!python3

"""

NEXT: Optimize. How to DIVIDE optimal solution?  Try: optimal = current seq taken or not;


PROBLEM: http://codeforces.com/contest/1107/problem/e

1<=n<=100
s = [i:{0,1}]
a = [a_i] cost for i+1 deleted chars
max for deleting till empty

I1 BF
count of subsets, B: b1,b2,b3,b4,..,b_m  sum(..) = n
for each p in permutations of m:  // m!
    for each p_i in p:  // m 
        cost to remove b_i elements from A  // amortized const
        continue with B \ b_i
cost for k elements:  // w/o memoization: ~(k)
  max { 
    cost for 1-k ,
    A[k]
  }
Time: O(m!*m*k)
Max: O(100!*100*1)  E2


I2 BF
Order to delete? With optimal cost to delete k elements known.
max cost (k_i) {
  if no b[i] then start over if any left
  cost of k_i + max (B \ k_i),  // deleted
  cost of B with k_i 
}
=> cost = 2^(m+)
Time: O(2^(m+))
Space: 2^(m+)

I3 
Memoization? Because will repeat. 
And removal of 1 makes m-2
0101


E1 
7
1101001
3 4 9 100 1 2 3
1101001 → 111001 → 11101 → 1111 → ∅.

E2
100
0101..0101
1 1 .. 1 1000 1 .. 1 1  <- a[50] = 1000, others 1
Optimal: all 0 or 1, then 50 at once

"""
import sys
sys.setrecursionlimit(99999)

n = int(input().strip())
s = [i for i in input().strip()]
a = [int(i) for i in input().strip().split(' ')]
ss = []
for i,e in enumerate(s):
  if i == 0 or s[i-1] != e:
    ss += [1]
  else:
    ss[-1] += 1

d = {1:a[0]}

def set_cost(m, a):
  if m not in d:
    r = max(
      a[0] + set_cost(m-1, a),
      a[m-1]
    )
    d[m] = r
  return d[m]

dd = {}
def cost(s, a):  # TODO: O(n!)
  if s not in dd:
    max_ = 0
    for i,e in enumerate(s):
      new_s = []
      for ii,ee in enumerate(s):
        if ii < i - 1 or i + 1 < ii:
          new_s += [ee]
        elif ii == i and len(s) > 1:
          new_s += [(s[i-1] if i > 0 else 0) + (s[i+1] if i < len(s)-1 else 0)]
        # else i-1 and i+ 1 skip
      assert(len(new_s) < len(s))
      r = set_cost(e, a) + cost(tuple(new_s), a)
      if max_ < r:
        max_ = r
    d[s] = max_
  return d[s]

print(cost(tuple(ss), a))