#!python3

"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams

Anagram - rearranged letters
ss - consequentive letters from s
1 <= |ss| < n

s: 2..100
q: 1..10
Anagrams - ?


1) BF. For 1..n-1, all ss, count all pairs. anagrams = pairs*(pairs-1)/2. T: O(n^3*q), ~10^7. S: O(n^2)


"""

queries = int(input().strip())
for query in range(queries):
    s = input().strip()
    n = len(s)
    d = dict()
    for i in range(1, n):
        for j in range(n-i+1):
            ss = ''.join(sorted(s[j:j+i]))
            if ss not in d:
                d[ss] = 0
            d[ss] += 1
    count = sum(int(d[ss]*(d[ss]-1)/2) for ss in d)
    print(count)


