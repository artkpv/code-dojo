#!python3


def isgood(s):
    if not s:
        return True
    char_to_frequency = {}  # char_to_frequency[char] = number of occurencies
    for c in s:
        if c in char_to_frequency:
            char_to_frequency[c] += 1
        else:
            char_to_frequency[c] = 1
    frequency_to_chars = {}  # occurencies to number of chars with it
    for char in char_to_frequency:
        amount = char_to_frequency[char]
        if amount in frequency_to_chars:
            frequency_to_chars[amount] += 1
        else:
            frequency_to_chars[amount] = 1
    if len(frequency_to_chars) == 1:
        return True
    if len(frequency_to_chars) > 2:
        return False
    # now only two groups of chars
    keys = iter(frequency_to_chars.keys())
    first = next(keys)
    second = next(keys)
    assert abs(first - second) != 0
    # Can get rid of a char? 2 cases when we remove one char:
    if first == 1 and frequency_to_chars[first] == 1:
        return True
    if second == 1 and frequency_to_chars[second] == 1:
        return True
    # now we can't get rid of a char group
    if abs(first - second) > 1:
        return False
    if first - second == 1 and frequency_to_chars[first] != 1:
        return False
    if second - first == 1 and frequency_to_chars[second] != 1:
        return False
    return True


s = input('').strip()
print('YES' if isgood(s) else 'NO')
