#!python3
# run please

def count(s):
    radix = ord('z') - ord('a') + 1
    result = [0] * radix
    for c in s:
        result[ord(c) - ord('a')] += 1
    return result


left = input('').strip()
right = input('').strip()
print('1' if count(left) == count(right) else '0')
