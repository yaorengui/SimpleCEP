#encoding: UTF-8
from PyQt4 import QtGui, QtCore
from Queue import *
class uiEdit(QtGui.QWidget):
    def __init__(self,engine,mainWindow):
        super(uiEdit,self).__init__()
        self.engine = engine
        self.mainWindow = mainWindow
        self._queue = Queue()
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
        self.bt_add.setFixedWidth(self.width()*0.04)
        self.bt_add.setFixedHeight(self.width()*0.03)
        self.bt_add.clicked.connect(self.onClickAdd)
        layout = QtGui.QGridLayout()
        #布局
        layout.addWidget(self.edit_cedl,0,1)
        layout.addWidget(self.bt_add,0,2)
        self.setLayout(layout)
        pass
    #添加待监测的复杂事件
    def onClickAdd(self):
        root = self.engine.putEventTreeToForestWithCEDL(str(self.edit_cedl.toPlainText()))
        self.mainWindow.visit(root)#添加结点
        self.mainWindow.reDraw()
        pass