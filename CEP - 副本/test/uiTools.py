#encoding: UTF-8
from PyQt4 import QtGui, QtCore
import shelve
from Queue import *
import time
from threading import Thread
from FileDialog import *
import tkFileDialog
from Tkinter import *
class uiTools(QtGui.QWidget):
    def __init__(self,engine,mainWindow):
        super(uiTools,self).__init__()
        self.engine = engine
        self.mainWindow = mainWindow
        self.__traceThread = Thread(target = self.__trace)
        self.__traceThread.start()

        self._queue = Queue()
        #添加实例
        #self.bt_next = QtGui.QPushButton()
        #self.bt_next.setFixedWidth(self.width()*0.1)
        #self.bt_next.setFixedHeight(self.width()*0.1)
        #self.bt_next.clicked.connect(self.nextStep)
        #self.bt_next.setIcon(QtGui.QIcon('../image/player_end_48.png'))
        #复杂事件定义语言标签
        self.lb_cedl = QtGui.QLabel()
        self.lb_cedl.setText(u'复杂事件编辑：')
        #编辑复杂事件定义语言
        self.edit_cedl = QtGui.QTextEdit()
        self.edit_cedl.setFixedWidth(self.width()*0.5)
        self.edit_cedl.setFixedHeight(self.width()*0.2)
        font = QtGui.QFont()
        font.setFamily('Lucida')
        font.setPointSize(20)
        self.edit_cedl.setFont(font)
        #添加待检测的复杂事件
        self.bt_add = QtGui.QPushButton("&add")
        self.bt_add.setFixedWidth(self.width()*0.1)
        self.bt_add.setFixedHeight(self.width()*0.1)
        self.bt_add.clicked.connect(self.onClickAdd)

        #数据源标签
        self.lb_path = QtGui.QLabel()
        self.lb_path.setText(u'数据源：')
        #数据源路径编辑
        self.edit_path = QtGui.QLineEdit()
        self.edit_path.setFixedWidth(self.width()*0.12)
        self.edit_path.setFixedHeight((self.width()*0.05))
        #打开数据按钮
        self.bt_open = QtGui.QPushButton("&browse")
        self.bt_open.setFixedWidth(self.width()*0.12)
        self.bt_open.setFixedHeight(self.width()*0.05)
        self.bt_open.clicked.connect(self.onClickOpen)
        layout = QtGui.QGridLayout()
        #layout.addWidget(self.bt_next,0,0)
        #数据源
        layout.addWidget(self.lb_path,0,0)
        layout.addWidget(self.edit_path,0,1)
        layout.addWidget(self.bt_open,0,2)
        #复杂事件编辑
        layout.addWidget(self.lb_cedl,1,0)
        layout.addWidget(self.edit_cedl,1,1)
        layout.addWidget(self.bt_add,1,2)


        self.setLayout(layout)
        self.loadData()
        pass
    #添加待监测的复杂事件
    def onClickAdd(self):
        root = self.engine.putEventTreeToForestWithCEDL(str(self.edit_cedl.toPlainText()))
        self.mainWindow.visit(root)#添加结点
        self.mainWindow.reDraw()
        pass
    #数据源配置
    def onClickOpen(self):
        fname = tkFileDialog.askopenfilename()
        self.edit_path.setText(fname)
        pass

    def __trace(self):
        while True:
          try:
            traceQueue = self.engine.traceQueue
            trace = traceQueue.get()
            #for item in trace:
                #self.mainWindow.updateGraph(item)
            self.mainWindow.updateGraph(trace)
            time.sleep(.01)
          except Empty:
            time.sleep(.1)
        pass

    def nextStep(self):
        try:
          item = self._queue.get()
          self.engine.put(item)
          print 'put the atom event to the event tree!'
        except Empty:
          print 'the queue is empty!'
        pass

    def loadData(self):
        f = shelve.open('../code/data.vt')
        print f,type(f),'test..............'
        if 'data' in f:
          d = f['data']
          for value in d:
            self._queue.put(value)
        f.close()
        pass