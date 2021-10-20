'''
rabin-karp. Based on hash.. !

'''


def rabin_karp_ssearch(text, pattern):
    m = len(pattern)
    n = len(text)
    if not text or m > n:
        return -1
    if not pattern:
        return 0
    R = 31
    def charo(c):
        return ord(c) - ord('a')
    phash = sum(charo(c)*R**i for i, c in enumerate(reversed(pattern)))
    thash = sum(charo(c)*R**i for i, c in enumerate(reversed(text[:m])))
    i = m
    while i < n and phash != thash:
        thash = (thash - charo(text[i-m])*R**(m-1)) * R + charo(text[i])  # m=3, i = 3 , thash - text[i-m=0]*R**2 ) * R + text[i] 
        i += 1
    assert i == n or phash == thash
    return i - m if phash == thash else -1

def rbss_test(t, p, e):
    r = rabin_karp_ssearch(t, p)
    print(f'test: {t} {p} {e}?={r}')
    assert r == e, r

rbss_test('abcde', 'bc', 1)
rbss_test('abracadabra', 'abra', 0)
rbss_test('abracadabra', 'cadab', 4)
rbss_test('abracadabra', 'abrac', 0)
rbss_test('abracadabra', 'abdra', -1)
rbss_test('', 'abdra', -1)
rbss_test('abde', 'abdra', -1)
rbss_test('abrad', '', 0)



def robin_moure_ssearch(text, pattern):
    '''

    Try to avoid backtracking problem by not restarting at the next if possible.

    O(n*m) . Worst - all in the pattern.
    S: O(m)
    '''

    if not text:
        return -1
    if not pattern:
        return 0
    chars = set(pattern)
    m = len(pattern)
    n = len(text)
    for i in range(n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        assert j == m or text[i+j] != pattern[j]
        if j == m:
            return i
        elif text[i+j] not in chars:
            i = i+j+1
        else:
            i += 1  # Possible to have DFA (determ, finite state automaton.
    return -1

def test(t, p, e):
    r = rabin_karp_ssearch(t, p)
    print(f'test: {t} {p} {e}?={r}')
    assert r == e, r

test('abracadabra', 'abra', 0)
test('abracadabra', 'cadab', 4)
test('abracadabra', 'abrac', 0)
test('abracadabra', 'abdra', -1)
test('', 'abdra', -1)
test('abrad', '', 0)


