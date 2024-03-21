"""

I1 BF.
Get all possible sums for 4/9 or 6/6 dice and their outcomes count.
Then iter all outcomes where 4/9 > 6/6 
Time: 4^9  + 6^6 + 36*36

"""
from itertools import product
from collections import Counter

dice4 = Counter(
    sum(elements)
    for elements
    in product(range(1,5), repeat=9)
)
dice6 = Counter(
    sum(elements)
    for elements
    in product(range(1,7), repeat=6)
)

sum_d4 = sum(dice4.values())
sum_d6 = sum(dice6.values())

pr = 0
for x in dice4:
    for y in dice6:
        if x > y:
            pr += dice4[x] / sum_d4 * dice6[y] / sum_d6

print(round(pr, ndigits=7))
