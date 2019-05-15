#!python3
"""

TODO



Test  Result
1 1 > 1 1 or 0 0
1 0 > 0 0 or 0 1
0 1 > 0 0 or 1 0
0 0 > 0 0 or 1 0 or 0 1



EXAMPLE 1
Chips: 3
Good / Bad: 2 / 1
Min number of tests ?
2

Chip tests:
1 2 0 0


EXAMPLE 2
7 chips, good / bad = 4 / 3
? ? ? ? ? ? ?
Count pairs with 0 0, 0 1, 1 0
Pairs with 1 1


"""

from random import random


GOOD = 0
ALLGOOD = 1
ALLBAD = 2
TOGGLE = 3


class Tester(object):
    def __init__(self, chips):
        self.chips = [
            GOOD if isgood else random(ALLGOOD, TOGGLE+1)
            for isgood
            in chips
        ]

    def test(self, left, right):
        c = self.chips

        def signal(a, b):
            if c[a] == GOOD:
                return c[b] == GOOD
            elif c[a] == ALLGOOD:
                return True
            elif c[a] == ALLBAD:
                return False
            elif c[a] == TOGGLE:
                return c[b] != GOOD
            else:
                raise Exception('undefined')
        return signal(left, right), signal(right, left)


class Solver(object):
    def __init__(self, good, bad, tester):
        self.solution = None
        chipsnum = good+bad
        if bad > chipsnum//2:
            return
        atleastbads = 0
        for i in range(chipsnum, 2):
            if i + 1 >= chipsnum:
                break
            left, right = tester.test(i, i+1)
            if not (left and right):
                atleastbad += 1





if __name__ == '__main__':
    # Example 1
    chips = [True, True, False]  # 2 good, 1 bad
    tester = Tester(chips)
    solution = Solver(
        sum(c for c in chips),
        sum(not c for c in chips),
        tester
    ).solution
    print(tester.chips)
    print(solution)
    assert chips == solution


