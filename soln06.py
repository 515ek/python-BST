#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 6. Add methods to find max and min element in BST. Provide test cases.
#################################################################################################
from soln01 import traversals as bst

class minmaxtree(bst):

    def __init__(self):
        super().__init__()
    
    def minNode(self):
        if not self.isEmpty():
            return self._min_(self.root)
    
    def _min_(self,node):
        if node.left is not None:
            return self._min_(node.left)
        else:
            return node.data
    
    def maxNode(self):
        if not self.isEmpty():
            cur = self.root
            while cur.right is not None:
                cur = cur.right
            else:
                return cur.data