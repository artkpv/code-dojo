#!python3


def isgood(s, previous, lo, width):
    if lo >= len(s):
        return True
    if s[0] == '0' and width > 1:
        return False
    value = int(s[lo:lo+width])
    if previous is not None and value - previous != 1:
        return False
    for nextwidth in (width, width+1):
        if isgood(s, value, lo+width, nextwidth):
            return True
    return False


def get_first_good(s):
    widths = list(range(1, len(s)//2 + 1))
    for width in widths:
        if isgood(s, None, 0, width):
            return s[0:width]
    return None


for query in range(int(input('').strip())):
    input_ = input('').strip()
    first = get_first_good(input_)
    print(('YES %s' % first) if first is not None else 'NO')
