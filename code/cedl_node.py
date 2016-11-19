# -*- coding: utf8 -*-
from collections import OrderedDict
from code.cedlPattern import *
from Queue import Queue, Empty

import time
#设计基准：
##1.系统中可有多个森林，具体依系统而定
##2.森林节点通常有多个事件树
##3.系统中，同一类事件只有一个节点，因此，存在不同事件节点共享一个子节点的情况，也存在多个事件树共享一个事件节点的情况
#森林节点
class forest_node():
    def __init__(self,forestId):

        self.forestId = forestId
        self.members= [] #存放事件类型节点

#事件类型节点
class eType_node():
    def __init__(self,eTypeId,op=None,father=None):
        self.id = None #节点在森林中的唯一编号,森林中，id具有唯一性
        self.context="cumulative"#设置为默认值
        self.childrenId = 0 #孩子结点个数
        self.eTypeId = eTypeId
        self.nodeId = [] #兄弟排行，节点在在父节点中子节点的编号,考虑到存在多个父节点，故采用结合的形式
        self.op = op
        self.children = []#eType_node类型
        self.father = [] #主要针对共享节点
        self.instances = [] #初步将事件实例定义为一次消费型
        self.attach = [] #存储attach_node节点，
        self.eventsIndex = {}#只在根节点中出现
        self.timeval = None #存储时间间隔，用于WITHIN操作
        self.timeunit = None #存储事件单位,用于WITHIN操作
        self.repeatNum = None #用于repeat操作存储重复次数
        self.complexEventID = None #存储复杂事件的名字,唯一的ID号
        self.start = []            #标记实例开始的起始位置
        self.seqt = [] ##针对seq操作 rencent
        self.last = [] ##针对seq操作 cumulativeSeq
        pass

    def toString(self):
        temp = "<strong>id:</strong>"
        temp+=str(self.id)
        temp+="<br>"
        temp+="<strong>context:</strong>"
        temp+=str(self.context)
        temp+="<br>"
        temp+="<strong>childrenId:</strong>"
        temp+=str(self.childrenId)
        temp+="<br>"
        return temp
        pass
    def addChildren(self,node):
        node.nodeId.append(self.childrenId)
        self.childrenId+=1
        self.start.append(0)#initiate the starting position with zero
        if str(self.op).lower() == 'seq':
            self.seqt.append(-1)
            self.last.append(-1)
            #print len(self.seqt),'dddd'

        self.children.append(node)


    def addInstances(self,node):
        self.instances.append(node)

    def getChildrenId(self):
        return self.childrenId

 #每个节点存储一个限制条件,便于增加和删除节点，也便于限制条件下推
class attach_node():
    def __init__(self,attachId=None):
        self.attachId = attachId
        self.restrictions = {}
        self.nodes = []#暂无用处



class eInstance_node():
    def __init__(self,eId,eTypeId,t0=None,t1=None):
        self.eSeq = eId
        self.eId = eId #按时间先后顺序赋值
        self.eTypeId = eTypeId #插入事件时使用 事件ID，如symbol="IF1607",IF1607为eTypeId
        #若为原子事件，则attrs中只包含原始数据，若为非原子事件，则attrs中包含多个原子事件的原始数据
        self.attrs = {}#存储原子事件的数据
        self.t0 = t0
        self.t1= t1
        if t0 == None:self.t0 = 0
        if t1 == None:self.t1 =1


class eIndex():
    def __init__(self):
        self.__eType_dict = OrderedDict()

        #node类型为事件类型
    def put(self,eTypeId,node):
        self.__eType_dict[eTypeId]=node

    def get(self,eTypeId):
        try:
            return self.__eType_dict[eTypeId]
        except:
            return 0

    #节点测试
def main():
    node_id = 0
    e_id = 0
    attach_id =0

    option = operator()

    index=eIndex()

    #根节点1
    root1 = eType_node(node_id) #根节点
    index.put(node_id,root1) #便于索引
    node_id+=1

    #事件节点
    op="SEQ"
    father = root1
    node = eType_node(node_id,op, father)
    index.put(node_id,node)
    node_id+=1

    root1.addChildren(node)

    option.visit(root1)

    #根节点2
    root2 = eType_node(node_id)
    index.put(node_id,root2) #便于索引
    node_id+=1

    index_node = index.get(1)
    if index_node == 0:
        print "该节点不存在！"
    else:
        root2.addChildren(index_node)


    #事件实例测试
    ins = eInstance_node(e_id, 1)
    e_id+=1
    attr = {}
    attr['name']="yaorengui"
    attr['password']="123456"
    attr['id']= 12
    ins.attrs[attr['id']] = attr
    ins.t0 = 12
    ins.t1 = 15
    index_node.instances.append(ins)

    #事件约束测试
    attach = attach_node(attach_id)
    attach_id+=1

    con = {}
    con['op']='>'
    con['arg1']="price"
    con['arg2']=15
    root2.attach.append(con)
    #可继续添加...

    option.visit(root2)
    pass
def global_test():
    global dic
    dic = {}
    dic['name']='yaorengui'
    print dic['name']
    pass
if __name__ == '__main__':
   main()
   #global_test()
   pass

##测试日志
#1.共享节点测试。不同事件树共享同一个事件节点时，检测修改共享节点引起的变化
#2.事件实例测试
#3.事件约束测试
