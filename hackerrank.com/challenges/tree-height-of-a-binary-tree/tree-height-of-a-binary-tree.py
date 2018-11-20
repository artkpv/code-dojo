#!python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(v):
    if v.left or v.right:
        return 1 + max(
                height(v.left) if v.left else 0,
                height(v.right) if v.right else 0)
    else:
        return 0

