#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:02:14 2018

@author: Mustafa Hajij
"""
import matplotlib.pyplot as plt
from unionfind import *
import networkx as nx

class kruskalsalgorithm():
    def __init__(self,inputgraph):
        self.original_graph=inputgraph
        self.tree=nx.Graph()


    
    def spanningtree(self):
        
        UF = UnionFind()
        UF.insert_objects(self.original_graph.nodes())
        '''
            looking at every pair of nodes that form an edge
            determine if it already exists within UF, adding
            to list if false
        '''
        T=nx.Graph()
        A =[]
        for u,v, data in sorted(self.original_graph.edges(data=True), key=lambda x: x[2]['weight']):
            setu = UF.find(u)
            setv= UF.find(v)

            if setu != setv:
                A.append((u,v,data['weight']))
                UF.union(setu,setv)

        for a,b,w in A:
            T.add_edge(a,b, weight = w)

        return T

