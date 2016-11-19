# encoding: UTF-8

import sys
import ctypes
from gui.QMainWindow import *
from cepEngine2 import *


#----------------------------------------------------------------------
def main():
    """主程序入口"""
    # 设置底部任务栏图标，win7以下请注释掉
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('simpleCEP demo')

    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('../image/93-view-filter.png'))
    #app.setFont(BASIC_FONT)
    str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609. LastPrice > 0"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit ru1609. LastPrice > 0"
    str_cedl3 = "select complexEvent2 from sh601006,sh601003,sh601001 pattern and(sh601006,sh601003,sh601001) limit sh601001.openPrice > 0"
    engine = cepEngine2()
    #engine.putEventTree('../code/input.txt')
    share = True
    engine.addEventWithCedl(str_cedl,share)
    engine.addEventWithCedl(str_cedl2,share)
    engine.addEventWithCedl(str_cedl3,share)
    engine.start()
    #engine.register('complexEvent',handler)
    engine.start()
    mainWindow = MainWindow(engine)
    mainWindow.showNormal()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()