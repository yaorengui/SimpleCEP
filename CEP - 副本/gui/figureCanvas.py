# encoding: UTF-8
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt4 import QtGui, QtCore
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import os
import numpy as np
from PIL import Image
class figureCanvas(FigureCanvas):
    def __init__(self,mainwindow,engine,graph):
        self.mainwindow = mainwindow
        self.engine = engine
        self.graph = graph
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xticks([])#clear the x and y
        self.ax.set_yticks([])
        '''
        x = np.linspace(0,1)
        y = np.sin(4*np.pi*x)*np.exp(-5*x)
        plt.fill(x,y,'r')
        plt.grid(True)
        plt.show()
        '''
        #image load
        self.image_file = cbook.get_sample_data(os.getcwd()+'\eventTree.png')
        self.image = plt.imread(self.image_file)
        plt.imshow(self.image)
        #plt.show()


        plt.axis('off')
        self.ax.hold(True)

        self.fig.set_figwidth(6)#the unit is inches 1in == 2.54cm
        str = self.graph.graph_attr.get('bb').split(',')
        #print self.graph.graph_attr.get('bb'),'dfffffffffffffffffffffffffffff'
        self.g_width = float(str[2])#int('12') str(123.3) chr(98) ord('a')
        self.g_height = float(str[3])
        self.fig.set_figheight(self.fig.get_figwidth()*(self.g_height/self.g_width))
        wh = Image.open(self.image_file).size
        self.maxWidth= wh[0]
        self.maxHeight = wh[1]

        #print  self.fig.get_figwidth(),self.ax.get_ylim(),self.ax.get_ylim(),'444'

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.canvas.mpl_connect('button_press_event',self.onClick)
        pass

    def reDraw(self):
        self.image_file = cbook.get_sample_data(os.getcwd()+'\eventTree.png')
        self.image = plt.imread(self.image_file)
        plt.imshow(self.image)
        self.fig.canvas.draw()


    def onClick(self,event):
        if event.xdata is not None:
            x = event.xdata*(self.g_width/self.maxWidth)
            y = (self.maxHeight - event.ydata)*(self.g_height/self.maxHeight)
            node = self.hitNode(x,y)
            if node!=None:
                self.g_node = self.graph.get_node(node.get_name())
                self.g_node.attr['fillcolor'] = 'darkviolet'

                self.graph.write('eventTree.dot')
                #self.graph.layout('dot')#加上这句，node会发生“未解决”的问题
                self.graph.draw('eventTree.png')
                self.reDraw()
                #恢复
                self.g_node.attr['fillcolor'] = 'ghostwhite'

                #获取结点相关信息
                nodeIndex = self.engine.eventForest.nodeIndex
                key = node.get_name()
                cedlNode = nodeIndex[str(key)]
                print 'ff',cedlNode.toString()
                content = cedlNode.toString()
                self.mainwindow.states.setContent(content)

                #print self.g_width,self.g_height,self.maxWidth,self.maxHeight
            #print x,y
        pass

    def hitNode(self,x,y):
        nodes = self.graph.nodes()
        for node in nodes:
            width = float(node.attr['width'])*72#72 points per inch
            height = float(node.attr['height'])*72
            pos = node.attr['pos'].split(',')
            x_pos = float(pos[0])
            y_pos = float(pos[1])
            if (x-x_pos)*(x-x_pos)/(width*width)+(y-y_pos)*(y-y_pos)/(height*height)<1:
                return node
        return None
        pass