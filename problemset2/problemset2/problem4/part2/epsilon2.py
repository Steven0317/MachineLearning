'''
Author: Steven Faulkner

returns the connected componentes of an epsilon cluster
'''
import networkx as nx
from epsilon1 import *
from bfs_graph_connected_components import *
from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import radius_neighbors_graph
import matplotlib.pyplot as plt

def epsilon_cluster(inlist, ε):

    G = nx.Graph()

    G = epsilon(inlist, ε)

    for c in list(connected_bfs(G)):
        print(c)

    return G
    
centers = [[1,1],[-1,-1],[1,-1]]
mylist, labels_true = make_blobs(n_samples = 10,centers=centers,cluster_std=1,random_state=0)


epi2 = epsilon_cluster(mylist,2)

nx.draw_networkx(epi2,with_labels=False)
plt.show()
