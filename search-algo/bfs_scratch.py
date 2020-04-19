#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:01:45 2020

@author: Vardhan Dongre
"""

import queue

# Define the Graph structure

class Graph():
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict
        
    # Print all the vertices of the graph (V)
    def vertices(self):
        return list(self.graph_dict.keys())
    
    # Print all the edges in the graph (E)
    def edges(self):
        return self.generate_edges()
    
    # Add a vertex to the graph
    def add_vertex(self,vertex):
        if vertex in self.graph_dict:
            raise "Node Already in Graph"
        self.graph_dict[vertex] = []
    
    # Add an edge (u,v)
    def add_edge(self,u,v):
        if u in self.graph_dict:
            self.graph_dict[u].append(v)
        else:
            self.graph_dict[u] = v
    
    # helper function for edges
    def generate_edges(self):
        edges = []
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                if {node,neighbour} not in edges:
                    edges.append({node,neighbour})
        return edges
    
    # Get the graph dictionary
    def get_graph(self):
        return self.graph_dict
            

# Graphs

# Acyclic graph
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)   
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
graph_1 = g.get_graph()

# Cyclic graph
h = Graph()
h.add_vertex(0)
h.add_vertex(1)
h.add_vertex(2)
h.add_vertex(3)
h.add_vertex(4)
h.add_vertex(5)
h.add_edge(0, 1)
h.add_edge(0, 2)
h.add_edge(1, 3)
h.add_edge(1, 4)
h.add_edge(2, 4)
h.add_edge(2, 5)
h.add_edge(3, 5)
h.add_edge(4, 5)
graph_2 = h.get_graph()


# Breadth First Search based on three colors

# Golbal Variables
n = len(g.vertices())
color = ['white']*n
dist = [-1]*n
pre = [None]*n

def BFS(g,s):
    
    # g: graph, s: source node
    # color: color coding each node; white = not visited, 
    # grey: unexplored neighbours of current node, black = visited
    # dist: distance of node from source
    # pre: list contaning parent nodes for each node
    q = queue.Queue()
    color[s] = 'Grey'
    dist[s]
    q.put(s)
    
    while (not q.empty()):
        u = q.get()
        # Sequence of visiting nodes
        print(u, end=" ")
        for node in g[u]:
            if color[node] == 'white':
                color[node] = 'grey'
                dist[node] = dist[u] + 1
                pre[node] = u
                q.put(node)
        color[u] = 'black'
        

        
    