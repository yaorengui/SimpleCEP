# -*- coding: utf8 -*-
import shelve
from eventForest import *
from Queue import Queue, Empty
from threading import Thread
from cedlLimit import *
import time
from antlr4.InputStream import InputStream
#添加共享节点
class cepEngine2():
    def __init__(self):
        self.numberOfComplexEvent = 0 #用于统计产生的复杂事件数
        self.outputQueue = Queue()#复杂事件队列 （输出）
        self.atomEventQueue = Queue()#原子事件队列 （输入）
        self.detectQueue = Queue() #atomEventQueue队列中的原子事件经检验合格的实例

        self.eventForest = eventForest(self)
        self.eventTree = eventTree(self)
        self.forest = forest_node('forest')
        #thread
        #负责插入原子事件到原子事件队列中，将成果插入的原子事件放入detectQueue队列中
        self.__insertThread = Thread(target = self.__insertAtomEvent)
        self.__detectionThread = Thread(target = self.__detection)#复杂复杂事件的检测
        self.__processThread = Thread(target = self.__process)#负责处理复杂事件的输出

        #process
        self.__handler = {}

        self.seq = 0

        self.traceQueue = Queue()#节点轨迹队列，演示实验时，用于跟踪结点处理顺序

    #The function is in charge of the insertion of atomEventData
    #不合适的原子事件不插入

    def __insertAtomEvent(self):
        while True:
            try:
                data = self.atomEventQueue.get()
                nodes = self.putDataToAtomNode(data)
                for node in nodes:
                    self.detectQueue.put(node)
            except Empty:
                time.sleep(.01)

    def __detection(self):
        while True:
            try:
                node = self.detectQueue.get()
                self.oneDetection(node)
            except Empty:
                time.sleep(.01)

    def __detection1(self):
        for tree in self.forest.members:
            self.eventForest.postOrderProcess(tree)
            item = tree.children[0].instances
            while len(item)!=0:
                print u'输出实例'
                item[0].eTypeId = tree.complexEventID
                self.outputQueue.put(item[0])
                item.remove(item[0])

    #自顶向上检测
    #从原子事件队列中取出原子事件，自顶向上检测
    def oneDetection(self,node):
        childQueue = Queue()
        childQueue.put(node)
        while True:
            #temp = []#存储一次原子事件引起的事件操作
            try:
                if childQueue.qsize() == 0:
                    break
                nodes = childQueue.get()
                self.traceQueue.put(nodes)#保存节点处理轨迹
                for father in nodes.father:
                    op = operator(self)
                    newInstances = op.handler(father,nodes)
                    limit = check()
                    for item in newInstances:
                        if limit.checks(father,item):
                            father.instances.append(item)
                            if father.op!='root':
                                childQueue.put(father)
                                #pass
                                #print 123
                            else:
                                while len(father.instances)>0:
                                    instance = father.instances[0]
                                    instance.eTypeId = father.complexEventID
                                    #self.outputQueue.put(instance)
                                    self.numberOfComplexEvent +=1


                                    #print instance.attrs['avg1'],instance.attrs['avg2']
                                    father.instances.remove(instance)
                                #print 123
                                #father.instances = []
                                #father.start[0] = 0

                temp = []
                #寻找最小father对node的最小起始位置
                for i,father in enumerate(nodes.father):
                    temp.append(father.start[nodes.nodeId[i]])


                if len(temp)>0:
                    for i,father in enumerate(nodes.father):
                        father.start[nodes.nodeId[i]]-=min(temp)

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
        #nodes = self. putDataToAtomNode(data)#共享型
        nodes = self.putToNode(data)
        for node in nodes:
            self.oneDetection(node)
            pass

    def putToNode(self,data):
        r = []
        instance = self.getInstance(data)
        #print self.eventForest.nodeIndex.keys()
        for key in self.eventForest.nodeIndex.keys():
            #print instance.eTypeId
            item = self.eventForest.nodeIndex[key]
            if item.eTypeId == instance.eTypeId:

                limit = check()
                #print limit.checks(item,instance)
                if limit.checks(item,instance):
                    #print 'ss'
                    item.instances.append(instance)    #需要处理的叶子结点
                    r.append(item)
                #else:
                    #item.instances.append(instance)    #需要处理的叶子结点
                    #r.append(item)

        return r
    #将原子事件实例插入叶子结点
    def putDataToAtomNode(self,data):
        r = []
        instance = self.getInstance(data)
        if self.eventForest.nodeIndex.has_key(instance.eTypeId):
            node = self.eventForest.nodeIndex[instance.eTypeId]
            limit = check()
            if limit.checks(node,instance):
                #print u'向',node.eTypeId,u'节点插入实例'
                node.instances.append(instance)    #向节点中插入实例
                r.append(node)
            else:
                #print u'不满足约束条件'
                pass
        else:
            #print u'不存在实例所对应的事件类型'
            pass

        return r


    def putAtomEvent(self,data):
        self.atomEventQueue.put(data)

    def putEventTree(self,fileName):
        input = FileStream(fileName)
        root = self.eventTree.getEventTree(input)
        self.eventForest.insertIndex(root) ##处理共享节点
        self.forest.members.append(root)
    #putEventTreeToForestWithCEDL
    def addEventWithCedl(self,str_cedl,share):
        input = InputStream(str_cedl)
        root = self.eventTree.getEventTree(input)
        self.eventForest.insertIndex(root,share) ##处理共享节点
        self.forest.members.append(root)
        return root
        pass

    def getInstance(self,data):
        self.seq += 1
        id = data['id']
        #print self.seq
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

    def getNodeInformation(self,node):
        pass

def handler(event):
    d = event.attrs
    #print_dict(d)

def print_dict(d):
    for key,value in d.items():
        #print key + ':'+str(value)
        pass

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
    #mode1()
    pass


if __name__ =='__main__':
    main()
    pass