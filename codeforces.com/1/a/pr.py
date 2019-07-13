#!python3
"""

6 6 4

11112222
11112222
11112222
11112222
3333


n%a == 0 : n//a else n//a + 1

"""

n, m, a = [int(i) for i in input().strip().split(' ')]
x = n//a + (1 if n%a > 0 else 0)
y = m//a + (1 if m%a > 0 else 0)
print(x * y)

