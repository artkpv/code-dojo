
# What's a Perfect Power anyway?
# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python
# https://en.wikipedia.org/wiki/Perfect_power

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59, 61,67,71,73,79,83,89,97,101,103,107,109,113,127, 131,137,139,149,151,157,163,167,173,179,181,191, 193,197,199,211,223,227,229,233,239,241,251,257, 263,269,271]

def next_div(n , d) :
  inx = primes.index(d) if d is not None else -1

  while inx < len(primes) - 1:
    inx += 1
    d = primes[inx]
    if d > n :
      return None
    if n % d == 0 :
      return d

  raise Exception('Not enough primes')

def isPP(n):
  print('isPP, n = ' + str(n))
  if n == 1 : return [1,1]

  m = None
  while True:
    m = next_div(n, m)
    if m is None:
      break

    k = 2
    while True :
      if n == m ** k :
        return [m, k]
      elif n < m ** k :
        break
      k += 1

  return None

# TODO: see this tests
'''
Time: 100ms Passed: 20 Failed: 6
Test Results:
  perfect powers
  should work for some examples
isPP, n = 4
✔  Test Passed
isPP, n = 9
✔  Test Passed
isPP, n = 5
✔  Test Passed
  should work for the first perfect powers
isPP, n = 4
✔  Test Passed
isPP, n = 8
✔  Test Passed
isPP, n = 9
✔  Test Passed
isPP, n = 16
✔  Test Passed
isPP, n = 25
✔  Test Passed
isPP, n = 27
✔  Test Passed
isPP, n = 32
✔  Test Passed
isPP, n = 36
✘  the perfect power 36 wasn't recognized as one
isPP, n = 49
✔  Test Passed
isPP, n = 64
✔  Test Passed
isPP, n = 81
✔  Test Passed
isPP, n = 100
✘  the perfect power 100 wasn't recognized as one
isPP, n = 121
✔  Test Passed
isPP, n = 125
✔  Test Passed
isPP, n = 128
✔  Test Passed
isPP, n = 144
✘  the perfect power 144 wasn't recognized as one
isPP, n = 169
✔  Test Passed
isPP, n = 196
✘  the perfect power 196 wasn't recognized as one
isPP, n = 216
✘  the perfect power 216 wasn't recognized as one
isPP, n = 225
✘  the perfect power 225 wasn't recognized as one
isPP, n = 243
✔  Test Passed
isPP, n = 256
✔  Test Passed
isPP, n = 289
✔  Test Passed
isPP, n = 324

'''




from random import random, randrange
from math import log, floor

Test.describe("perfect powers")
Test.it("should work for some examples")
Test.assert_equals(isPP(4), [2,2], "4 = 2^2")
Test.assert_equals(isPP(9), [3,2], "9 = 3^2")
Test.assert_equals(isPP(5), None, "5 isn't a perfect power")

Test.it("should work for the first perfect powers")
pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
for item in pp:
    Test.expect(isPP(item) != None, "the perfect power "+str(item)+" wasn't recognized as one")

Test.it("should work for random perfect powers")
for i in range(100):
    m = 2 + floor(random() * 255)
    k = 2 + floor(random() * log(268435455) / log(m))
    l = m**k
    r = isPP(l)
    if r==None:
        Test.expect(r != None, str(l) + " is a perfect power")
        break
    elif r[0]**r[1] != l:
        Test.assert_equals(r[0]**r[1], l, "your pair (" + str(r[0]) + ", "+ str(r[1])+ ") doesn't work for "+ str(l))
        break


Test.it("should return valid pairs for random inputs")
for i in range(100):
    l = randrange(65535);
    r = isPP(l);
    if r != None and r[0]**r[1] != l:
        Test.assert_equals(r[0]**r[1], l, "your pair ("+str(r[0])+", "+str(r[1])+") doesn't work for "+str(l))
        break
