#!python3

k, n = [int(i) for i in input().strip().split(' ')]
cards = [int(i) for i in input().strip().split(' ')]

def play():
    petya = 0
    vasya = 0
    for c in cards:
        if c % 6 == 0 and c % 9 == 0:
            petya = max(0, petya - 1)
            vasya = max(0, vasya - 1)
        elif c % 6 == 0:
            vasya += 1
        elif c % 9 == 0:
            petya += 1
        if vasya == k and petya == k:
            return 'Draw'
        elif vasya == k:
            return 'Vasya'
        elif petya == k:
            return 'Petya'
    if petya == vasya:
        return 'Draw'
    return 'Petya' if petya > vasya else 'Vasya'
print(play())


