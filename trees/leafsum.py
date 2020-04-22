#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:27:14 2020

@author: Vardhan Dongre
"""
# Binary Tree Class

class BintreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None # left child
        self.right = None # right child
        
    # Get a list of child nodes of the current node
    def getchildNode(self,node):
        if node.left == None and node.right == None:
            return []
        elif node.left == None and node.right != None:
            return [node.right]
        elif node.right == None and node.left != None:
            return [node.left]
        return [node.left, node.right]

# Finding the sum of leaf nodes of a Binary tree

def leafsum(node):
    if node is None:
        return 0
    
    if node.left == None and node.right == None:
        return node.val
    
    total = 0
    for child in node.getchildNode(node):
        total += leafsum(child)
        
    return total

# Finding the sum of leaf nodes of any tree

# def leafsum(node):
#     if node is None:
#         return 0
    
#     if isleaf(node):
#         return node.val
    
#     total = 0
#     for child in node.getchildNode(node):
#         total += leafsum(child)
        
#     return total

# def isleaf(node):
#     return len(node.getchildNode(node)) == 0

# Binary Tree 1 Leaf Sum = 3
tree_1 = BintreeNode(5)
tree_1.left = BintreeNode(4)
tree_1.right = BintreeNode(3)
tree_1.left.left = BintreeNode(1)
tree_1.left.right = BintreeNode(-6)
tree_1.right.left = BintreeNode(0)
tree_1.right.right = BintreeNode(7)
tree_1.right.right.left = BintreeNode(8)

# Binary Tree 2 Leaf Sum = 22
tree_2 = BintreeNode(0)
tree_2.left = BintreeNode(0)
tree_2.right = BintreeNode(0)
tree_2.left.left = BintreeNode(8)
tree_2.left.right = BintreeNode(0)
tree_2.right.left = BintreeNode(0)
tree_2.right.right = BintreeNode(0)
tree_2.left.right.left = BintreeNode(7)
tree_2.left.right.right = BintreeNode(0)
tree_2.right.left.left = BintreeNode(1)
tree_2.right.right.right = BintreeNode(9)
tree_2.left.right.right.left = BintreeNode(-1)
tree_2.left.right.right.right = BintreeNode(-2)

