#!python3

def find_triangle(a, l, r):
    s = sorted(enumerate(a[l: r+1]), key=lambda x:x[1])
    for i in range(len(s)-1, 1, -1):
        if s[i][1] < s[i-1][1] + s[i-2][1]:
            return [l+s[i-2][0], l+s[i-1][0], l+s[i][0]]
    return None


n, q = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
for k in range(q):
    l, r = sorted(int(i) for i in input().strip().split(' '))
    res = find_triangle(a, l-1, r-1)
    print(' '.join(str(i+1) for i in res) if res else -1)

