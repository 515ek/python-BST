#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 2. Add methods to in-order, pre-order, post-order and level-order traversals
#################################################################################################
from mclass import BST as bst
import user_ds as uds
import random

class traversals(bst):

    def __init__(self):
        super().__init__()
        #self.data = []

    def inorder(self):
        self.inls = []
        if not self.isEmpty():
            self._inorder_(self.root)
        return self.inls
    
    def _inorder_(self,node):
        if not node is None:
            self._inorder_(node.left)
            #print(node.data)
            self.inls.append(node.data)
            self._inorder_(node.right)
    
    def preorder(self):
        self.prels = []
        if not self.isEmpty():
            self._preorder_(self.root)
        return self.prels
    
    def _preorder_(self,node):
        if not node is None:
            #print(node.data)
            self.prels.append(node.data)
            self._preorder_(node.left)
            self._preorder_(node.right)
    
    def postorder(self):
        self.postls = []
        if not self.isEmpty():
            self._postorder_(self.root)
        return self.postls
    
    def _postorder_(self,node):
        if not node is None:
            self._postorder_(node.left)
            self._postorder_(node.right)
            #print(node.data)
            self.inls.append(node.data)
    
    def levelorder(self):
        self.levells = []
        que = uds.flexQueue()
        que.enque(self.root)
        self._levelorder_(que)
        return self.levells
    
    def _levelorder_(self,que):
        if not que.isEmpty():
            temp = que.deque()
            print(temp.data)
            self.levells.append(temp.data)
            if not temp.left is None:
                que.enque(temp.left)
            if not temp.right is None:
                que.enque(temp.right)
            self._levelorder_(que)
