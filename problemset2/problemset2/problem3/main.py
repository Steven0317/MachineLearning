'''
@Steven Faulkner

'''
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import networkx as nx
from EMST import *
from bfs_graph_connected_components import *

def Zahns(inlist, k):

    
    T = EMST(inlist)
     
    i=0
    for u,v,w in sorted(T.edges(data=True),key=lambda x:x[2]['weight'],reverse=True):
        if i < k-1:
            T.remove_edge(u,v)
            i+=1
        else:
            break
    
    for c in list(connected_bfs(T)):
        print(c)
        
    return T
    


centers = [[1,1],[-1,-1],[1,-1]]
mylist, labels_true = make_blobs(n_samples = 50,centers=centers,cluster_std=1,random_state=0)


mst = Zahns(mylist,2)

nx.draw_networkx(mst,with_labels=False)
plt.show()

