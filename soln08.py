#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 8. Add method to count number of nodes in the left sub tree and number of nodes in right sub tree. Provide test cases.
#################################################################################################
from soln01 import traversals as bst

class subtree(bst):

    def __init__(self):
        super().__init__()
    
    def leftsubTree(self):
        if not self.isEmpty():
            return self._subtree_(self.root.left)
    
    def rightsubTree(self):
        if not self.isEmpty():
            return self._subtree_(self.root.right)

    def _subtree_(self,node):
        if node.left is not None and node.right is not None:
            return 1 + self._subtree_(node.left) + self._subtree_(node.right)
        elif node.left is not None:
            return 1 + self._subtree_(node.left)
        elif node.right is not None:
            return 1 + self._subtree_(node.right)
        else:
            return 1