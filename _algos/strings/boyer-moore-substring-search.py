#!python3
"""

Boyer-Moore substring search

"""

def search(s, p, radix):
    print('search "%s" in "%s"' % (p, s))
    n = len(s)
    m = len(p)
    right = [-1] * radix
    def ch2ord(ch):
        return ord(ch) - ord('a')
    for i in range(m):
        right[ch2ord(p[i])] = i

    i = 0
    while i <= n-m:
        skip = 0
        for j in range(m-1, -1, -1):
            if s[i+j] == p[j]:
                continue
            else:
                r = right[ch2ord(s[i+j])]
                if r == -1: skip = 1
                else: skip = max(1, j - r)
        if skip == 0:
            print(' found: %d' % i)
            return i
        i += skip
    print(' not found')
    return None


if __name__ == '__main__':
    assert(search('a', 'a', 26) == 0)
    assert(search('ba', 'a', 26) == 1)
    """
    baab  ->   baab
    aab         aab
    """
    assert(search('baab', 'aab', 26) == 1)
    assert(search('xxxxxexxneedle', 'needle', 26) == 8)
    assert(search('eedle', 'needle', 26) == None)
