#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:11:50 2020

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

def height(node):
    # if node.left == None and node.right == None:
    #     return 0
    # if node.left == None and node.right != None:
    #     return height(node.right)+1
    # if node.left != None and node.right == None:
    #     return height(node.left)+1
    
    # Alternate way
    if node == None:
        return -1
    return max(height(node.left), height(node.right))+1
    

# Binary Tree 1 Height = 4
tree_1 = BintreeNode(0)
tree_1.left = BintreeNode(0)
tree_1.right = BintreeNode(0)
tree_1.left.left = BintreeNode(8)
tree_1.left.right = BintreeNode(0)
tree_1.right.left = BintreeNode(0)
tree_1.right.right = BintreeNode(0)
tree_1.left.right.left = BintreeNode(7)
tree_1.left.right.right = BintreeNode(0)
tree_1.right.left.left = BintreeNode(1)
tree_1.right.right.right = BintreeNode(9)
tree_1.left.right.right.left = BintreeNode(-1)
tree_1.left.right.right.right = BintreeNode(-2)