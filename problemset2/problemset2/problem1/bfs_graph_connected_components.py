"""
Author: Steven Faulkner
A simple BFS algorithm to implement
with networkx
"""

import networkx as nx

'''
    generator function that creates a list of sets containing connected nodes


    iterates over the nodes within the graph, if a node is not within the visited set
    run the the bfs algorthim to find all connections related to that node then adds
    that set to the list

'''    
def connected_bfs(graph):

    visited = set()


    for v in graph:
        if v not in visited:
            c = set(bfs(graph, v))
            yield c
            visited.update(c)
    



    #generic bfs that returns a set of connected nodes

def bfs(graph,v):

    visited = set()
    node_list = {v}

    while node_list:
        queue = node_list
        node_list = set()
        for i in queue:
            if i not in visited:
                yield i
                visited.add(i)
                node_list.update(graph[i])

                
graph = nx.path_graph(4)
graph.add_path([10,11,12])


print(sorted(connected_bfs(graph), key=len, reverse=True))

