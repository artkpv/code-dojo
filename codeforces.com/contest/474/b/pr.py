#!python3

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
s = [a[0]]
for a_i in a[1:]:
    s += [s[-1] + a_i]
queries = int(input().strip())

def bisect(s, m):
    lo = 0
    hi = len(s) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if (s[mid-1] if 0 < mid else 0) < m <= s[mid]:
            return mid
        elif s[mid] < m:
            lo = mid+1
        else:
            hi = mid-1
    raise Error('should have found')


for m in [int(q_i) for q_i in input().strip().split(' ')]:
    inx = bisect(s, m)
    print(inx + 1)


