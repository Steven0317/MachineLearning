# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:20:15 2018

@author: Mustafa Hajij

StevenFaulkner U9616-1844
"""
from sklearn import manifold
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


"""
Use the following function to draw a graph
the following function accepts as input a graph G
and a dictionary pos

pos is the position of the nodes of the graph G

"""

def draw_graph(G,pos): # this function is provided for you and you do not need to alter it.
     
     nx.draw_networkx_nodes(G, pos,
                       node_color='r',
                       node_size=500,
                       alpha=1)
     nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

#example of utilization of the above function

#(1) Define the graph G

G = nx.cubical_graph()

#(2) check the nodes of the graph G

#print("the nodes of the graph are : ")
#print(G.nodes())

#(3) define the position dictionary
pos = {0: np.array([ 0.82877618,  0.53211873]), 
       1: np.array([ 0.8059564,  0.       ]), 
       2: np.array([ 0.51148475,  0.37349706]), 
       3: np.array([ 0.54462887,  0.89200482]), 
       4: np.array([ 0.31695909,  0.62593525]), 
      5:np.array([ 0.02260257,  1.        ]), 
      6: np.array([ 0.        ,  0.46707769]), 
       7: np.array([ 0.28222528,  0.10714391])}

#print("the position of the nodes of the graph are : ")
#print(pos)

# draw the graph 

#draw_graph(G,pos)



# start your code here

#(I)

# the input of both of the following two functions is a weighted graph G. (In case the graph is not weighted you should make sure to assign a weight of 1 to the edges)
# the output is a dictionary of positions that assigns to everynode in the graph a position as in the above example




def graph_node_position_mds(G):

    nx.set_edge_attributes(G, 1,'weight')
    length=nx.floyd_warshall_numpy(G)
    mds = manifold.MDS(n_components=2,dissimilarity='precomputed')
    pos = mds.fit(length).embedding_
    
    return pos

def graph_node_position_Laplacian(G):
    
    nx.set_edge_attributes(G, 1,'weight')
    length=nx.floyd_warshall_numpy(G)
    spec = manifold.SpectralEmbedding(n_components=2)
    pos = spec.fit(length).embedding_
    
    return pos




#(II) test your results :
    #A    
        # (1 ) run the function  graph_node_position_mds and save the results as MDS_pos
        # (2 ) run the function draw_graph(G,MDS_pos)
        
MDS_pos = graph_node_position_mds(G)
draw_graph(G,MDS_pos)
    # B 
        # (1 ) run the function graph_node_position_Laplacian and save the results as Laplacian_pos
        # (2 ) run the function draw_graph(G,Laplacian_pos)
   
LAP_pos = graph_node_position_Laplacian(G)
draw_graph(G,LAP_pos)   
