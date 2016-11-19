# encoding: UTF-8
import shelve
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
from figureCanvas import *
from uiStates import *
from uiConfigure import *
import pygraphviz as pgv
from gui.uiEdit import *
import tkMessageBox

class MainWindow(QtGui.QMainWindow):
    """主窗口"""

    #----------------------------------------------------------------------
    def __init__(self,engine):
        """Constructor"""
        super(MainWindow, self).__init__()
        self.engine = engine
        self.__queue = Queue()
        self.atomEventQueue = Queue()#临时队列
        self.MaxLenOfAtomQueue = 200
        self.__traceThread = Thread(target = self.__trace)
        self.__traceThread.start()

        self.flag = False#初始状态为False，表示
        self.__startThread = putAtomEventToForestThread()
        self.__startThread.start()

        self.A = pgv.AGraph(directed = True,strict=True,center = True)
        self.A.node_attr['shape'] = 'circle'
        self.imageData = None#保存图像数据
        self.drawEventForest()
        self.setWindowTitle('SimpleCEP')

        grid = QtGui.QGridLayout()
        #滑块控件
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setGeometry(30,40,100,30)
        self.connect(self.slider,QtCore.SIGNAL('valueChanged(int)'),self.changeSliderValue)
        grid.addWidget(self.slider,0,0)

        self.sc = figureCanvas(self,self.engine,self.A)
        grid.addWidget(self.sc,1,0)

        self.states = uiStates(self.engine,self)
        self.states.setFixedWidth(0.3*self.width())
        grid.addWidget(self.states,1,1)


        central = QtGui.QWidget()
        central.setLayout(grid)
        self.setCentralWidget(central)


        self.initToolBar()
        #self.loadData()#加载原子事件

    def initToolBar(self):
        #下一步
        nextAction = QtGui.QAction(QtGui.QIcon('../image/player_end_48.png'), 'Next', self)
        nextAction.setShortcut('Ctrl+N')
        nextAction.setStatusTip('Next')
        nextAction.triggered.connect(self.onClickNext)
        self.statusBar()
        #开始
        self.startAction = QtGui.QAction(QtGui.QIcon('../image/windowsmedia11hc48.png'), 'Start', self)
        self.startAction.setShortcut('Ctrl+S')
        self.startAction.setStatusTip('Start')
        self.startAction.triggered.connect(self.onClickStart)
        self.statusBar()
        #编辑复杂事件
        editAction = QtGui.QAction(QtGui.QIcon('../image/accessories_text_editor_32.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Edit')
        self.uiEdit = uiEdit(self.engine,self)
        editAction.triggered.connect(self.onClickEdit)
        self.statusBar()
        #参数配置，例如数据源
        configureAction = QtGui.QAction(QtGui.QIcon('../image/setup_32.png'), 'Edit', self)
        configureAction.setShortcut('Ctrl+C')
        configureAction.setStatusTip('Configure')
        self.uiConfigure = uiConfigure(self.engine,self)
        configureAction.triggered.connect(self.onClickConfigure)
        self.statusBar()
        #退出
        exitAction = QtGui.QAction(QtGui.QIcon('../image/'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()

        #文件菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(nextAction)
        fileMenu.addAction(self.startAction)
        fileMenu.addAction(exitAction)
        #编辑菜单
        menubar = self.menuBar()
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(editAction)
        editMenu.addAction(configureAction)

        #工具栏
        tool = self.addToolBar('start')
        tool.addAction(self.startAction)
        tool.addAction(nextAction)
        tool = self.addToolBar('next')
        tool.addAction(editAction)
        tool.addAction(configureAction)

    def changeSliderValue(self):
        self.__startThread.setSpeed(float(self.slider.value())/100)
        pass

    def onClickNext(self):
        if self.atomEventQueue.empty() == False:
          item = self.atomEventQueue.get()
          self.engine.put(item)
          print item['id']

    def onClickStart(self):
        if self.__startThread.flag == True:
            self.__startThread.setFlag(False)
            self.startAction.setIcon(QtGui.QIcon('../image/windowsmedia11hc48.png'))
        else:
            self.startAction.setIcon(QtGui.QIcon('../image/ic_pause_48.png'))

            self.__startThread.setFlag(True)

        if self.__startThread.target == None:
            self.__startThread.setTarget(self.autoPutAtomEvent)
        pass

    def autoPutAtomEvent(self):
        if self.atomEventQueue.empty() == False:
          item = self.atomEventQueue.get()
          self.engine.put(item)
          #print item['id']

    def onClickEdit(self):
        self.uiEdit.show()
        pass
    def onClickConfigure(self):
        self.uiConfigure.show()
        pass
    #提取复杂事件处理轨迹，并更改事件森林的状态
    def __trace(self):
        while True:
          if self.engine.traceQueue.empty() == False:#try catch时，存在bug：队列为空时，应用紊乱！
            traceQueue = self.engine.traceQueue
            trace = traceQueue.get()
            self.updateGraph(trace)
            time.sleep(.01)
          else:
            time.sleep(.1)
        pass

    def loadData(self):
        f = shelve.open('../code/data.vt')
        if 'data' in f:
          d = f['data']
          for value in d:
            self.atomEventQueue.put(value)
        f.close()
        #tkMessageBox.showinfo(title='infomation',message = "load data finished!")
        print 'load finished!'
        pass

    def updateGraph(self,item):
        g_node = self.A.get_node(item.id)
        g_node.attr['fillcolor'] = 'red'
        fathers = item.father
        for father in fathers:
            print father.eTypeId,father.id,item.id,'test....'
            edge = self.A.get_edge(father.id,item.id)
            edge.attr['color'] = 'green:red'

        self.A.write('eventTree.dot')
        self.A.draw('eventTree.png')
        self.sc.reDraw()
        #恢复
        g_node.attr['fillcolor'] = 'ghostwhite'
        for father in fathers:
            edge = self.A.get_edge(father.id,item.id)
            edge.attr['color'] = 'green:blue'
        pass
    def reDraw(self):
        self.A.write('eventTree.dot')
        self.A.layout('dot')#没这句时，dot文件中，结点无pos，运行出错
        draw = self.A.draw('eventTree.png')
        self.sc.reDraw()
        self.imageData = self.A.draw()
        print type(self.A),type(self.imageData),'ffffffffffffff'
        print self.imageData
        pass

    def drawEventForest(self):
          forest = self.engine.forest
          eventTrees = forest.members
          for item in eventTrees:
            self.visit(item)
            self.A.graph_attr['epsilon'] = '0.000'
            self.A.write('eventTree.dot')
            self.A.layout('dot')
            self.A.draw('eventTree.png')
    pass

    def addEventTreeToGraph(self,node):
        self.visit(node)
        pass

    def visit(self,node):
          self.__queue.put(node)
          self.A.add_node(node.id,shape="doublecircle",label=str(node.eTypeId),style = "filled",color = "black",fillcolor = "grey66",fontsize = 10,margin = 0)
          while(True):
            if self.__queue.qsize() == 0:
                break
            try:
                item = self.__queue.get()
                num = item.childrenId
                for i in range(0,num):
                  self.__queue.put(item.children[i])
                  self.A.add_node(item.children[i].id,label=str(item.children[i].eTypeId),style="filled",fillcolor="ghostwhite",fontsize = 10,margin = 0)
                  #print item.eTypeId,item.children[i].eTypeId,item.id,item.children[i].id
                  self.A.add_edge(item.id,item.children[i].id,dir="both",arrowhead="vee",arrowtail="vee",color="green:blue",bgcolor="black",arrowsize=0.75)

                #print item.eTypeId
            except Empty:
                print "exit"
                break
    pass
class putAtomEventToForestThread(Thread):
    def run(self):
        self.seq = 0
        self.target = None
        self.flag = False
        self.time = .001
        while True:
            while self.flag == True:
                if self.target!=None:
                  self.target()
                  time.sleep(self.time)

    def setFlag(self,value):
        self.flag = value

    def setTarget(self,value):
        self.target = value
        pass
    def setSpeed(self,value):
        if(value>.001):
            self.time = value