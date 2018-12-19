#!python3
"""

4 digits
circle 0..9, clockwise, 0 top
rotations, right-left
1  1 >
2  9 < = 0+1-2=-1 mod 10 = 9
3  2 > = ||0+1|-2|+3=12 mod 10 = 2;
4  8
5  3
6  7
7  4
8  6
9  5
10 5
11 6
12 4
13 7
14 3
15 8
16 2
17 9
18 1
19 10 0
20 0
21 11 1
22 -1 9
23 12 2
24 -2 8
..
47 4

if even:
    m = (n+1)//2 mod 10
if odd:
    m = -n//2 mod 10

"""

def convert(n):
    if n%2 == 1:
        return ((n+1)//2)%10
    return (-n//2)%10

a = [int(i) for i in input().strip().split(' ')]
print(''.join(str(convert(i)) for i in a))
