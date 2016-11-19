# -*- coding: utf8 -*-
import time
import datetime
from code.cedl_node import *
def testNone():
    i = None
    j = None
    if i == j:
        print True
    else:print False

def testObjectEqual():
    node1 = eType_node('E1')
    node2 = eType_node('E2')
    node1.op = '-1'
    node2.op = 'ande'
    if node1 == node2:
        print 'the two objects is not equal'
    else:
        print 'the two objects is equal'

if __name__ == '__main__':
    testObjectEqual()
   # main()
   #testTime()
   #testNone()


