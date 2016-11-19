# -*- coding: utf8 -*-
from antlr4 import *
import time
import datetime
from code.cedl_node import *
'''
class test():
    def __init__(self):
        pass
    def func1(self):
        global dic
#        print dic['yao']
        pass
    def func2(self):
        pass

def testTime():
   t = test()
   dic = {}
   dic['yao']='yooo'
   #时间测试
   t.func1()
   for i in range(100):
       print time.time()
   import datetime
   datec = datetime.datetime(2010,6,6,8,14,59,445)
   #datec = time.ctime()
   timestamp = time.mktime(datec.timetuple())
   print datec,timestamp

   ltime = time.localtime(time.time())
   timeStr = time.strftime("%Y-%m-%d %H:%M:%S",ltime)
   print ltime,timeStr

   d1 = datetime.datetime(2015,7,5,4,5)
   d2 = datetime.datetime(2015,7,4,2,5)
   print d1,d2,(d1-d2).seconds
'''
def testNone():
    i = None
    j = None
    if i == j:
        print True
    else:print False

def testFind():
    cc = []
    seq = 0
    temp = eType_node(seq)
    #object.__eq__(temp)
    seq+=1
    cc.append(temp)
    #for i,node in enumerate(cc):



if __name__ == '__main__':
   # main()
   #testTime()
   testNone()


