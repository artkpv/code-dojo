#!python3
w1, h1, w2, h2 = [int(i) for i in input().strip().split(' ')]
print(h1+h2+w2+h2+h1+w1+max(0,abs(w2-w1)-1)+(1 if w2 != w1 else 0) + 4)