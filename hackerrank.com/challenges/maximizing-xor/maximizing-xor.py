#!python3
def maxXor(l, r):
  max_ = 0
  for i in range(l, r+1):
    for j in range(i+1, r+1):
      if max_ < i^j:
        max_ = i^j
  return max_

if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
