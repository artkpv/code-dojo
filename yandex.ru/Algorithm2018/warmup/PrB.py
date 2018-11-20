#!python3
"""
https://contest.yandex.ru/algorithm2018/contest/7456/problems/B/
"""

s = input().strip()
n = len(s)

x = -1  # palindrom left most index
y = n + 1  # palindrom length
for i in range(len(s)-1):  # iterate all possible centers of palindrom
    for c in [0,1]:  # 0 - odd, 1 - even length
        l = i + c - 1
        r = i + 1
        is_palindrom = 0 <= l and r < n and s[l] == s[r]
        if is_palindrom and (r - l + 1 < y or s[x:x+y] > s[l:r+1]):
            x = l
            y = r - l + 1

print(s[x:x+y] if x != -1 else -1)
