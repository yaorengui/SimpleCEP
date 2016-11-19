# -*- coding: utf8 -*-
from cedl_node import *
from eventForest import *
from Queue import Queue, Empty
from threading import Thread
import time
from cedlLimit import *
class cepEngine():
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
                for tree in self.forest.members:
                    self.eventTree.insertInstance(instance,tree)
            except Empty:
                time.sleep(.01)

    def __detection(self):
        while True:
            for tree in self.forest.members:
                self.eventForest.postOrderProcess(tree)
                item = tree.children[0].instances
                while len(item)!=0:
                    print u'输出实例'
                    item[0].eTypeId = tree.complexEventID
                    self.outputQueue.put(item[0])
                    item.remove(item[0])

           # break
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
        for tree in self.forest.members:
            #1.插入原子事件
            node = self.eventTree.insertInstance(instance,tree)
            #2.向上检测各个非叶子节点是否有新实例生成
            if node != None:
                while True:
                    if len(node.father)>0:
                        node = node.father[0]
                        #访问非叶子节点，生成新的实例
                        if (node.op != '-1')&(node.op!=None):#根节点的op为None,叶子节点的op为-1
                            op = operator()
                            newInstances = op.handler(node)
                            for i,child in enumerate(node.children):
                                while node.start[i]>0:
                                    child.instances.remove(child.instances[0])
                                    node.start[i]-=1

                            if newInstances !=None:
                                limit = check()
                                for item in newInstances:
                                   if limit.checks(node,item):#若满足该节点的约束条件，则加入
                                     node.instances.append(item)
                            else:
                                break#没有新的实例生成时，退出循环
                    else:
                        break#访问到根节点时，退出循环
            else:
                continue
            #查看是否有实例，有实例则输出实例
            item = tree.children[0].instances
            while len(item)!=0:
                print u'输出实例',tree.complexEventID
                item[0].eTypeId = tree.complexEventID
                #self.outputQueue.put(item[0])

                #事件处理
                if self.__handler.has_key(item[0].eTypeId):
                    funcs = self.__handler[item[0].eTypeId]
                    for func in funcs:
                        func(item[0])

                item.remove(item[0])


    def putAtomEvent(self,data):
        self.atomEventQueue.put(data)

    def putEventTree(self,fileName):
        input = FileStream(fileName)
        root = self.eventTree.getEventTree(input)
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
'''
def handler(event):
    print event.eTypeId
    data = event.attrs #实例数据为字典格式，存储复杂事件涉及到的所有原子事件的数据
    print data['E1']['id'],data['E1']['name'],data['E1']['password']

def main():
    #step1:start the complexEventEngine
    engine = cepEngine()
    engine.start()
    #step2:define the complex event
    engine.putEventTree('input1.txt')

   #step3:define the data sources
    data = {}
    data['id'] = 'E1'
    data['name'] = 'yao'
    data['password']=123


    engine.putAtomEvent(data)

    data = {}
    data['id'] = 'E2'
    data['name'] = 'yang'
    data['password']=123

    engine.putAtomEvent(data)

    #step4:define the handler
    engine.register('complexEvent',handler)#当发生complexEvent时,执行handler,参数为complexEvent涉及到的所有原子事件数据




    #limits = cepEngine.forest.members[0].attach
    #op = operator()
    #op.visitLimits(limits)
'''
'''

if __name__ =='__main__':
    main()
    pass
'''
