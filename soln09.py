#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 9. Add method the check whether two BSTs are same. Provide test cases.
#################################################################################################
from soln01 import traversals as bst

def isSame(T1 , T2):
    if T1.levelorder() == T2.levelorder():
        return True
    else:
        return False

def seedsameTree(T1):
    T1.add(50)
    T1.add(30)
    T1.add(60)
    T1.add(20)
    T1.add(25)


if __name__ == '__main__':
    T1 = bst()
    T2 = bst()
    seedsameTree(T1)
    seedsameTree(T2)
    print(T1.levelorder())
    print(isSame(T1,T2))