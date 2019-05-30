#!python3

"""

"""

from collections import Counter, defaultdict
k = int(input().strip())
games = Counter()
game_pairs = defaultdict(set)
for i in range(2**k-1):
    left, right = input().strip().split(' ')
    games[left] += 1
    game_pairs[left].add(right)
    games[right] += 1
    game_pairs[right].add(left)

def top_two():
    level = 0
    common = games.most_common()
    common_inx = 0
    # first level:
    if common[0][1] != k or common[1][1] != k:
        return None, None
    level += 1
    common_inx += 2
    # from second till last - 1:
    while level < k - 1:
        pairs = 2**level
        gamers = pairs
        expected_games = k - level
        for i in range(gamers):
            current = common[common_inx + 1]
            if current[1] != expected_games:
                return None, None
            # should have played with higher gamer:
            max_player = max(games[p] for p in game_pairs[current[0]])
            if max_player <= current[1]:
                return None, None
        common_inx += gamers
        level += 1
    # last level:
    for i in range(2**(k-1)):
        if common[common_inx + i][1] != 1:
            return None, None
    return common[0][0], common[1][0]

left, right = top_two() 
print(' '.join([left, right]) if left else 'NO SOLUTION')




