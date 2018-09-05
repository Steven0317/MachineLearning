"""
Created on Tue Feb 20 17:49:51 2018

@author: Mustafa Hajij
"""

import math
from itertools import tee, islice, chain
import numpy as np
from unionfind import *
import networkx as nx
from sklearn.neighbors import radius_neighbors_graph
from scipy.sparse import find
# Import any library you see necessary 



"""

Part 1 point cloud 0-barcode 

"""

# this function is provided to you in case you want to load the data sets I gave to you.
def load_data_from_hd(path): # path must be a string to the location of the file
    
    with open(path) as f:
        names_list = [line.split(',') for line in f if line.strip()]
    f=[]    
    for line in names_list:
        f.append([float(x) for x in line])
    return np.array(f)


def epsilon_neighborhood_graph(pointcloud,alpha):
     
    mat= radius_neighbors_graph(pointcloud,alpha, mode='distance', include_self=False,p = 2)
    (row,col,entries)=find(mat)
    G =nx.Graph()     
    
    for i in range(0,len(pointcloud)):
        G.add_node(i)
    for i in range(0,len(row)):
        G.add_edge(row[i],col[i],weight=entries[i])        
    return G 


def previous_and_next(some_iterable):
    
    prevs, current, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    
    return zip(prevs, current, nexts)




def zero_barcode_pointcloud(pointcloud,alpha):

   
    Graph = epsilon_neighborhood_graph(pointcloud,alpha)
   
    barlist = [(0,math.inf) for i in range(1,len(G.nodes()))]
    UF = UnionFind()
    UF.insert_objects(Graph)
  
    for u,v, data in sorted(Graph.edges(data=True), key=lambda x: x[2]['weight']):
           
        setu = UF.find(u)
        setv = UF.find(v)
        if setu != setv:
           
            UF.union(setu,setv)
            barlist.pop(1)
            barlist.append((0,data['weight']))
    
    return barlist



"""

Part 2 : no code is required. Submit the results as described in the description.

"""


"""

Part 3 (Bonus)scalar function 0-barcode 

"""

def zero_barcode_scalar_function(pointcloud,alpha):
   
    UF = UnionFind()
    sortedlist = sorted(pointcloud, key=lambda x: x[1])
    pairedlist=[] 
   
    for i in range(0, len(sortedlist)):
       
        if pointcloud[i-1][1] > sortedlist[i][1] and pointcloud[i+1][1] > sortedlist[i][1]:
           
            UF.insert_objects(sortedlist[i])
            pairedlist.append(sortedlist[i])
       
        if pointcloud[i-1][1] < sortedlist[i][1] and pointcloud[i+1][1] < sortedlist[i][1]:
           
            c=UF.find(pointcloud[i-1])
            d=UF.find(pointcloud[i+1])
            UF.union(c,d)
            
            if c[1] < d[1]:
                maxPoint=d
            else:
                maxPoint=c
            
            pairedlist.append((sortedlist[i],maxPoint))
       
        else:
            c=UF.find(pointcloud[i-1])
            UF.union(sortedlist[i],c)
            print(c,sortedlist[i])
    return pairedlist


                  

                         

if __name__ == '__main__':
    '''
    mylist = zero_barcode_pointcloud(load_data_from_hd('dataset_1.txt'),3)
    persistence = max(mylist)
    print(mylist)
    '''
    
    pointcloud=[(1,1),(2,2),(3,4),(4,3),(5,5),(6,3.5),(7,7),(8,8),(9,9),(10,8),(11,9.5),(11,7.5),(12,12),(13,1.5)]
    sortedlist=sorted(pointcloud, key=lambda x: x[1])
    scalarlist = zero_barcode_scalar_function(pointcloud,3)
    print(scalarlist)
    