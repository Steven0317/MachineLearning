"""
Created on Tue Feb 20 17:49:51 2018

@author: Mustafa Hajij
Steven Faulkner u96161844
"""

import networkx as nx

from sklearn.cluster import KMeans
from sklearn.neighbors import radius_neighbors_graph
from scipy.sparse import find

from itertools import count
import itertools
import random
from matplotlib import pylab as plt
import math


class interval():
    def __init__(self,_a,_b):
         self.a=_a
         self.b=_b


"""
THE FOLLOWING 4 FUNCTIONS ARE PROVIDED FOR YOU TO HELP YOU IN THE HOMEWORK. YOU DO NOT NEED TO CHANGE THESE FUNCTIONS OR ALTER THEM.
"""

def epsilon_neighborhood_graph(pointcloud,alpha):
     
    mat= radius_neighbors_graph(pointcloud,alpha, mode='distance', include_self=False,p = 2)
    (row,col,entries)=find(mat)
    G =nx.Graph()     
    for i in range(0,len(pointcloud)):
 
        G.add_node(i)
    for i in range(0,len(row)):

        G.add_edge(row[i],col[i],weight=entries[i])
         
    return G 

def epsilon_graph_clusters(pointcloud,alpha): # you will need this inside the main function mapper_graph
    
    graph=epsilon_neighborhood_graph(pointcloud,alpha)
    
    CC_graphs=list(nx.connected_component_subgraphs(graph))
    
    CC_points=[]
     
    for CC in CC_graphs:
   
        CC_points.append([pointcloud[i] for i in CC.nodes()])
    return CC_points    


def circle_example(number): # this function just samples from the unit circle uniformaly.


    X=[]
    for i in range(0,number):
        angle = random.uniform(0,1)*(math.pi*2)
        x=math.cos(angle)
        y=math.sin(angle)
        X.append((x,y))
      
    return X   


def build_coordiante_filter(X,coordinate): # this creates a simple f to be used as input for the function 

    f={}
    for x in X:
        f[x]=x[1]
     
    return f 




"""
START YOUR IMPLEMENTATION HERE
"""  

"""
INTERVAL is an instance of the class provided above. Technically you can calculate that from the function f (a would be the min value of f and b would be the max value of f )


"""
  
def calculate_cover(INTERVAL,N,epsilon):  #INTERVAL =[a,b] , N is number of divisions for the interval and epsilon is the overlap
    
    i=0
    intvl = []
    start = INTERVAL.a
    end = INTERVAL.b
    delta = abs(start-end)/ N
    
    #beginning interval
    point = start + delta
    intvl.append((start, point + epsilon))
    start = point
    
    #middle interval(s)
    while i < (N-2):
        point = start + delta
        intvl.append((start - epsilon, point + epsilon))
        start = point
        i +=1
    
    #ending interval
    point = start + delta
    intvl.append((start - epsilon, end))
    
    return intvl


    #return a list of intervals each of them represents part of the cover as described in the lecture.
    
"""
Input mapper_graph:
X is an array that represents the data. Each element point must be a tuple : otherwise Python will complain when you want to use the function f for hashing the points in X.
f is a dictionary : keys are the points in X and the values are real numbers
N is the number of slices in the cover
epsilon : is the amount of overlap between slices
alpha is the clustering parameter for the function epsilon_graph_clusters provided above

"""    
    
def mapper_graph(X,f,N,epsilon,alpha):
        
        """
        
   
        """
        intvl = interval(min(f.values()),max(f.values()))
    
        cover = calculate_cover(intvl, N,epsilon)
        
        G=nx.Graph()
        
        for u,j in cover:
            bucket = []
            for i in f:
                if u <= f[i] <= j:
                    bucket.append(i)
            centoid = KMeans(n_clusters=1,random_state=0).fit(bucket).cluster_centers_
            centoid = itertools.chain.from_iterable(centoid)
            bucket = epsilon_graph_clusters(bucket,alpha)
            chain = itertools.chain.from_iterable(bucket)
            G.add_node(tuple(centoid), clusters = set(chain))
        
        
        for i,j in G.nodes(data=True):
            for u,v in G.nodes(data=True):
                a = itertools.chain.from_iterable(j.values())
                b = itertools.chain.from_iterable(v.values())
                if set(a) & set(b):
                    G.add_edge(i,u)
                    

        return G
        
"""
test your work
"""    

# (1) define the data
X=circle_example(200)
# (2) define the function f
f=build_coordiante_filter(X,1) # this will create a function f(x,y)=y
# choose other Mapper parameters : I choose the following. You will need to keep changing them untill you obtain a good result (circular graph)                                                 
N=4
epsilon=.3 # this will also depend on the number of points in X
alpha=.15 # this will depend on the number of points in X                         
color = ['blue', 'yellow', 'yellow','red' ]
# (3) run the Mapper constructoin
G=mapper_graph(X,f,N,epsilon,alpha)   
# (4) Draw the graph using networkx

nx.draw_networkx(G, pos=nx.spring_layout(G),with_labels=False, node_color = color)

# (5) save the output image  

plt.savefig('mapper.png')