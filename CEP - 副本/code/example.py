# -*- coding: utf8 -*-
from cepEngine import cepEngine
import shelve
def handler(event):
    d = event.attrs
    print_dict(d)
    pass

def print_dict(d):
    for key,value in d.items():
        print key + ':'+str(value)
def mode1():
    #模式1
    engine = cepEngine()  #step1:start the complexEventEngine
    engine.start()
    engine.putEventTree('input1.txt') #step2:define the complex event
    engine.register('complexEvent',handler)#step3:define the handler
    f = shelve.open('tickData.vt') #step4:put data
    if 'data' in f:
        d = f['data']
        for value in d:
            engine.putAtomEvent(value)
    f.close()
def mode2():
    #模式2
    engine = cepEngine()
    engine.putEventTree('input1.txt')
    engine.register('complexEvent',handler)

    """读取数据"""
    f = shelve.open('tickData.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
            #print str(value)
            #if (value['id'] == 'zn1701') | (value['id'] == 'zn1702'):
                #print str(value)
            engine.put(value)
    f.close()

from cepEngine2 import *

def mode3():
    engine = cepEngine2()
    engine.start()
    engine.putEventTree('input1.txt')
    engine.register('complexEvent',handler)#当发生complexEvent时,执行handler,参数为complexEvent涉及到的所有原子事件数据
    f = shelve.open('data.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
            engine.putAtomEvent(value)
    f.close()

def mode4():
    engine = cepEngine2()
    engine.putEventTree('input.txt')
    engine.register('complexEvent',handler)

    """读取数据"""
    f = shelve.open('data.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
            engine.put(value)
    f.close()

def mode5():
    engine = cepEngine2()
    engine.putEventTree('input.txt')
    engine.register('complexEvent',handler)
    engine.start()
    """读取数据"""
    f = shelve.open('data.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
            engine.putAtomEvent(value)

    f.close()

def main():
    mode5()
    #mode4()
    #mode3()
    #mode2()
    #mode1()

if __name__ =='__main__':
    main()
    pass
