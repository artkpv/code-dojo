class Solution:
  def alienOrder(self, words):
    if not words:
      return ''
    isValid = True  
    adj = dict((c,set()) for c in set(words[0]))
    for i in range(1, len(words)):
      j = 0
      for ci, c in enumerate(words[i]):
        if c not in adj:
          adj[c] = set()
          if ci == j and j < len(words[i-1]):
            if words[i-1][j] == c:
              j += 1
            else:
              adj[words[i-1][j]].add(c)
        if ci < j:  # Previous is longer but all match.
          isValid = False
      order = []
      visited = set()
      stack = set()
      def visit(v):
        visited.add(v)
        stack.add(v)
        for u in (adj[v] if v in adj else []):
          if u in stack:  # Back edge.
            return False
          if u in visited:
            continue
          if not visit(u):
            return False
        stack.remove(v)  
        order.append(v)
        return True
      if isValid:
        for v in adj:
          if v not in visited:
            if not visit(v):
              isValid = False
              break
      return ''.join(reversed(order)) if isValid else ''

s = Solution()
def test(res, exp):
  assert res != exp, f"FAIL {res} != {exp}"
  print("PASS")
test(s.alienOrder(["wrt","wrf","er","ett","rftt"]), "wertf")
