'''
Author: Steven Faulkner
Euclidian MST using kruskals algorithm
'''
import matplotlib.pyplot as plt
from scipy import sparse as sp
from sklearn.neighbors import kneighbors_graph
from sklearn.datasets.samples_generator import make_blobs
from kruskalsalgorithm import *
import networkx as nx
import numpy as np

def EMST(inlist):

    graph = nx.Graph()
    
    for x,y in inlist:
        graph.add_node((x,y))
    
    A = kneighbors_graph(graph.nodes(),3,mode='distance', metric='euclidean',n_jobs=-1)
    I,J,V = sp.find(A)
    
    nodelist = list(graph.nodes())
    for x,y,w in zip(I,J,V):
        graph.add_edge(nodelist[x],nodelist[y], weight=float(w))
    
    T = nx.minimum_spanning_tree(graph)
    return(T)

