#!python3
"""
k-element permutations from n-element set.
"""

def quicksort(a, l, r):
    def partition(a, l, r):
        m = (l+r)//2
        a[m], a[r] = a[r], a[m]
        p = a[r]
        i = l
        j = r-1
        while i <= j:
            while a[i] <= p:
                if i == r:
                    break
                i += 1
            while a[j] >= p:
                if j == l:
                    break
                j -= 1
            if i > j:
                break
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        a[r], a[i] = a[i], a[r]
        return i
    if l >= r: return 
    m = partition(a, l, r)
    quicksort(a, l, m-1)
    quicksort(a, m+1, r)

def permutations(n, k):
    """
    Creates a generator for k-element permutations on n-element set.

    Examples:
        n = 3, k = 2
            0 1  2
            0 2  1
            1 0  2
            1 2  0
            2 0  1
            2 1  0

    """
    def next_permutation(a):
        # Finds first two in asc from right, exchange with its next and sort remaining.
        i = n-2
        while i >= 0 and not a[i] < a[i+1]:
            i -= 1
        if i < 0:
            return i  # no next permutation

        ii = i+1  # min a[ii] where a[ii] > a[i] for ii in i+1..n-1
        for j in range(i+1, n):
            if a[j] > a[i] and a[j] < a[ii]:
                ii = j
        a[i], a[ii] = a[ii], a[i]
        quicksort(a, i+1, n-1)
        return i

    if k > n or k == 0:
        return
    a = list(range(n))
    while True:
        yield tuple(a[:k]) 
        while True:
            i = next_permutation(a)
            if i >= k:  # skip as not in k-el permutation
                continue
            elif i == -1:  # nothing changed
                return None
            else:  # found next
                break


#
# ================================  TESTS ====================================
#

def test_edge_cases():
    assert(len(list(permutations(1,1))) == 1)
    assert(len(list(permutations(10,11))) == 0)
    assert(len(list(permutations(1,0))) == 0)
    assert(len(list(permutations(0,1))) == 0)

def test_simple():
    assert(list(permutations(3, 2)) == [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)])

if __name__ == "__main__":
    test_edge_cases()
    test_simple()

    import sys
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        for p in permutations(n, k):
            print(p)
        