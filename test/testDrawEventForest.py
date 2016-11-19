# -*- coding: utf8 -*-
from code.cepEngine2 import *
from Queue import Queue, Empty
import pygraphviz as pgv
class graphvize:
    def __init__(self):
         self.__queue = Queue()
         self.A = pgv.AGraph(directed = True,strict=True)

    def draw(self):
          engine = cepEngine2()
          engine.putEventTree('../code/input1.txt')
          forest = engine.forest
          eventTrees = forest.members
          for item in eventTrees:
            self.visit(item)
            self.A.graph_attr['epsilon'] = '0.001'
            self.A.write('eventTree.dot')
            self.A.layout('dot')
            self.A.draw('eventTree.png')
            self.A.draw('eventTree.png')

    pass

    def visit(self,node):
          self.__queue.put(node)
          while(True):
            if self.__queue.qsize() == 0:
                break
            try:
                item = self.__queue.get()
                num = item.childrenId
                for i in range(0,num):
                  self.__queue.put(item.children[i])
                  self.A.add_edge(item.eTypeId,item.children[i].eTypeId)
                  #打印孩子节点的相关信息
                print item.eTypeId
                 # if len(item.instances)!=0:
                   # print "存在实例"
                    #print item.instances[0].eTypeId
                #print item
            except Empty:
                print "exit"
                break
    pass
def main():
    gra = graphvize()
    gra.draw()


if __name__ == "__main__":
    main()