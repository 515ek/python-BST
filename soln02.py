#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 3. Add methods to display the traversal in ascending and descending order
#################################################################################################
from soln01 import traversals as bst

class ascdscTree(bst):

    def __init__(self):
        super().__init__()
    
    def ascTraverse(self):
        self.ls = super().inorder()
        return self.ls
    
    def descTraverse(self):
        self.ls = super().inorder()
        self.ls.reverse()
        return self.ls