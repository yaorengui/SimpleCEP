# -*- coding: utf8 -*-
from cepEngine import cepEngine
import shelve
from cepEngine2 import *
import time
def testTime(isShare,strCedl):
    engine = cepEngine2()
    for item in strCedl:
        engine.addEventWithCedl(item,isShare)

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

def testAverageNumberOfComplexEvent(isShare,strCedl):
    engine = cepEngine2()
    for item in strCedl:
        engine.addEventWithCedl(item,isShare)
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

def testSpace(isShare,strCedl):
    print 'start....'
    engine = cepEngine2()
    for item in strCedl:
        engine.addEventWithCedl(item,isShare)
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
    str_cedl = "select complexEvent from cu1607,p1609,ru1609 pattern AND(SEQ(cu1607,p1609),ru1609) limit ru1609.LastPrice > 2000"
    str_cedl2 = "select complexEvent2 from p1609,cu1607 pattern SEQ(cu1607,p1609) limit p1609.LastPrice > 2000"
    strAvg = "select avgs from p1609 pattern seq(avg(p1609,40,LastPrice,avg1),avg(p1609,90,LastPrice,avg2)) limit avg1.average>$avg2.average and avg1.average<5445"
    strDec = "select dec from p1609 pattern seq(dec(p1609,3,LastPrice,dec1),p1609) limit dec1.minValue>5000 and dec1.minValue<$p1609.LastPrice"
    strMin = "select min from p1609 pattern min(cu1607,3,LastPrice,min1) limit min1.minValue<5444"

    #strInc = "select min from p1609 pattern inc(cu1607,3,LastPrice,inc1) limit inc1.minValue>0"

    temp = []
    #temp.append(str_cedl)
    #temp.append(str_cedl2)
    temp.append(strAvg)
    #temp.append(strDec)
    #temp.append(strMin)
    #temp.append(strInc)
    testTime(True,temp)
    #testTime(False,temp)
    testAverageNumberOfComplexEvent(True,temp)
    testSpace(True,temp)

    #testTime(False,temp)

if __name__ =='__main__':
    main()
    pass
