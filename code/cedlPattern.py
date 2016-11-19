# -*- coding: utf8 -*-
from code.cedl_node import *
from Queue import Queue, Empty
import time

class operator():
    def __init__(self,cep2):
        self.cep = cep2
        self.pattern = {}
        self.pattern['recent.and']=self.recentAnd
        self.pattern['recent.or']=self.Or
        self.pattern['recent.seq']=self.recentSeq
        self.pattern['recent.not']=self.recentNot
        self.pattern['recent.within']=self.recentWithin
        self.pattern['recent.repeat']=self.recentRepeat
        self.pattern['recent.root']=self.ROOT

        self.pattern['chronicle.and']=self.chronicleAnd
        self.pattern['chronicle.seq']=self.continuousSeq #顺序环境与连续环境操作步骤一样
        self.pattern['chronicle.root']=self.ROOT

        self.pattern['continuous.and']=self.continuousAnd
        self.pattern['continuous.seq']=self.continuousSeq
        self.pattern['continuous.root']=self.ROOT

        self.pattern['cumulative.and']=self.cumulativeAnd
        self.pattern['cumulative.seq']=self.cumulativeSeq
        self.pattern['cumulative.root']=self.ROOT


        self.pattern['and']=self.AND #测试通过
        self.pattern['not'] = self.NOT
        self.pattern['root']=self.ROOT
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
    def handler(self,node,child):
        if self.pattern.has_key(str(node.op).lower()):
            key = str(node.context).lower()+'.'+str(node.op).lower()
            return  self.pattern[key](node,child)
        else:
            print 'no exist key',str(node.op)
            return []
    def cumulativeSeq(self,node,child):
        #print node.start[0],node.start[1],len(node.children[0].instances),len(node.children[1].instances)
        #print len(node.children[0].instances),len(node.children[1].instances)
        #for i in node.seqt:
            #print i
        newInstances = []

        for i,item in enumerate(node.seqt):
            if node.seqt[i] == -1:
                if node.children[i] != child:
                    break
                elif i == 0:
                    node.seqt[i] = 0
                    node.start[i] = len(node.children[i].instances)-1
                    #print node.seqt[0],node.seqt[1],child.eTypeId
                else:
                    #print node.seqt[0],node.seqt[1],child.eTypeId
                    node.last[i-1] = len(node.children[i-1].instances)-1
                    node.start[i] = len(node.children[i].instances)-1
                    if i == node.childrenId - 1:
                        node.last[i] = len(node.children[i].instances)-1
                        #生成复杂事件
                        temp = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
                        newInstances.append(temp)
                        temp.attrs['eSeq'] = []
                        temp.attrs['eTypeId'] = []
                        for j,item in enumerate(node.children):
                            for k in range(node.last[j]-node.start[j]+1):
                              self.mergeInstanceWithEseq(item.instances[node.start[j]+k],temp)
                            node.start[j] = node.last[j]+1
                        self.cep.numberOfComplexEvent+=1
                        #跟新seqt、last
                        for s,item in enumerate(node.seqt):
                            node.seqt[s] = -1
                            node.last[s] = -1
                    #print node.seqt[0],node.seqt[1],child.eTypeId
                break
        self.removeChildInstances(node)
        return newInstances
        pass

    def cumulativeAnd(self,node,child):
        newInstances = []
        for i in range(node.childrenId):
            if len(node.children[i].instances)-1 < node.start[i]:
                return newInstances
        #生成复杂事件
        temp = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
        newInstances.append(temp)
        self.cep.numberOfComplexEvent+=1
        temp.attrs['eSeq'] = []
        temp.attrs['eTypeId'] = []
        for i,item in enumerate(node.children):
            for j in range(len(item.instances)-node.start[i]):
              self.mergeInstanceWithEseq(item.instances[node.start[i]+j],temp)
            #修改start
            node.start[i] = len(item.instances)
            #print 's', len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
            self.removeChildInstances(node)
            #print 'e',len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
        #孩子实例更新

        return newInstances

    def mergeInstanceWithEseq(self,source,dest):
        dest.attrs['eSeq'].append(source.eSeq)
        dest.attrs['eTypeId'].append(source.eTypeId)
    def continuousAnd(self,node,child):
        #print 'len',len(node.children[0].instances),len(node.children[1].instances)
        #if len(node.children[0].instances)-1 >= node.start[0] &len(node.children[1].instances)-1 >= node.start[1]:
           #print node.children[0].instances[node.start[0]].eSeq,node.children[1].instances[node.start[1]].eSeq
        ##step1检测是否满足复杂事件生成条件
        newInstances = []
        #若其中一个孩子结点为空，返回[]
        min1 = 0
        while True:
            for i in range(node.childrenId):
                #print i,node.start[0],node.start[1]
                if len(node.children[i].instances)-1 < node.start[i]:
                    return newInstances
                else:
                    temp =node.children[0].instances[node.start[0]].eSeq
                    if node.children[i].instances[node.start[i]].eSeq < temp:
                        temp = node.children[i].instances[node.start[i]].eSeq
                        min1 = i
            #print 'ddd'
            #step2:初始化返回的实例
            self.cep.seq+=1
            temp = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
            newInstances.append(temp)
            self.cep.numberOfComplexEvent+=1
            #step3:给返回的实例填充数据
            for i,child in enumerate(node.children):
                instance = child.instances[node.start[i]]#the node.start[i] instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[0].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[0].t0>instance.t0:
                        newInstances[0].t0 = instance.t0
                    if newInstances[0].t1<instance.t1:
                        newInstances[0].t1 = instance.t1

            node.start[min1]+=1
            #print '222',min1

            fathers = node.children[min1].father
            #print len(node.children[min1].father)

            seq = []
            #求删除实例的个数
            for i in range(len(fathers)):
                seq.append(fathers[i].start[node.children[min1].nodeId[i]])
                #print i,node.children[min1].nodeId[0],node.children[min1].nodeId[1]
            #删除实例
            #print min(seq)
            for j in range(min(seq)):
                node.children[min1].instances.remove(node.children[min1].instances[0])
            #修改start
            for k in range(len(fathers)):
                fathers[k].start[node.children[min1].nodeId[k]]-=min(seq)

    def continuousSeq(self,node,child):
        newInstances = []
        if node.seqt[len(node.seqt)-1] == 0:
            #实例生成
            #step2:初始化返回的实例
            self.cep.seq += 1
            temp = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
            newInstances.append(temp)
            self.cep.numberOfComplexEvent+=1
            #step3:给返回的实例填充数据
            for i,child in enumerate(node.children):
                #print i,node.start[i],len(child.instances),'dd'
                instance = child.instances[node.start[i]]#the node.start[i] instance
                #print node.start[i]
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[0].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[0].t0>instance.t0:
                        newInstances[0].t0 = instance.t0
                    if newInstances[0].t1<instance.t1:
                        newInstances[0].t1 = instance.t1

            #修改seqt数组
            for i in range(len(node.seqt)):
                node.seqt[i] = -1

            #开始新的实例生成
            if len(node.children[0].instances)-1>=node.start[0]+1:
                node.start[0] +=1
                node.seqt[0] = 0
                #跟新后面的start、seqt
                temp = node.children[0].instances[node.start[0]].eSeq
                for i in range(len(node.start)-1):
                    for j,item in enumerate(node.children[i+1].instances):
                        if item.eSeq > temp:
                            node.seqt[i+1] = 0
                            node.start[i+1] = j
                            temp = item.eSeq
                            break
            #for item in node.seqt:
                #print 'dddd',item
        else:
            #开始新的实例生成
            if node.seqt[0] == -1:
                #开始新的实例生成
                if len(node.children[0].instances)-1>=node.start[0]+1:
                    #print 'node'
                    node.start[0] +=1
                    node.seqt[0] = 0
                    #跟新后面的start、seqt
                    temp = node.children[0].instances[node.start[0]].eSeq
                    for i in range(len(node.start)-1):
                        for j,item in enumerate(node.children[i+1].instances):
                            if item.eSeq > temp:
                                node.seqt[i+1] = 0
                                temp = item.eSeq
                                node.start[i+1] = j
                                break
                    #for item in node.seqt:
                       #print 'dddd',item
            else:
                #print 'ddd'
                for i,seq in enumerate(node.seqt):
                    if node.seqt[len(node.seqt)-i-1] == 0:
                        #print 'd'
                        temp1 = node.children[len(node.seqt)-i-1].instances[node.start[len(node.seqt)-i-1]].eSeq
                        #print temp1
                        for j,item in enumerate(node.children[len(node.seqt)-i].instances):
                            if item.eSeq > temp1:
                                node.seqt[len(node.seqt)-i] = 0
                                node.start[len(node.seqt)-i] = j
                                break

        #step5:通用，删除过期实例，并更新start数组
        for child in node.children:
            fathers = child.father
            seq = []
            #求删除实例的个数
            for i in range(len(fathers)):
                seq.append(fathers[i].start[child.nodeId[i]])

            #删除实例
            for j in range(min(seq)):
                child.instances.remove(child.instances[0])
            #修改start
            for k in range(len(fathers)):
                fathers[k].start[child.nodeId[k]]-=min(seq)
                pass
        #print len(newInstances)
        return newInstances

    def recentAnd(self,node,child):
        #step1检测是否满足复杂事件生成条件
        newInstances = []
        #若其中一个孩子结点为空，返回[]
        for i in range(node.childrenId):
            if len(node.children[i].instances)-1<=node.start[i]:
                return []
        #step2:初始化返回的实例
        temp = eInstance_node(0,node.eTypeId,time.time(),0)
        newInstances.append(temp)
        self.cep.numberOfComplexEvent+=1
        #step3:给返回的实例填充数据
        for i,child in enumerate(node.children):
                instance = child.instances[len(child.instances)-1]#the last instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[0].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[0].t0>instance.t0:
                        newInstances[0].t0 = instance.t0
                    if newInstances[0].t1<instance.t1:
                        newInstances[0].t1 = instance.t1

        #step4:跟新start数组
        for i in range(len(node.start)):
            node.start[i] = len(node.children[i].instances)-1

        #print 's', len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
        self.removeChildInstances(node)
        #print 'e',len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
        return newInstances
        pass
    def recentSeq(self,node,child):
        newInstances = []
        if node.children.index(child) == len(node.children)-1:
            teSeq = child.instances[len(child.instances)-1].eSeq
            indexs = [] #实例索引集，预组成Seq类型的复杂事件
            indexs.append(len(child.instances)-1)
            node.start[len(node.children)-1] = len(child.instances)-1
            for i in range(node.childrenId-1):
                index = node.childrenId-1-1-i
                flag = False#标记是否找到比teseq小的实例，初始化为False
                for j in range(len(node.children[index].instances)-1):
                    insindex = len(node.children[index].instances) -1 -j
                    if node.children[index].instances[insindex].eSeq < teSeq:
                        teSeq = node.children[index].instances[insindex].eSeq
                        indexs.append(insindex)
                        node.start[index] = insindex
                        flag = True
                        break
                #判定是否继续
                if flag == False:
                    break
            #组成复杂事件
            if len(indexs) == node.childrenId:
                temp = self.getComplexWithIndexs(node,indexs)
                newInstances.append(temp)
                self.cep.numberOfComplexEvent+=1
                #修改start

                for i in range(node.childrenId):
                    node.start[i] = indexs[node.childrenId-1-i]


            #print 's', len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
            self.removeChildInstances(node)
            #print 'e',len(node.children[0].instances),node.start[0],len(node.children[1].instances),node.start[1]
        return newInstances

    #倒着数，recentSeq专用
    def getComplexWithIndexs(self,node,indexs):
        #print indexs[0],indexs[1],len(node.children[0].instances),len(node.children[1].instances)
        self.cep.seq += 1
        instance = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
        #step3:给返回的实例填充数据
        for i,child in enumerate(node.children):
            instance = child.instances[indexs[len(indexs)-i-1]]
            attr = instance.attrs
            for key in attr.keys():
                instance.attrs[key] = attr[key]  #给返回的实例填充数据
                if instance.t0>instance.t0:
                    instance.t0 = instance.t0
                if instance.t1<instance.t1:
                    instance.t1 = instance.t1
        return instance

    def removeChildInstances(self,node):
        #step`1:通用，删除过期实例，并更新start数组
        for a,child in enumerate(node.children):
            fathers = child.father
            seq = []
            #求删除实例的个数
            for i in range(len(fathers)):
                seq.append(fathers[i].start[child.nodeId[i]])
            #删除实例
            for j in range(min(seq)):
                node.children[a].instances.remove(child.instances[0])
            #修改start
            for k in range(len(fathers)):
                fathers[k].start[child.nodeId[k]]-=min(seq)


    def recentSeq2(self,node):
        newInstances = []
        if node.seqt[len(node.seqt)-1] == 0:
            #实例生成
            #step2:初始化返回的实例
            self.cep.seq += 1
            temp = eInstance_node(self.cep.seq,node.eTypeId,time.time(),0)
            newInstances.append(temp)
            #step3:给返回的实例填充数据
            for i,child in enumerate(node.children):
                #print i,node.start[i],len(child.instances),'dd'
                instance = child.instances[node.start[i]]#the node.start[i] instance
                #print node.start[i]
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[0].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[0].t0>instance.t0:
                        newInstances[0].t0 = instance.t0
                    if newInstances[0].t1<instance.t1:
                        newInstances[0].t1 = instance.t1

            #修改seqt数组
            for i in range(len(node.seqt)):
                node.seqt[i] = -1

            #开始新的实例生成
            if len(node.children[0].instances)-1>=node.start[0]+1:
                node.start[0] +=1
                node.seqt[0] = 0
                #跟新后面的start、seqt
                temp = node.children[0].instances[node.start[0]].eSeq
                for i in range(len(node.start)-1):
                    for j,item in enumerate(node.children[i+1].instances):
                        if item.eSeq > temp:
                            node.seqt[i+1] = 0
                            node.start[i+1] = j
                            temp = item.eSeq
                            break
            #for item in node.seqt:
                #print 'dddd',item
        else:
            #开始新的实例生成
            if node.seqt[0] == -1:
                #开始新的实例生成
                if len(node.children[0].instances)-1>=node.start[0]+1:
                    #print 'node'
                    node.start[0] +=1
                    node.seqt[0] = 0
                    #跟新后面的start、seqt
                    temp = node.children[0].instances[node.start[0]].eSeq
                    for i in range(len(node.start)-1):
                        for j,item in enumerate(node.children[i+1].instances):
                            if item.eSeq > temp:
                                node.seqt[i+1] = 0
                                temp = item.eSeq
                                node.start[i+1] = j
                                break
                    #for item in node.seqt:
                       #print 'dddd',item
            else:
                #print 'ddd'
                for i,seq in enumerate(node.seqt):
                    if node.seqt[len(node.seqt)-i-1] == 0:
                        #与顺序环境和连续环境唯一不同的地方
                        #跟新下标为len(node.seqt)-i-1的孩子结点
                        #***********************************************


                        #***********************************************
                        #print 'd'
                        temp1 = node.children[len(node.seqt)-i-1].instances[node.start[len(node.seqt)-i-1]].eSeq
                        #print temp1
                        for j,item in enumerate(node.children[len(node.seqt)-i].instances):
                            if item.eSeq > temp1:
                                node.seqt[len(node.seqt)-i] = 0
                                node.start[len(node.seqt)-i] = j
                                break

        #step5:通用，删除过期实例，并更新start数组
        for child in node.children:
            fathers = child.father
            seq = []
            #求删除实例的个数
            for i in range(len(fathers)):
                seq.append(fathers[i].start[child.nodeId[i]])

            #删除实例
            for j in range(min(seq)):
                child.instances.remove(child.instances[0])
            #修改start
            for k in range(len(fathers)):
                fathers[k].start[child.nodeId[k]]-=min(seq)
                pass
        #print len(newInstances)
        return newInstances
        pass

    def recentSeq1(self,node):
        newInstances = []

        if len(node.children[0].instances)!=0:
            #print len(node.seqt)
            node.seqt[0] = 0

        if node.seqt[len(node.seqt)-1]>-1:
            #step1:初始化返回的实例
            temp = eInstance_node(0,node.eTypeId,time.time(),0)
            newInstances.append(temp)
            #step3:给返回的实例填充数据
            for i,child in enumerate(node.children):
                #print i,node.start[i], node.start[len(node.start)-1],len(child.instances)
                instance = child.instances[node.start[i]]#the node.start[i] instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[0].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[0].t0>instance.t0:
                        newInstances[0].t0 = instance.t0
                    if newInstances[0].t1<instance.t1:
                        newInstances[0].t1 = instance.t1
            for i in range(len(node.seqt)):
                node.seqt[i] = -1
            if len(node.children[0].instances)!=0:
                node.seqt[0] = 0

        else:
            for i in node.start:
                #print len(node.seqt)-i+1
                if node.seqt[len(node.seqt)-i-1]!=-1:
                    node.start[len(node.seqt-i-1)] = len(node.children[len(node.seqt)-i-1].instances)-1
                    if i!=len(node.start)-1:
                        node.start[len(node.seqt-i)] = len(node.children[len(node.seqt)-i].instances)-1
                    break
            pass

        return newInstances
        pass

    def recentNot(self,node):

        pass

    def recentWithin(self,node):


        pass

    def recentRepeat(self,node):

        pass

    def chronicleAnd(self,node,child):
        #step1:获取返回实例的个数
        li = []
        newInstances = []
        for i in range(node.childrenId):
            num = len(node.children[i].instances)
            li.append(num)
        count = min(li)
        if count == 0:
            return newInstances
        #step2:初始化返回的实例
        for i in range(count):
            temp = eInstance_node(0,node.eTypeId,time.time(),0)
            newInstances.append(temp)
            self.cep.numberOfComplexEvent+=1
        #step3:给返回的实例填充数据
        for i,child in enumerate(node.children):
            for j in range(count):
                instance = child.instances[node.start[i]+j]#the jst instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[j].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[j].t0>instance.t0:
                        newInstances[j].t0 = instance.t0
                    if newInstances[j].t1<instance.t1:
                        newInstances[j].t1 = instance.t1

        #每个子结点实例的起始位置＋count
        for i in range(len(node.start)):
            node.start[i]+=count

        self.removeChildInstances(node)
        return newInstances
        pass

    def chronicleSeq(self,node,child):
        newInstances = []
        while True:
            #step1:initiate the t time
            #print 'enter....'
            if len(node.children)>0:
                n = node.children[0]
                if len(n.instances) > node.start[0]:
                    t = n.instances[node.start[0]].t1
                else:
                    #print node.start[0],'Return None'
                    return newInstances
            else:
                #print 'Return None'
                return newInstances
            temp = []
            for i,child in enumerate(node.children):
                if len(child.instances)>node.start[i]:
                    #instance = children.instances[0]
                    #find one instance where its time is larger than time

                    while len(child.instances)>node.start[i]:
                        instance = child.instances[node.start[i]]
                        node.start[i]+=1
                        if instance.t1 >= t:
                            temp.append(instance)
                            t = instance.t1
                            break

                else:
                    break
            #step2:fill the newInstance
            if len(temp) == len(node.children):
                newInstance = eInstance_node(0,node.eTypeId,time.time(),0)
                self.cep.numberOfComplexEvent+=1
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
                    node.start[i]-=1
                break
        return newInstances
        pass

    def Or(self,node):

        pass

    def AND(self,node):
        #step1:获取返回实例的个数
        li = []
        newInstances = []
        for i in range(node.childrenId):
            num = len(node.children[i].instances)
            li.append(num)
        count = min(li)
        if count == 0:
            return newInstances
        #step2:初始化返回的实例
        for i in range(count):
            temp = eInstance_node(0,node.eTypeId,time.time(),0)
            newInstances.append(temp)
        #step3:给返回的实例填充数据
        for i,child in enumerate(node.children):
            for j in range(count):
                instance = child.instances[node.start[i]+j]#the jst instance
                attr = instance.attrs
                for key in attr.keys():
                    newInstances[j].attrs[key] = attr[key]  #给返回的实例填充数据
                    if newInstances[j].t0>instance.t0:
                        newInstances[j].t0 = instance.t0
                    if newInstances[j].t1<instance.t1:
                        newInstances[j].t1 = instance.t1

        #每个子结点实例的起始位置＋count
        for i in range(len(node.start)):
            node.start[i]+=count

        for child in node.children:
            fathers = child.father
            seq = []
            #求删除实例的个数
            for i in range(len(fathers)):
                seq.append(fathers[i].start[child.nodeId[i]])
            #删除实例
            for j in range(min(seq)):
                child.instances.remove(child.instances[0])
            #修改start
            for k in range(len(fathers)):
                fathers[k].start[child.nodeId[k]]-=1
                pass
            pass

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
                newInstance = eInstance_node(0,node.eTypeId,time.time(),0)
                #每个实例包含子节点的n个实例
                for j in range(n):
                    #instance = child.instances[0]
                    instance = child.instances[node.start[0]+i*n+j]#the jst instance
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
            return newInstances

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
                if len(n.instances) > node.start[0]:
                    t = n.instances[node.start[0]].t1
                else:
                    #print node.start[0],'Return None'
                    return newInstances
            else:
                #print 'Return None'
                return newInstances
            temp = []
            for i,child in enumerate(node.children):
                if len(child.instances)>node.start[i]:
                    #instance = children.instances[0]
                    #find one instance where its time is larger than time

                    while len(child.instances)>node.start[i]:
                        instance = child.instances[node.start[i]]
                        node.start[i]+=1
                        if instance.t1 >= t:
                            temp.append(instance)
                            t = instance.t1
                            break

                else:
                    break
            #step2:fill the newInstance
            if len(temp) == len(node.children):
                newInstance = eInstance_node(0,node.eTypeId,time.time(),0)
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
                    node.start[i]-=1
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
        newInstances = []
        if len(node.children[0].instances) == 0:
            return newInstances
         #step2:检测实例是否满足时间限制，并给返回的实例填充数据，修改时间

        while len(node.children[0].instances)>node.start[0]:
            instance = node.children[0].instances[node.start[0]]
            node.start[0]+=1
            cur = time.time()
           # print 'key',str(node.timeunit).lower()
            factor = self.within[str(node.timeunit).lower()]#upper为大写
            if factor == None:
                factor = 1
            if ((cur - instance.t0)/factor) < node.timeval:
                newInstance = eInstance_node(0,node.eTypeId,time.time(),0)
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

    def findIndex(self,child,father):
        for i,item in enumerate(father.children):
            if child.id == item.id:
                return i
        return None

    def ROOT(self,node,child):
        newInstances = []
        while len(node.children[0].instances)>node.start[0]:
            instance = node.children[0].instances[node.start[0]]
            attr = instance.attrs
            node.start[0]+=1
            newInstance = eInstance_node(0,node.eTypeId,time.time(),0)

            for key in attr.keys():
                newInstance.attrs[key] = attr[key]  #给返回的实例填充数据
                if newInstance.t0>instance.t0:
                    newInstance.t0 = instance.t0
                if newInstance.t1<instance.t1:
                    newInstance.t1 = instance.t1
            newInstances.append(newInstance)
        return newInstances
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