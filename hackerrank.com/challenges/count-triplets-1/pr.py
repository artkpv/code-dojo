#!python3
"""
1 <= n <= 10^5,  NOT SORTED!!!
1 <= r <= 10^9
1 <= a_i <= 10^9
Num of triples with geom progression with r.

Idea 1
Check all triples for condition. Count.
Time: ~ n * (n-1) * (n-2) ~= n^3

n*(n-1) / 2

n*(n-1)*(n-2) / 6

4*3*2 / 6 = 4

Space: ~1

Idea 2
Dictionary.
a b c
a a*r a*r*r
Need to find two others.
Maintain one dictionary by a and find remaining a*r and a*r*r.
b0 b1 b2
a_i can be b0 or b1 or b2 = b0 = a_i; b1 = a_i / r ; b2 = a_i / r / r
Two or more seq. with one b0 ?
How to count all sequences ? Now have way to find those.

Dictionary:
    one a0 : (count a0 indexes, count a1 indexes, count a2 indexes)
    two a0 : ...

Then num of all sequences = sum( d_i item: d_i[0] * [1] * [2] )

Time: ~n
Space: ~n

DON"T WORK !!!


Idea 3
The same as idea 2 but store indecies.
Need to count triples. BUT b0_inx < b1_inx < b2_inx  !
TODO


Example 1
2
1 2 2 4

1: 1 2 1
Result : 2


Example 2
2
1 1 2 2 4 4
1: 2 2 2
Result: 2*2*2

Ex 3
3
1 3 9 9 27 81

cache
1: 1 1 2
3: 1 2 1
9: 2 1 1
27: 1 1 0
81: 1 0 0

2+2+2 = 6

Example 4
81 27 9 9 3 1

81: (1 0 0)
27: (1 0 0)
9: (2 0 0)


Example 5
1
1
0


Example 6
1
1 1 1 1
1 2 3 4

1 2 3
1 2 4
1 3 4
2 3 4
> 4  !!

i count cache
0 0     1:1 0 0
1 0     1:2 1 0
2 4     1:2 2 1


Example 7
1
1 1 1 1 1  | 5 times
1 2 3 4 5


Example 8
3
1 9 3
0

Example 9
3
1 1 1 9 3 1
0




"""

num, ratio = [int(i) for i in input('').strip().split(' ')]
array = [int(i) for i in input('').strip().split(' ')]
ones = {}
pairs = {}
triples = 0
for i, e in enumerate(array):
    # update triples:
    base, remainder = divmod(e, ratio*ratio)
    if base > 0 and remainder == 0:
        if base in pairs:
            triples += pairs[base]

    # update pairs:
    base, remainder = divmod(e, ratio)
    if base > 0 and remainder == 0:
        pairs[base] = pairs.get(base, 0) + ones.get(base, 0)

    # update ones
    ones[e] = ones.get(e, 0) + 1


print(triples)
