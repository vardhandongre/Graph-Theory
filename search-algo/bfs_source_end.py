#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:11:01 2020

@author: Vardhan Dongre
"""

# Global Variables

graph = {0:[1,2],
         1:[2],
         2:[0,3],
         3:[3]}

n = len(graph)

def bfs(start, end):
    
    prev = solve(start)
    print(prev)
    return reconstructPath(start, end, prev)

def solve(s):
    q = []
    q.append(s)
    
    visited = [False]*n
    visited[s] = True
    
    prev = [None]*n
    
    while q:
        node = q.pop(0)
        neighbours = graph[node]
        
        for neighbour in neighbours:
            if visited[neighbour] == False:
                q.append(neighbour)
                visited[neighbour] = True
                prev[neighbour] = node
                
    return prev

def reconstructPath(start, end, prev):
    path = []
    at = end
    while at != None:
        path.append(at)
        at = prev[at]
        
    path.reverse()
    print(path)
    if path[0] == start:
        return path
    
    else:
        return []