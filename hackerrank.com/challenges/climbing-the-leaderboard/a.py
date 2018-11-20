#!python3

n = int(input().strip())
scores = list(sorted(set(int(i) for i in input().strip().split(' ')), reverse=True))
m = int(input().strip())
alice = [int(i) for i in input().strip().split(' ')]

rank = len(scores)+1
for i in alice:
    while rank > 1 and scores[rank-2] <= i:
        rank -= 1
    print(rank)
