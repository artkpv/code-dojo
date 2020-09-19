#!python3

n = int(input().strip())
draws = 1
scores = [(0,0)]
for time in range(n):
    a, b = [int(j) for j in input().strip().split(' ')]
    c, d = scores[-1]
    difference = min(a,b) - max(c,d)
    draws += (difference + 1 if difference >= 0 else 0)
    if c == d:
        draws -= 1
    scores += [(a,b)]
print(draws)


    
    

