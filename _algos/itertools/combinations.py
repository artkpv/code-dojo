#!python3
"""
  Unordered k-subset from n-set
"""

def combinations(k, n):
  """
  2 3
    1 2
    1 3
    2 3
  3 4,  4*3*2/(3*2*1) = 4
    1 2 3
    1 2 4
    1 3 4
    2 3 4
  2 5, 10
    1 2..5
    2 3..5
    3 4..5
    4 5
  """
  assert(n >= k)
  c = [i for i in range(1, k+1)]
  while True:
    yield tuple(c)
    # next:
    for j in range(k-1,-1,-1):
      if c[j] + 1 <= n and (j == k-1 or c[j] + 1 < c[j+1]):
        c[j] += 1
        for jj in range(j+1, k):
          c[jj] = c[jj-1] + 1
        break
    else:
      break

if __name__ == "__main__":
  print("Start")
  assert(list(combinations(1, 1)) == [(1,)])
  assert(list(combinations(1, 2)) == [(1,), (2,)])
  assert(list(combinations(2, 2))== [(1, 2)])
  assert(list(combinations(2, 3)) == [(1, 2), (1, 3), (2, 3)])
  assert(list(combinations(3, 6)) == [
    (1,2,3),(1,2,4),(1,2,5),(1,2,6),(1,3,4),(1,3,5),(1,3,6),(1,4,5),(1,4,6),(1,5,6),
    (2,3,4),(2,3,5),(2,3,6),(2,4,5),(2,4,6),(2,5,6),
    (3,4,5),(3,4,6),(3,5,6),
    (4,5,6)])

  print("Time")
  import timeit, itertools
  r = timeit.timeit("assert(sum(1 for _ in itertools.combinations(range(50), 5)) == 2118760)",
    number=10, setup="import itertools")
  print(" itertools.combinations(..): %.4f" % r)
  r2 = timeit.timeit("assert(sum(1 for _ in combinations(5,50)) == 2118760)", 
    number=10, setup="from __main__ import combinations")
  print(" combinations(..): %.4f (%.2f times longer)" % (r2, r2/r))

  print("Done")
