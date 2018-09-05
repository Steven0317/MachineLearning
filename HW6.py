# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:20:15 2018

@author: Mustafa Hajij
"""
from time import time
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform 
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from numpy import *
from numpy import linalg as LA
import numpy as np
from sklearn import manifold, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.decomposition import PCA


Axes3D

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(251, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)


coordinates_array = np.array(X)
dist_array = pdist(coordinates_array)

dist_array = squareform(dist_array)



"""
Implement MDS 

"""
def MDS(d, n):
    
    P = np.square(d)
   
    I = np.identity(len(d))
    
    I2 = np.ones(len(d))
    
    I2 = (1/n)*I2
   
    J = (I - I2)
    J1 = -.5*J
    B = P.dot(J).dot(J1)

    eigenvalues, eigenvectors = LA.eig(B)
    
    idx = eigenvalues.argsort()[-n:][::-1]   
    eigenValues = eigenvalues[idx]
    eigenVectors = eigenvectors[:,idx]
    eigenValues = np.diag(eigenValues)
    eigenValues = np.sqrt(eigenValues)
    
    return eigenVectors.dot(eigenValues)
    

    
"""
Implement ISOMAP 

"""
def ISO(pointcloud, n, k):
    
    A = kneighbors_graph(pointcloud,k,mode='connectivity')
    
    G = nx.from_scipy_sparse_matrix(A,edge_attribute='weight')
  
    length=nx.floyd_warshall_numpy(G)
    
    spec = MDS(length,n)
    spec = np.absolute(spec)
    return spec

"""
Compare your results to the results from the sklearn example 

"""
t0 = time()
Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)
t1 = time()

ax = fig.add_subplot(257)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Isomap (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


t0 = time()
mds = manifold.MDS(n_components, max_iter=100, n_init=1)
Y = mds.fit_transform(X)
t1 = time()

ax = fig.add_subplot(258)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

"""
Use the data "S" with PCA and, project and plot the data and explain your observation.

"""

pca = PCA(n_components=2)
pca.fit(X)
test = pca.transform(X)

ax = fig.add_subplot(256)
plt.scatter(test[:, 0], test[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("PCA")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')




'''
MDS and ISO testing

'''
M = MDS(dist_array, 2)

ax = fig.add_subplot(253)
plt.scatter(M.real[:, 1], M.real[:, 0],c=color, cmap=plt.cm.Spectral)
plt.title("MDS Classic")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


I = ISO(X, 2, 10)

ax = fig.add_subplot(252)
plt.scatter([I[:, 0]], [I[:, 1]],  cmap=plt.cm.Spectral)
plt.title("Isomap Classic")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


'''
Observational Analysis
'''
print()
print("The comparison between skleanrn MDS and Classical shows us that the figure was able to be proportionally be reduced and retained its shape,albeit a more dense shape versus the sklearn implementatin that contains more noise "
      + "pertaining to isomap I was able to recreate the supposed spread of the plot but failed to be able to apply colors without errors, hence why "
      + " the graph is only blue, so I unable to fully know if the hte two plots are completely similar")
print()
print("PCA does a good job proportionally showing the figure in a reduced dimension, hence how its shape is incredibly simliar to that of MDS")