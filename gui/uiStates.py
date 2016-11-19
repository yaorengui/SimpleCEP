#encoding: UTF-8
from PyQt4 import QtGui, QtCore
import shelve
from Queue import *
import time
from threading import Thread
class uiStates(QtGui.QFrame):
    def __init__(self,engine=None,mainWindow=None,content=None):
        super(uiStates,self).__init__()
        self.engine = engine
        self.mainWindow = mainWindow
        self.contentLabel = QtGui.QLabel(str(content))
        grid = QtGui.QGridLayout()
        grid.addWidget(self.contentLabel, 0, 0)
        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(grid)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        pass
    def setContent(self,content):
        self.contentLabel.setText(content)