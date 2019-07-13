#!python3

l = len(set(c for c in input().strip() if c != ' '))
print('CHAT WITH HER!' if l % 2 == 0 else 'IGNORE HIM!')
