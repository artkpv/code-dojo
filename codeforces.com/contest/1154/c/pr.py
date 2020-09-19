#!python3
"""

1 <= a,b,c <= 7*10^8

1 2 3 4 5 6 7
a b c a c b a
3 2 2


I1
7 * n, ~ 5 * 10^9 TL
iterate 1..7
find optimal
O(N)

I2
Remove full weeks first then iterate

1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7
a b c a c b a a b c a c b a a b c a c b a
  ^                                   $
3 2 2 - for full week


x = min(a,b,c)
weeks = x // {3,2,2}
a -= weeks*3
b -= weeks*2
c -= weeks*2

O(7)




Ex1
2 1 1
> 4 days from 5

Ex2
3 2 2
> 7 from 1

Ex3
1 100 1
> 3

Ex4
30 20 10

"""
A = 0
B = 1
C = 2
WEEK = (A, B, C, A, C, B, A)
FULL = (3, 2, 2)


def find_best_start_day(abc):
    bestdays = 0
    beststart = None
    for start in range(len(WEEK)):
        # simulate:
        diddays = 0
        abccopy = abc[:]
        day_inx = start
        while True:
            food_type = WEEK[day_inx]
            if abccopy[food_type] == 0:  # end of journey
                break
            # can continue:
            abccopy[food_type] -= 1
            diddays += 1
            day_inx = (day_inx + 1) % len(WEEK)
        if diddays > bestdays:
            bestdays = diddays
            beststart = start
    return beststart, bestdays


abc = [int(i) for i in input().strip().split(' ')]
days = 0
# Remove extra, if it can >2 weeks:
gap_weeks = 2
has_much_food = all(e > (max(FULL) * gap_weeks) for e in abc)
if has_much_food:
    # Find min weeks we can go. Thus find min food to eat:
    inx = 0
    min_weeks = (abc[0] - FULL[0] * gap_weeks) // FULL[0]
    for i, food in enumerate(abc):
        thisweeks = (abc[i] - FULL[i] * gap_weeks) // FULL[i]
        if thisweeks < min_weeks:
            min_weeks = thisweeks
            inx = i
    assert min_weeks >= 1
    for i, food in enumerate(abc):
        abc[i] = food - min_weeks * FULL[i]
    days += min_weeks * len(WEEK)

start_day, diddays = find_best_start_day(abc)
days += diddays
print(days)
