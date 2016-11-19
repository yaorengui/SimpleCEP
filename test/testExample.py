# -*- coding: utf8 -*-
from code.cepEngine2 import *


if __name__ =='__main__':
    #engine = cepEngine2()
    #engine.putEventTree('code/input.txt')
    #engine.register('complexEvent',handler)
    #engine.start()
    """读取数据"""
    f = shelve.open('data.vt')
    if 'data' in f:
        d = f['data']
        for value in d:
           # engine.putAtomEvent(value)
            print value

    f.close()