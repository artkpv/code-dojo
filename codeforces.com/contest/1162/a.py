#!python3

n, h, m = [int(i) for i in input().strip().split(' ')]
money = [h] * n
for _ in range(m):
   l, r, area_h = [int(i) for i in input().strip().split(' ')]
   for inx in range(l-1, r):
       if money[inx] > area_h:
            money[inx] = area_h
print(sum(m**2 for m in money))
