#! python3

class Node:
    def __init__(self, v, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = v

class BST:
    def __init__(self, root=None):
        self.root = root

    def put(self, v):
        self.root = self._put(self.root, v)

    def _put(self, x, v):
        if x is None:
            return Node(v, 1)
        if v < x.value:
            x.left = self._put(x.left, v)
        elif x.value < v:
            x.right = self._put(x.right, v)
        else:
            x.value = v
        return x

    def get_min(self):
        return self._get_min(self.root)

    def _get_min(self, x):
        if x.left is None:
            return x.value
        return self._get_min(x.left)

    def delete_min(self):
        if self.root is not None:
            self.root = self._delete_min(self.root)

    def _delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self._delete_min(x.left)
        return x

    def get_max(self):
        return self._get_max(self.root)

    def _get_max(self, x):
        if x.right is None:
            return x.value
        return self._get_max(x.right)

    def delete_max(self):
        if self.root is not None:
            self.root = self._delete_max(self.root)

    def _delete_max(self, x):
        if x.right is None:
            return x.left
        x.right = self._delete_max(x.right)
        return x

