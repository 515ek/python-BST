#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 03-10-2018
## Assignment: Implementing the Binary Search Tree DataStructure
## Question: 2. Add methods to in-order, pre-order, post-order and level-order traversals
#################################################################################################
from soln01 import traversals
from mclass import BST
from soln02 import ascdscTree as s2
from soln04 import htree as s4
from soln05 import leaftree as s5
from soln06 import minmaxtree as s6
from soln08 import subtree as s8
import random

def seedTree(tree):
    tree.add(50)
    tree.add(10)
    tree.add(60)
    tree.add(25)
    tree.add(55)
    tree.add(75)
    tree.add(20)
    tree.add(70)
    tree.add(90)

def soln01():
    tree1 = BST()
    assert(tree1.isEmpty())
    seedTree(tree1)
    assert(tree1.node_count() == 9)
    assert(tree1.lookup(25))
    tree1.delete(25)
    assert(tree1.node_count() == 8)
    assert(not tree1.lookup(25))

def soln02():
    t2 = traversals()
    seedTree(t2)
    print("Inorder---->>")
    print(t2.inorder())
    print("preorder---->>")
    print(t2.preorder())
    print("postorder---->>")
    print(t2.postorder())
    print("levelorder---->>")
    print(t2.levelorder())

def soln03():
    t3 = s2()
    seedTree(t3)
    print("Ascending order---->>")
    print(t3.ascTraverse())
    print("Descending order---->>")
    print(t3.descTraverse())

def soln04():
    t4 = s4()
    seedTree(t4)
    assert(t4.height() == 4)

def soln05():
    t5 = s5()
    seedTree(t5)
    assert(t5.leaves() == 4)

def soln06():
    t6 = s6()
    seedTree(t6)
    assert(t6.minNode() == 10)
    assert(t6.maxNode() == 90)

def soln08():
    t8 = s8()
    seedTree(t8)
    assert(t8.leftsubTree() == 3)
    assert(t8.rightsubTree() == 5)

if __name__ == '__main__':
    soln01()
    soln02()
    soln03()
    soln04()
    soln05()
    soln06()
    soln08()
