#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 4. Add method to find the height of binary search tree. Provide test cases.
#################################################################################################
from soln01 import traversals as bst

class htree(bst):

    def __init__(self):
        super().__init__()
    
    def height(self):
        if not self.isEmpty():
            return self._ht_(self.root)
    
    def _ht_(self,node):
        if node == None:
            return 0
        else:
            return 1 + max(self._ht_(node.left),self._ht_(node.right))