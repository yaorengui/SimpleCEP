#encoding: UTF-8
from PyQt4 import QtGui,QtCore
import shelve
from Queue import *
import tkFileDialog
import tkMessageBox
import os
from dataStream import *

import time
class uiConfigure(QtGui.QWidget):
    def __init__(self,engine,mainWindow):
        super(uiConfigure,self).__init__()
        self.engine = engine
        self.mainWindow = mainWindow
        self._queue = Queue()
        #数据源路径编辑
        self.edit_path = QtGui.QLineEdit()
        self.edit_path.setFixedWidth(self.width()*0.5)
        self.edit_path.setFixedHeight((self.width()*0.05))
        #打开数据按钮
        self.bt_open = QtGui.QPushButton("&browse")
        self.bt_open.setFixedWidth(self.width()*0.08)
        self.bt_open.setFixedHeight(self.width()*0.06)
        self.bt_open.clicked.connect(self.onClickOpen)
        #加载数据按钮
        self.bt_ok = QtGui.QPushButton("&OK")
        self.bt_ok.setFixedWidth(self.width()*0.08)
        self.bt_ok.setFixedHeight(self.width()*0.06)
        self.bt_ok.clicked.connect(self.onClickOk)
        #取消
        self.bt_cancel = QtGui.QPushButton("&Cancel")
        self.bt_cancel.setFixedWidth(self.width()*0.08)
        self.bt_cancel.setFixedHeight(self.width()*0.06)
        self.bt_cancel.clicked.connect(self.onClickCancel)
        #在线数据
        self.radioOnline = QtGui.QRadioButton()
        self.radioOnline.setText(u'新浪在线数据')
        self.radioOnline.setChecked(False)
        self.radioLocal = QtGui.QRadioButton()
        self.radioLocal.setText(u'本地数据')
        self.radioLocal.setChecked(True)
        #layout = QtGui.QGridLayout()
        self.connect(self.radioOnline,QtCore.SIGNAL("toggled(bool)"),self.radioClick)
        #self.connect(self.radioLocal,QtCore.SIGNAL("toggled(bool)"),self.radioLocalClick)

        layout = QtGui.QGridLayout()

        #数据源
        layout.addWidget(self.radioLocal,0,0)
        layout.addWidget(self.edit_path,1,0)
        layout.addWidget(self.bt_open,1,1)
        layout.addWidget(self.radioOnline,2,0)
        layout.addWidget(self.bt_ok,3,0)
        layout.addWidget(self.bt_cancel,3,1)
        self.setLayout(layout)
        #数据流配置
        self.stream = dataStream()
        self.stream.setTarget(self.procesDataStream)
        pass

    def procesDataStream(self,data):
        if self.mainWindow.atomEventQueue.qsize()<self.mainWindow.MaxLenOfAtomQueue:
            self.mainWindow.atomEventQueue.put(data)
        pass

    def radioClick(self):
        if self.radioLocal.isChecked() == False:
            self.edit_path.setEnabled(False)
            self.bt_open.setEnabled(False)
        else:
            self.edit_path.setEnabled(True)
            self.bt_open.setEnabled(True)
            self.bt_load.setEnabled(True)

    #数据源配置
    def onClickOpen(self):
        fname = tkFileDialog.askopenfilename()
        self.edit_path.setText(fname)
        #加载数据
        pass

    def onClickOk(self):
        if self.radioLocal.isChecked() == True:
            if os.path.isfile(str(self.edit_path.text())):
              self.loadData(self.edit_path.text())
        else:
            #启动来自新浪的股票数据流
            nodeIndex = self.engine.eventForest.nodeIndex
            keys = nodeIndex.keys()
            for item in keys:
                if nodeIndex[item].op =='-1':
                    #print nodeIndex[item].eTypeId,'dfdd'
                    self.stream.addStream(str(nodeIndex[item].eTypeId))
            pass
        self.close()
        pass

    def onClickCancel(self):
        self.close()
        pass

    def loadData(self,str_file):
        f = shelve.open(str(str_file))
        if 'data' in f:
          d = f['data']
          for value in d:
            self.mainWindow.atomEventQueue.put(value)
        f.close()
        bb = tkMessageBox.showinfo(title='infomation',message = "load data finished!")
        pass