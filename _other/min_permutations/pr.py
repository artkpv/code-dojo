
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def hash(arr):
  return sum(e*8**i for i, e in enumerate(arr))

from collections import deque
def issorted(arr):
  for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
      return False
  return True

def minOperations(arr):
  if not arr:
    return 0
  if issorted(arr):
    return 0
  n = len(arr)
  dp = {}
  q = deque()
  q.append((arr,0))
  res = None
  while res is None:
    arr, ops = q.popleft()
    for size in range(2, n+1):
      for i in range(n-size+1):
        b = arr.copy()
        b[i:i+size] = reversed(b[i:i+size])
        if issorted(b):
          res = ops + 1
        q.append((b, ops+1))
  return res








# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here

