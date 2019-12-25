# quicksort
# partitions array by p , putting it on its needed place

import random

def select(a, k, lo, hi):
    if lo >= hi:
        return a[hi]
    m = (lo+hi)//2
    pivot = a[m]
    i = lo
    j = hi
    while i <= j:
          while a[i] < pivot:
              i += 1
          while a[j] > pivot:
              j -= 1
          if i <= j:
              a[i], a[j] = a[j], a[i]
              i += 1
              j -= 1

    # a[lo..i-1] <= a[i] == pivot <= a[i+1..hi]
    if i == k:
        return a[i]
    if k < i:
        return select(a, k, lo, i-1)
    else:
        return select(a, k, i+1, hi)

if __name__ == '__main__':
    assert(select([5,4,3,2,1], 2, 0, 4) == 3)
    assert(select([5,4,3,2,1], 1, 0, 4) == 2)
    a = list(reversed(range(1, 1001)))
    random.shuffle(a)
    assert(select(a, 23, 0, len(a)-1) == 24)

