#!python3


def asc(a, i, j):
    if not (0 <= i < len(a)) or not (0 <= j < len(a)):
        return True
    return a[i] < a[j]


def getreverse(a, i):
    j = i + 1
    n = len(a)
    while j < n and not asc(a, j-1, j):
        j += 1
    j -= 1
    if j - i == 1:  # it is swap
        return None
    if asc(a, i-1, j) and asc(a, i, j+1):  # both ends are good
        return (i, j)
    return None  # some ends are bad


def getswap(a, i):
    j = i+1
    while j < len(a) and a[j] < a[i]:
        if not asc(a, j, j+1):
            j += 2
            break
        j += 1
    j -= 1
    # is good?
    if j - i == 1:
        inasc = asc(a, i-1, j) and asc(a, i, j+1)
    else:
        inasc = (asc(a, i-1, j) and asc(a, j, i+1) and
                 asc(a, j-1, i) and asc(a, i, j+1))
    if inasc:
        return (i, j)
    else:
        return None  # bad swap


def cansort(a, n):
    reverse = None
    swap = None
    i = 0
    while i < len(a):
        if not asc(a, i-1, i):
            if reverse or swap:
                return (False, None, None)
            reverse = getreverse(a, i-1)
            if not reverse:
                swap = getswap(a, i-1)
            if not reverse and not swap:  # both bad
                return (False, None, None)
            i = (reverse or swap)[1] + 1
        else:
            i += 1
    return (True, reverse, swap)


def getresult(a, n):
    can, reverse, swap = cansort(a, n)
    result = 'yes' if can else 'no'
    if can and (reverse or swap):
        result += '\n'
        result += 'swap' if swap else 'reverse'
        left, right = (reverse or swap)
        result += ' %d %d' % (left+1, right+1)
    return result


n = int(input('').strip())
array = [int(i) for i in input('').strip().split(' ')]
print(getresult(array, n))
