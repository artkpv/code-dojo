#!python3
"""
1E
ashley
ash
2

2E
hackerhappy
hackerrank
9

3E
""
"abcd"
4

4E
"abc"
""
3

5E
""
""
0

6E
"xxxxabc"
"xxxxdef"
7
No

7E
y
yu
2
NO
"""

s = input().strip()
t = input().strip()
k = int(input().strip())
lcp = 0  # longest common prefix
while lcp < len(s) and lcp < len(t) and s[lcp] == t[lcp]:
  lcp += 1
k -= len(s) - lcp
k -= len(t) - lcp
if k > 0:
  # 2 moves to delete and add:
  if 2*lcp <= k:
    k = 0  # as can remove by 1 at empty
  else:
    k = 0 if k % 2 == 0 else -1
print('Yes' if k == 0 else 'No')
