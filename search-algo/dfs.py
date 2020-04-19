#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:54:52 2020

@author: don
"""
from collections import defaultdict
g = {
     0:[1,2],
     1:[0,3,4],
     2:[0,3,5],
     3:[1,2,4],
     4:[1,3,6],
     5:[2,6],
     6:[4,5]}

graph = g

n = len(g)

visited = [False]*n

order = []

def dfs(node):
    if visited[node] == True:
        return
    
    visited[node] = True
    order.append(node)
    
    neighbours = graph[node]
    for next_node in neighbours:
        dfs(next_node)
    

start = 0
dfs(start)
print(order)

# class Graph(object):
#     def __init__(self):
        
#         self.graph = defaultdict(list)
        
#     def add_edge(self,u,v):
#         self.graph[u].append(v)
        
#     def DFSutil(self, n, visited):
#         visited[n] = True
#         print(n, end=" ")
    
#         for i in self.graph[n]:
#             if visited[i] == False:
#                 self.DFSutil(i, visited)
            
#     def DFS(self,n):
    
#         visited = [False]*(len(self.graph))
#         self.DFSutil(n, visited)

        



# Define a graph

# graph = Graph()
# graph.add_edge(0,1)
# graph.add_edge(0,2)
# graph.add_edge(1,2)
# graph.add_edge(2,0)
# graph.add_edge(2,3)
# graph.add_edge(3,3)

# graph.DFS(2)




