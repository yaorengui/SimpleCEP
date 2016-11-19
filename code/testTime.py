# -*- coding: utf8 -*-
from cepEngine import cepEngine
import shelve
from cepEngine2 import *
import time
def test():
    str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609. LastPrice > 0"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit ru1609. LastPrice > 0"
    str_cedl3 = "select complexEvent2 from sh601006,sh601003,sh601001 pattern and(sh601006,sh601003,sh601001) limit sh601001.openPrice > 0"
    engine = cepEngine2()
    engine.addEventWithCedl(str_cedl)
    engine.addEventWithCedl(str_cedl2)
    #engine.addEventWithCedl(str_cedl3)
    engine.start()

    """加载数据"""
    f = shelve.open('../data/stock1.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
            engine.putAtomEvent(value)
    f.close()

def testTime(isShare):
    str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609. LastPrice > 0"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit ru1609. LastPrice > 0"
    engine = cepEngine2()
    engine.addEventWithCedl(str_cedl,isShare)
    engine.addEventWithCedl(str_cedl2,isShare)

    testTime = []
    temp = 0
    for i in range(7):
        """加载数据"""
        f = shelve.open('../data/stock'+str(i)+'.vt')
        if 'data' in f:
            d = f['data']
            start = time.time()
            for value in d:
                engine.put(value)
            t = (time.time() - start) + temp
            testTime.append(t)
            temp = t
            #print time.time() - start
            '''
            print 'the number of complex event:',engine.outputQueue.qsize()
            print 'the number of simple event:',engine.atomEventQueue.qsize()
            print 'the number of limit simple event:',engine.detectQueue.qsize()
            print 'the number of eventIndex in eventForest:',engine.eventForest.outputQueue.qsize()
            nodes= engine.eventForest.nodeIndex
            for key in nodes.keys():
                print  'the operation of node:',nodes[key].op
                print 'the type of node:',nodes[key].eTypeId
                print 'the number of the instances:',len(nodes[key].instances)
                print 'start of the node:',nodes[key].start
                print '*******************************************************'
        '''
        f.close()
    for i,item in enumerate(testTime):
        print '(', str(i+1),',',item,")"

def testAverageNumberOfComplexEvent(isShare):
    #str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609. LastPrice > 0"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit ru1609. LastPrice > 0"
    cedl =      'select complexEvent2 from p1609,cu1607 pattern AND(cu1607,p1609) limit ru1609. LastPrice > 0'
    engine = cepEngine2()
    #engine.addEventWithCedl(str_cedl,isShare)
    engine.addEventWithCedl(str_cedl2,isShare)
    testTime = []
    temp = 0
    for i in range(7):
        """加载数据"""
        f = shelve.open('../data/stock'+str(i)+'.vt')
        if 'data' in f:
            d = f['data']
            start = time.time()
            for value in d:
                engine.put(value)
            t = (time.time() - start) + temp
            testTime.append(engine.numberOfComplexEvent)
            temp = t
        f.close()

    print '\\addplot coordinates {'

    for i,item in enumerate(testTime):
        print '(', str(i+1),',',item,")"

    print '};'

def testSpace(isShare):
    str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609. LastPrice > 0"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit ru1609. LastPrice > 0"
    engine = cepEngine2()
    engine.addEventWithCedl(str_cedl,isShare)
    engine.addEventWithCedl(str_cedl2,isShare)

    testTime = []
    temp = 0
    for i in range(7):
        """加载数据"""
        f = shelve.open('../data/stock'+str(i)+'.vt')
        if 'data' in f:
            d = f['data']
            temp = 0.0
            start = time.time()
            for value in d:
                engine.put(value)
                nodes= engine.eventForest.nodeIndex
                for key in nodes.keys():
                    temp +=len(nodes[key].instances)
            t = (time.time() - start) + temp
            testTime.append(temp/10000)
            temp = t


        f.close()
    for i,item in enumerate(testTime):
        print '(', str(i+1),',',item,")"

def main():
   #testTime(True)
   #testTime(False)
   testAverageNumberOfComplexEvent(True)
   #testSpace(True)

if __name__ =='__main__':
    main()
    pass
