# -*- coding: utf8 -*-
from code.cedl_node import *
from Queue import Queue, Empty
import time

class operator():
    def __init__(self):
        self.pattern = {}
        self.pattern['and']=self.AND #测试通过
        self.pattern['not'] = self.NOT
        self.pattern['none']=self.ROOT
        self.pattern['seq']=self.SEQ #测试通过
        self.pattern['within']=self.WITHIN #测试通过
        self.pattern['repeat']=self.REPEAT #测试通过

        self.within = {}
        self.within['s'] = 1
        self.within['secs'] = 1
        self.within['m'] = 60
        self.within['mins'] = 60
        self.within['min'] = 60
        self.within['h'] = 3600
        self.within['hours'] = 3600
        self.within['hour'] = 3600
        self.within['d'] = 3600*12
        self.within['days'] = 3600*12
        self.within['day'] = 3600*12

        self.__queue = Queue()
        self.__queue2 = Queue()
        pass
    ##返回实例集合或None
    def handler(self,node):
        return  self.pattern[str(node.op).lower()](node)
        pass
    def AND(self,node):
        #step1:获取返回实例的个数
        li = []
        for i in range(node.childrenId):
            num = len(node.children[i].instances)
            li.append(num)
        count = min(li)
        if count == 0:
            return None

        #step2:初始化返回的实例
        newInstances = []
        for i in range(count):
            temp = eInstance_node(0,node.eTypeId,time.time(),time.time())
            newInstances.append(temp)

        #step3:给返回的实例填充数据
        for child in node.children:
            for j in range(count):
                instance = child.instances[node.start[child.nodeId]+j]#the jst instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[j].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[j].t0>instance.t0:
                        newInstances[j].t0 = instance.t0
                    if newInstances[j].t1<instance.t1:
                        newInstances[j].t1 = instance.t1

                #child.instances.remove(child.instances[0]) #移除子节点实例
        '''
        #step3:remove the instances of the children
        for child in node.children:
            while node.start[child.nodeId]>0:
                child.instances.remove(child.instances[0])
                node.start[child.nodeId]-=1
        '''

        return newInstances

    def NOT(self,node):

        pass

    def REPEAT(self,node):
        newInstances = []
        child = node.children[0]
        n = int(node.repeatNum)
        count = len(child.instances)/n
        if count > 0:
            for i in range(count):
                newInstance = eInstance_node(0,node.eTypeId,time.time(),time.time())
                #每个实例包含子节点的n个实例
                for j in range(n):
                    #instance = child.instances[0]
                    instance = child.instances[node.start[child.nodeId]+i*n+j]#the jst instance
                    attr = instance.attrs
                    for key in attr.keys():
                        newInstance.attrs[key] = attr[key]  #给返回的实例填充数据
                        if newInstance.t0>instance.t0:
                          newInstance.t0 = instance.t0
                        if newInstance.t1<instance.t1:
                            newInstance.t1 = instance.t1
                    #child.instances.remove(instance)
                newInstances.append(newInstance)

            #step3:remove the instances of the children
            '''
            for child in node.children:
              while node.start[child.nodeId]>0:
                  child.instances.remove(child.instances[0])
                  node.start[child.nodeId]-=1
           '''

            return newInstances

        else:
            return None

    #There are two ways for solving the seq operator:
    #First_way
    #Second_way
    #This is the first way
    #测试通过
    def SEQ(self,node):
        newInstances = []
        while True:
            #step1:initiate the t time
            #print 'enter....'
            if len(node.children)>0:
                n = node.children[0]
                if len(n.instances) > node.start[n.nodeId]:
                    t = n.instances[node.start[n.nodeId]].t1
                else:
                    return None
            else:
               return None
            temp = []
            for child in node.children:
                if len(child.instances)>node.start[child.nodeId]:
                    #instance = children.instances[0]
                    #find one instance where its time is larger than time

                    while len(child.instances)>node.start[child.nodeId]:
                        #print len(child.instances),node.start[child.nodeId]
                        instance = child.instances[node.start[child.nodeId]]
                        node.start[child.nodeId]+=1
                        if instance.t1 >= t:
                            temp.append(instance)
                            t = instance.t1
                            break

                else:
                    break
            #step2:fill the newInstance
            if len(temp) == len(node.children):
                newInstance = eInstance_node(0,node.eTypeId,time.time(),time.time())
                for item in temp:
                    attr = item.attrs
                    for key in attr.keys():
                        newInstance.attrs[key] = attr[key]  #给返回的实例填充数据
                        if newInstance.t0>instance.t0:
                          newInstance.t0 = instance.t0
                        if newInstance.t1<instance.t1:
                            newInstance.t1 = instance.t1

                newInstances.append(newInstance)
            else:
                #print 'out...'
                for i in range(len(temp)):
                    node.start[node.children[i].nodeId]-=1
                break
        '''
        #step3:remove the instances of the children
        for child in node.children:
            while node.start[child.nodeId]>0:
                child.instances.remove(child.instances[0])
                node.start[child.nodeId]-=1
        '''
        return newInstances
    #测试通过
    def WITHIN(self,node):
        if len(node.children[0].instances) == 0:
            return None
        #step1:初始化返回的实例
        newInstances = []

         #step2:检测实例是否满足时间限制，并给返回的实例填充数据，修改时间

        while len(node.children[0].instances)>node.start[node.children[0].nodeId]:
            instance = node.children[0].instances[node.start[node.children[0].nodeId]]
            node.start[node.children[0].nodeId]+=1
            cur = time.time()
           # print 'key',str(node.timeunit).lower()
            factor = self.within[str(node.timeunit).lower()]#upper为大写
            if factor == None:
                factor = 1
            if ((cur - instance.t0)/factor) < node.timeval:
                newInstance = eInstance_node(0,node.eTypeId,0,0)
                attr = instance.attrs
                for key in attr.keys():
                    newInstance.attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstance.t0>instance.t0:
                        newInstance.t0 = instance.t0
                    if newInstance.t1<instance.t1:
                        newInstance.t1 = instance.t1
                newInstances.append(newInstance)
        '''
        #step3：清空子节点
        for child in node.children:
            while node.start[child.nodeId]>0:
                child.instances.remove(child.instances[0])
                node.start[child.nodeId]-=1
        '''

        return newInstances

        pass
    def ROOT(self,node):
        s = [3,9,7,8]
        s.remove(s[0])
        s.remove(s[0])
        s.remove(s[0])
        c = len(s)
        print min(s),len(s)
        pass
     #访问事件树
    def visit(self,node):
        self.__queue.put(node)
        while(True):
            if self.__queue.qsize() == 0:
                break
            try:
                item = self.__queue.get()
                num = item.childrenId
                #将孩子节点入队
                for i in range(0,num):
                    self.__queue.put(item.children[i])
                 #打印孩子节点的相关信息
                print item.eTypeId
                if len(item.instances)!=0:
                    print "存在实例"
                    print item.instances[0].eTypeId
                #print item
            except Empty:
                print "exit"
                break
        pass
    #访问限制节点
    def visitLimits(self,node):
        for item in node:
            print "-----------------------"

            print item.restrictions['op']
            print item.restrictions['event_name']
            print item.restrictions['event_attr']
            print item.restrictions['value']
            print "------------------------"

        pass
    #访语法树
    def visit2(self,node):
        self.__queue2.put(node)
        while(True):
            try:
                item = self.__queue2.get()
                if(self.isChild(item)==False):
                    num = self.getNumberOfChild(item)
                    for i in range(0,num):
                        self.__queue2.put(item.getChild(i))
                    print item
                else:
                    print item

                #print item
            except Empty:
                print "exit"
                break
        pass
    def isChild(self,node):
        if(node.getChild(0)==None):
            return True
        else:
            return False
    def getNumberOfChild(self,node):
        i = 0
        while(True):
            if(node.getChild(i)!=None):
                i+=1
            else:
                return i
        pass
def main():
    op = operator()
    temp = eInstance_node(0,'fdg',time.time(),time.time())

if __name__ == "__main__":
    main()