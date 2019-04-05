#!python3
"""
1 <= rows, cols <= 200
1 <= seconds <= 10^9

t0 - plants
t1 -
t2 - plants
t3 - explode  - inverted
t4 - plants   ..
t5 - explode  - original
t6 - plants
t7 - explode
t8 - plants
..

k seconds

k // 3 = 0 - recursive ..

Idea 1
field = rows numbers

for sec in secs:
    ..
    if sec % 3 == 0:
        for row in rows:
            row = (!init[row+1]) & row
            row = (!init[row]<<1) & row
            row = (!init[row]>>1) & row
            row = (!init[row]) & row
            row = (!init[row-1]) & row

init mask  field  (!init)&field
1          1      0
1          0      0
0          0      0
0          1      1


"""


def tonum(s):
    num = 0
    for i in range(len(s)):
        if s[i] == chr(79):
            num |= 1
        if i != len(s) - 1:
            num <<= 1
    return num


def print_field(field, cols):
    for row in field:
        s = ''
        for c in range(cols):
            s += 'O' if row & (1 << (cols - c - 1)) else '.'
        print(s)


def plant_explode(field, rows, cols):
    """
field:
000
010
000

exploded:
010
111
010

new field:
101
000
101

    """
    exploded = [0]*rows
    # create explosion field:
    for i in range(rows):
        exploded[i] |= field[i]  # bombs itself
        if i > 0:
            exploded[i] |= field[i-1]  # upper
        if i < rows - 1:
            exploded[i] |= field[i+1]  # lower
        exploded[i] |= field[i] << 1  # left
        exploded[i] |= field[i] >> 1  # right
        # now exploded[i] has 1 for exploded and 0 for not
        # reverse (filled with bombs) and truncate:
        exploded[i] &= 2**(cols)-1  # truncate
        exploded[i] ^= 2**(cols)-1
    return tuple(exploded)


def getfilled(rows, cols):
    return (2**cols-1 for _ in range(rows))


#
# READ INPUT:
#
rows, cols, seconds = [int(i) for i in input().strip().split(' ')]
field = tuple(tonum(input().strip()) for _ in range(rows))
if seconds == 1:
    print_field(field, cols)
elif seconds % 2 == 0:  # plants all field before next explosion
    print_field(getfilled(rows, cols), cols)
else:  # seconds % 2 == 1
    cache = {field: 1}
    second = 1

    while second <= seconds:
        second += 2
        field = plant_explode(field, rows, cols)
        assert(second <= seconds)
        if second == seconds:
            break
        if field not in cache:
            cache[field] = second
        else:
            # it repeats: a .. a .. a .. a
            # so skip these intervals:
            before = cache[field]
            interval = second - before
            left = seconds - second
            second += interval * (left // interval)
            """
            Example 1:
                repeats at 1 3 5 ..
                seconds = 7
                at 3 finds it
                interval = 2
                left = 4
                next second = 3 + 2 *(4//2) = 3 + 4 = 7

            Example 2:
                repeats at 1 5 9 13 ..
                seconds = 15
                at 5 finds it
                interval = 4
                left = 10
                next second = 5 + 4 *(10//4) = 5 + 8 = 13

            """
    print_field(field, cols)
