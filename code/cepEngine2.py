# -*- coding: utf8 -*-
import shelve
from cedl_node import *
from eventForest import *
from Queue import Queue, Empty
from threading import Thread
from cedlLimit import *
import time
#添加共享节点
class cepEngine2():
    def __init__(self):
        self.outputQueue = Queue()
        self.atomEventQueue = Queue()
        self.eventForest = eventForest()
        self.eventTree = eventTree()
        self.forest = forest_node('forest')
        #thread
        self.__insertThread = Thread(target = self.__insertAtomEvent)
        self.__detectionThread = Thread(target = self.__detection)
        self.__processThread = Thread(target = self.__process)

        #process
        self.__handler = {}

        self.seq = 0



    #The function is in charge of the insertion of atomEventData
    def __insertAtomEvent(self):
        while True:
            try:
                data = self.atomEventQueue.get()
                instance = self.getInstance(data)
                #print str(self.eventForest.nodeIndex)
                if self.eventForest.nodeIndex.has_key(instance.eTypeId):
                    nodes = self.eventForest.nodeIndex[instance.eTypeId]
                    for node in nodes:
                        limit = check()
                        if limit.checks(node,instance):
                            print u'向',node.eTypeId,u'节点插入实例'
                            node.instances.append(instance)    #向节点中插入实例
                        else:
                            print u'不满足约束条件'
                else:
                    print u'不存在实例所对应的事件类型'
            except Empty:
                time.sleep(.01)

    def __detection(self):
        while True:

            self.__detection1()
           # break

    def __detection1(self):
        for tree in self.forest.members:
            self.eventForest.postOrderProcess(tree)
            item = tree.children[0].instances
            while len(item)!=0:
                print u'输出实例'
                item[0].eTypeId = tree.complexEventID
                self.outputQueue.put(item[0])
                item.remove(item[0])

    def __detection2(self,node):
        childQueue = Queue()
        childQueue.put(node)
        while True:
            try:
                if childQueue.qsize() == 0:
                    break
                nodes = childQueue.get()
                for father in nodes.father:
                    if father.op!=None:#根节点的op为None,叶子节点的op为-1
                        op = operator()
                        newInstances = op.handler(father)
                        if newInstances !=None:
                            limit = check()
                            for item in newInstances:
                               if limit.checks(father,item):#若满足该节点的约束条件，则加入
                                 father.instances.append(item)
                            childQueue.put(father)
                    else:
                        #output the result
                        for instance in nodes.instances:
                            print 'output the instance'
                            instance.eTypeId = father.complexEventID
                            self.outputQueue.put(instance)

                temp = []
                for father in nodes.father:
                    if father.op != None:
                        temp.append(father.start[node.nodeId])
                if len(temp)>0:
                    for father in nodes.father:
                        father.start[node.nodeId] = father.start[node.nodeId]-min(temp)

                    for i in range(min(temp)):
                        nodes.instances.remove(nodes.instances[0])

            except Empty:
                break

    def __process(self):
        while True:
            try:
                output = self.outputQueue.get()
                if self.__handler.has_key(output.eTypeId):
                    funcs = self.__handler[output.eTypeId]
                    for item in funcs:
                        item(output)
            except Empty:
                time.sleep(.01)

    def put(self,data):
        instance = self.getInstance(data)
        if self.eventForest.nodeIndex.has_key(instance.eTypeId):
            nodes = self.eventForest.nodeIndex[instance.eTypeId]
            for node in nodes:
                limit = check()
                if limit.checks(node,instance):
                    print u'向',node.eTypeId,u'节点插入实例'
                    node.instances.append(instance)    #向节点中插入实例
                    self.__detection2(node)
                else:
                    print u'不满足约束条件'
        else:
            print u'不存在实例所对应的事件类型'



    def putAtomEvent(self,data):
        self.atomEventQueue.put(data)

    def putEventTree(self,fileName):
        input = FileStream(fileName)
        root = self.eventTree.getEventTree(input)
        self.eventForest.insertIndex(root) ##处理共享节点
        self.forest.members.append(root)

    def getInstance(self,data):
        self.seq+=0
        id = data['id']
        instance = eInstance_node(self.seq,id,time.time(),time.time())
        instance.attrs[id] = data
        return instance

    def register(self, eTypeId=None, handler=None):
        """注册事件处理函数监听"""
        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        if self.__handler.has_key(eTypeId):
            if handler not in self.__handler[eTypeId]:
                self.__handler[eTypeId].append(handler)
        else:
            self.__handler[eTypeId] = [handler]

    def unregister(self,eTypeId,handler):
        """注销事件处理函数监听"""
        #one
        if eTypeId!=None&handler!=None:
            if self.__handler.has_key(eTypeId):
                if handler in self.__handler[eTypeId]:
                    self.__handler[eTypeId].remove(handler)
                else:
                    del self.__handler[eTypeId]
        #two
        elif eTypeId != None&handler == None:
            if self.__handler.has_key(eTypeId):
                del self.__handler[eTypeId]
        #three
        elif eTypeId == None&handler!=None:
            for i,item in handler:
                if handler in self.__handler[i]:
                    self.__handler[i].remove(handler)

    def start(self):
        if self.__insertThread.isAlive() == False:
          self.__insertThread.start()
        if self.__detectionThread.isAlive() == False:
          self.__detectionThread.start()
        if self.__processThread.isAlive() == False:
          self.__processThread.start()

def handler(event):
    d = event.attrs
    print_dict(d)

def print_dict(d):
    for key,value in d.items():
        print key + ':'+str(value)

def mode1():
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
def main():
   mode1()

if __name__ =='__main__':
    main()
    pass