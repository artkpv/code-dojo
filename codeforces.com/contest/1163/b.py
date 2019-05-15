#!python3

import collections

n = [int(i) for i in input().strip().split(' ')]
U = [int(i) for i in input().strip().split(' ')]
longest = 1
counter = collections.Counter()

for i, u in enumerate(U):
    counter[u] += 1

    def issuit():
        if len(counter) == 1:
            return True
        mc = counter.most_common()
        if len(counter) == 2:
            if mc[-1][1] == 1:
                return True
            if mc[-2][1] - mc[-1][1] == 1:
                return True
            return False
        else:  # > 2
            uniques = set(counter.values())
            if len(uniques) > 2:
                return False
            if mc[-2][1] != 1 and mc[-1][1] == 1:
                return True
            if len(uniques) == 1:
                return False
            e1 = uniques.pop()
            e2 = uniques.pop()
            return abs(e1 - e2) == 1

    if issuit() and longest < i + 1:
        longest = i + 1

print(longest)
