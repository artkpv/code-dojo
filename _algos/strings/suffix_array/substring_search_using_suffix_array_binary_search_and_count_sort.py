'''
Suffix sort for substring search.

Problem: Given text of N size and pattern of M size find substring in the text that matches the pattern. N >= M. To match pattern right end continues at left.

Idea 1
1. Sort suffixes. 
    - Count sort for each i-th char. - N*W
2. Binary search for substring. 
    - log(N)
Time: O(N*N).   In real N*log(N)? 
Space: N

'''

def ss_search(text, pattern):
    if not text:
        return -1
    if not pattern:
        return -1
    RADIX = ord('Z') - ord('A') + 1
    N = len(text)
    M = len(pattern)
    suffixes = list(range(N))
    def charat(i):
        return text[i % N]
    def sort_():
        aux = [0] * N
        def myord(c):
            assert 'A' <= c <= 'Z', 'only upper case chars'
            return ord(c) - ord('A')
        def sort__(lo, hi, d):
            if d == N or hi <= lo:
                return
            count = [0] * (RADIX+1)
            for i in range(lo, hi+1):
                count[myord(charat(suffixes[i] + d)) + 1] += 1
            indexes = [0] * (RADIX+1)
            for i in range(1, len(count)):
                count[i] += count[i-1]
                indexes[i] = count[i]
            for i in range(lo, hi+1):
                k = myord(charat(suffixes[i] + d))
                j = count[k]
                count[k] += 1
                aux[lo + j] = suffixes[i]
            for i in range(lo, hi+1):
                suffixes[i] = aux[i]
            for i in range(1, len(indexes)):
                sort__(lo+indexes[i-1], lo+indexes[i] - 1, d+1)
        sort__(0, N-1, 0)
    def search_():
        ttext = text + text
        def getsuffix(i):
            j = suffixes[i]
            return ttext[j: j + M]
        def compare(left, right):
            for i in range(min(len(left), len(right))):
                d = ord(left[i]) - ord(right[i])
                if d != 0:
                    return d
            return len(left) - len(right)
        if pattern[0] < text[suffixes[0]]:
            return -1
        if pattern == getsuffix(0):
            return suffixes[0]
        l = 0
        r = N
        # Invariant: suffix at l < pattern <= suffix at r
        while r - l > 1:
            m = (r + l) // 2
            d = compare(getsuffix(m), pattern)
            if d < 0:
                l = m
            elif d > 0:
                r = m
            else:
                return suffixes[m]
        if r == N:
            return -1
        if getsuffix(r) != pattern:
            return -1
        return suffixes[r]

    sort_()
    return search_()


def myassert(t, p, expectedinx):
    print(f'TEST: "{t}", "{p}"')
    r = ss_search(t, p)
    assert r == expectedinx, f'{r} result, {expectedinx} expected.'
    if r != -1:
        assert (t+t)[r:r+len(p)] == p, f' {(t+t)[r:r+len(p)]} failed' 
    print('PASS')

#         01234567890
myassert('ABRACADABRA', 'ABRACA', 0)
myassert('ABRACADABRA', 'ABRA', 0)
myassert('ABRACADABRA', 'CADA', 4)
myassert('ABRACADABRA', 'AA', 10)
myassert('ABRACADABRA', 'AABRA', 10)
myassert('ABRACADABRA', 'A', 10)
myassert('ABRACADABRA', '', -1)
myassert('ABRACADABRA', 'Z', -1)
myassert('ABRACADABRA', 'ZAB', -1)
