#!python3

"""
3-way string quicksort (by chars)

TIME:
    N strings of the same W length.
    W*N + 2*N*log(N) chars compare.
    Quicksort: W*2*N*Log(N) chars compare. ~2*log(N) more!

    Master theorem:
        T(n) = ~n + 3*T(n/3)  ~ best partition every time
        n*log(n) <=  n ~= n^log(3, 3) = n
    Recursition tree:
        3^i - each level, num of calls: 1 3 9 27 81 ..
        3^h/n = 1  => h = log(3,n)
        n CHARS compare at each level
        n * log(3,n)  --  CHARS compare

Space: ~1


"""

import random


def sort(array, lo, hi, inx):
    if lo >= hi:
        return
    # Partition array of strings by i-th char, stable
    # Time ~ n to compare CHARS at i-th position
    suitable = (w for w in array[lo:hi+1] if inx < len(w))
    pivot = next(suitable, None)
    if pivot is None:
        return
    lt = lo-1
    gt = hi+1
    i = lo
    while i < gt:
        difference = compare(array[i], pivot, inx)
        if difference < 0:
            lt += 1
            array[i], array[lt] = array[lt], array[i]
            i += 1
        elif difference > 0:
            gt -= 1
            array[i], array[gt] = array[gt], array[i]
        else:  # the same
            i += 1

    # Invariant, by inx:
    #     array[lo..lt] < pivot = array[lt+1..gt-1] < array[gt..hi]

    # Repeat recursively for left, equal, right parts
    sort(array, lo, lt, inx)  # the same inx
    sort(array, lt+1, gt-1, inx+1)  # as all at inx are equal
    sort(array, gt, hi, inx)
    return array


def compare(left, right, inx):
    if inx >= len(left) and inx >= len(right):
        return 0
    elif inx >= len(left):
        return -1
    elif inx >= len(right):
        return 1
    return ord(left[inx]) - ord(right[inx])


#
#  =====================================
#              TESTS
#  =====================================
#


def isequal(left, right):
    if left != right:
        assert False, 'Expected: %s == %s' % (left, right)


if __name__ == '__main__':
    isequal(sort(['bbb', 'ccc', 'aaa'], 0, 2, 0), ['aaa', 'bbb', 'ccc'])
    isequal(sort(['a', 'a', 'a'], 0, 2, 0), ['a', 'a', 'a'])
    isequal(sort([
        'abd', 'abc', 'abe'
    ], 0, 2, 0), [
        'abc', 'abd', 'abe'
    ])

    # Random load test

    generator = random.Random()
    N = 10**5
    array = []
    width = 30
    for i in range(N):
        array += [''.join(chr(generator.randint(ord('a'), ord('z')))
                  for i in range(generator.randint(1, width)))]
    expected = array.copy()

    expected.sort()

    sort(array, 0, len(array)-1, 0)

    isequal(array, expected)

    print('all tests pass')
