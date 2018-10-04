#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 5. Add method to count the number of terminal nodes in BST. Provide test cases.
#################################################################################################
from soln01 import traversals as bst

class leaftree(bst):

    def __init__(self):
        super().__init__()
    
    def leaves(self):
        if not self.isEmpty():
            return self._leaf_(self.root)
    
    def _leaf_(self,node):
        if node.left is not None and node.right is not None:
            return self._leaf_(node.left) + self._leaf_(node.right)
        elif node.left is not None:
            return self._leaf_(node.left)
        elif node.right is not None:
            return self._leaf_(node.right)
        else:
            return 1