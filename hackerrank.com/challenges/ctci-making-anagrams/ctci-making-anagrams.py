#!python3

def number_needed(a, b):
    radix = ord('z') - ord('a') + 1
    base = ord('a')
    a_d = [0] * radix
    b_d = [0] * radix
    for c in a:
        a_d[ord(c) - base] += 1
    for c in b:
        b_d[ord(c) - base] += 1
    deletions = 0
    for i in range(radix):
        if a_d[i] != b_d[i]:
            deletions += max(b_d[i], a_d[i]) - min(b_d[i], a_d[i])
    return deletions


a = input().strip()
b = input().strip()

print(repr(number_needed(a, b)))
