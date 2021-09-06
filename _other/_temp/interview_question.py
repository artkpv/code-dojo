

class Node:
  def __init__(self, s, e, maxend):
    self.s = s
    self.e = e
    self.maxe = maxend
    self.left = None
    self.right = None

  def __str__(self):
      return f"<Node {self.s} {self.e} {self.maxe}"

    
class Searcher:
  
  def __init__(self, ranges):
    self.root = None
    for s, e in ranges:
      s, e = (s, e) if s < e else (e, s)
      self.root = self._add(self.root, s, e)  

  def search(self, x):
    def visit(v):
      # print(f"visit {v}")
      if not v:
        return False
      if v.s <= x <= v.e:
        return True
      if x < v.s: 
        return visit(v.left)
      elif v.s < x and x <= v.maxe:
        return visit(v.right)
      return False
    return visit(self.root)
    
  def _add(self, v, s, e):
    if v == None:
      v = Node(s, e, e)
      return v 
    v.maxe = max(v.maxe, e)
    if v.s >= s:
      v.left = self._add(v.left, s, e)
    else: 
      assert v.s < s      
      v.right = self._add(v.right, s, e)
    return v
      

s = Searcher([
    [1,50],
    [99, 100],
    [20, 48],
    [20, 20],
    [75, 90]
])

for x in (
    1,50,51, 74, 75,76, 100
):
    r = s.search(x)
    print(f"searching {x}: {r}")

