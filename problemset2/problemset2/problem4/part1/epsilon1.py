'''
Author: Steven Faulkner

funtion to implement an epsilon clustering graph
'''
from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import radius_neighbors_graph
import matplotlib.pyplot as plt
from scipy import sparse as sp
import networkx as nx

def epsilon(inlist,ε):

    G = nx.Graph()

    for x,y in inlist:
        G.add_node((x,y))

    R = radius_neighbors_graph(G.nodes(),ε,mode='distance',metric ='euclidean', n_jobs = -1)
    I,J,V = sp.find(R)

    nodelist = list(G.nodes())

    for x,y,w in zip(I,J,V):
        G.add_edge(nodelist[x], nodelist[y], weight=float(w))

    return G


centers = [[1,1],[-1,-1],[1,-1]]
mylist, labels_true = make_blobs(n_samples = 20,cluster_std=.5,random_state=0)

epi = epsilon(mylist,1)

for edge in epi.edges(data=True):
    print(edge)

nx.draw_networkx(epi,with_labels=False)
plt.show()

