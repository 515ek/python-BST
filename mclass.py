#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: Create a Class BST to implement the working of Binary Search Tree DataStructure.
#################################################################################################

class BST:

    class _Node:

        def __init__(self,el):
            self.left = None
            self.right = None
            self.data = el

    def __init__(self):
        self.root = None
        self.count = 0
    
    def isEmpty(self):
        return self.root == None
    
    def add(self,element):
        current = parent = self.root
        
        while current != None and current.data != element:
            parent = current
            if element < current.data:
                current = current.left
            elif element > current.data:
                current = current.right
        
        if current is None:
            nn = self._Node(element)
            if parent is None:
                self.root = nn
            elif element < parent.data:
                parent.left = nn
            elif element > parent.data:
                parent.right = nn
        
        self.count += 1
    
    def node_count(self):
        return self.count
    
    def lookup(self,key):
        if not self.isEmpty():
            cur = self.root
            while cur is not None:
                if key == cur.data:
                    return True
                elif key > cur.data:
                    cur = cur.right
                elif key < cur.data:
                    cur = cur.left
            else:
                return False
    
    def delete(self,key):
        if not self.isEmpty():
            self.root = self._del_(self.root,key)
    
    def _del_(self,node,key):
        if node is None:
            return node
        elif key < node.data:
            node.left = self._del_(node.left,key)
        elif key > node.data:
            node.right = self._del_(node.right,key)
        
        elif node.left and node.right:
            tmp = self.find_min(node.right)
            node.data = tmp.data
            node.right = self._del_(node.right,node.data)
        else:
            if node.left is None:
                node = node.right
            else:
                node = node.left
            self.count -= 1
        return node
    
    def find_min(self,node):
        if node.left is None:
            return node
        else:
            return self.find_min(node.left)