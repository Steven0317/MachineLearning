'''
Author: Steven Faulkner
Euclidian MST using kruskals algorithm
'''

from scipy import sparse as sp
from sklearn.neighbors import kneighbors_graph
from sklearn.datasets.samples_generator import make_blobs
from kruskalsalgorithm import *
import networkx as nx

def EMST(inlist):

    graph = nx.Graph()
    
    for x,y in inlist:
        graph.add_node((x,y))
    
    A = kneighbors_graph(graph.nodes(),3,mode='distance', metric='euclidean',include_self=False,n_jobs=-1)
    
    I,J,V = sp.find(A)
    
    nodelist = list(graph.nodes())
    for x,y,w in zip(I,J,V):
        graph.add_edge(nodelist[x],nodelist[y], weight=float(w))


    T = kruskalsalgorithm(graph)
    return(T.spanningtree())
 
    
'''
test functions for  EMST
'''
centers = [[1,1],[-1,-1],[1,-1]]
mylist, labels_true = make_blobs(n_samples = 10,centers=centers,cluster_std=0.5,random_state=0)

mst = EMST(mylist)
print(mst.edges(data=True))


