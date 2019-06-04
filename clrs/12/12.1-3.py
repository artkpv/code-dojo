#! python3

# Ex. 12.1-3

def inorder_linear(bst):
    """
       3
     1   5

             10
        5         15
      1   7    13    19

    s:
    10 5 1
    10 5  | 1
    10    | 1 5
    10 7  | 1 5
    10

             10
         5         15
      1    7    13    19
        3

    """

    s = []
    v = bst.root
    inorder = []
    while v != None or len(s) > 0:
        while v != None:
            s += [v]
            v = v.left
        v = s.pop()
        inorder += [v]
        v = v.right
    return inorder



from bst import BST
bst = BST()
bst.put(10)
bst.put(9)
bst.put(8)
bst.put(3)
bst.put(6)
bst.put(5)
bst.put(4)
print([i.value for i in inorder_linear(bst)])

