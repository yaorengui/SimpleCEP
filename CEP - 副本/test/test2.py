#encoding: UTF-8
import warnings
import networkx as nx
from testTo_mupy_matrix import *
from PIL import Image
import pygraphviz as pgv
import matplotlib.pyplot as plt
if __name__ =='__main__':
    G = nx.MultiDiGraph()
    a = G.add_node(3,label = 'a')
    b = G.add_node(4,label = 'b')
    G.add_edge(a,b)
    #G.add_edge(0,1,weight=2)
    #G.add_edge(1,0)
    #G.add_edge(2,2,weight = 3)
    #G.add_edge(2,2)
    plt.imshow(nx.to_numpy_matrix(G))
    plt.show()
    #print nx.to_numpy_matrix(G,nodelist = [0,1,2])
