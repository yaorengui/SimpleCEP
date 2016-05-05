# -*- coding: utf8 -*-
from gen.cedlLexer import *
from gen.cedlParser import *
from cedl_visitor import *
from cedlPattern import *
from Queue import Queue, Empty
import time
from cedlLimit import *
class eventForest():
    def __init__(self):
        self.outputQueue = Queue()
        self.nodeIndex = {}
        self.id = 0

        pass
    def complexEventDetection(self,forest):
        for tree in forest.members:
            self.postOrderProcess(tree)
            for item in tree.children[0].instances:
                print u'输出实例'
                self.outputQueue.put(item)

    ##1.该算法采用主动检测的方式侦查复杂事件
    ##2.采用后序遍历的方式为非叶子节点生成新的实例
    ##3.任何实例加入事件实例集合前都要检测是否满足约束条件，只有满足约束条件时才加入
    ##4.该算法不对叶子节点进行处理，所以，只有满足约束条件的原子事件的实例才加入其实例集合
    def postOrderProcess(self,node):
        #先访问孩子节点
        for child in node.children:
            self.postOrderProcess(child)

        #访问非叶子节点，生成新的实例
        if (node.op != '-1')&(node.op!=None):#根节点的op为None,叶子节点的op为-1
            op = operator()
            newInstances = op.handler(node)
            if newInstances !=None:
                limit = check()
                for item in newInstances:
                   if limit.checks(node,item):#若满足该节点的约束条件，则加入
                     node.instances.append(item)

    def insertIndex(self,node):
        #process root node
        #print 'dfdfd',node.eTypeId

        for child in node.children:
            self.insertIndex(child)

        if str(node.eTypeId) == 'root':
            node.id = self.id
            self.id+=1
            if self.nodeIndex.has_key(node.eTypeId):
                self.nodeIndex[node.eTypeId].append(node)
            else:
                self.nodeIndex[node.eTypeId]=[node]

            return


        share = self.getSharedNode(node)
        if share == None:
            node.id = self.id
            self.id+=1
            if self.nodeIndex.has_key(node.eTypeId):
                self.nodeIndex[node.eTypeId].append(node)
            else:
                self.nodeIndex[node.eTypeId]=[node]
        else:
            for child in node.children:
                child.father.remove(node)

            father = node.father[0]
            father.children.remove(node)
            father.children.append(share)


    def getSharedNode(self,node):
        if self.nodeIndex.has_key(node.eTypeId):
            nodes = self.nodeIndex[node.eTypeId]
            for item in nodes:
                if self.isSameNode(item,node):
                    flag = True
                    for i in range(len(item.children)):
                        if item.children[i].id != node.children[i].id:
                            flag = False
                            break
                    if flag == True:
                        return item
            return None
        else:
            return None

    #1.检测两个节点，他们的eTypeId 和 attrs是否相同
    def isSameNode(self,node1,node2):
        attach1 = node1.attach
        attach2 = node2.attach
        if node1.childrenId != node2.childrenId:
            return False
        elif node1.op != node2.op:
            return False
        elif node1.timeval != node2.timeval:
            return False
        elif node1.timeunit != node2.timeunit:
            return False
        elif node1.repeatNum != node2.repeatNum:
            return False

        if len(attach1) != len(attach2):
            return False

        for i in range(len(attach1)):
            limit1 = attach1[i].restrictions
            limit2 = attach2[i].restrictions
            if limit1['op'] != limit2['op']:
                return False
            if limit1['event_name'] != limit2['event_name']:
                return False
            if limit1['event_attr'] != limit2['event_attr']:
                return False
            if limit2['value'] != limit2['value']:
                return False

        return True

class eventTree():
    def __init__(self):
        pass
    #将输入转为事件树
    def getEventTree(self,input):
        lexer = cedlLexer(input)#词法分析
        stream = CommonTokenStream(lexer)#单词流
        parser = cedlParser(stream)#语法分析
        visitor = cedl_visitor()
        tree = parser.cedl_event()#获取语法树
        visitor.visit(tree)#以visitor方式访问语法树
        root = visitor.root#获取事件树
        root.attach = visitor.limits#获取限制条件
        root.eventsIndex = visitor.atom_events #获取原子事件的索引表
        root.complexEventID = visitor.complexEventID
        self.assignLimits(root)
        return root
        pass
    def assignLimits(self,root):
        limits = root.attach
        op = operator()
        op.visitLimits(limits)
        for item in limits:
            #print 'gggg',item

            key1 = item.restrictions['event_name']
            v  = item.restrictions['value']

            if type(v)== type({}):
                key2 = v['event_name']
                sameFather = self.getSameFather(root,key1,key2)

                if sameFather == None:
                    continue

                if sameFather.eTypeId == root.eTypeId:
                    continue

                #print "no None"
                sameFather.attach.append(item)

                #root.attach.remove(item)#会出麻烦

            else:
                event = self.lookup(root.eventsIndex,key1)
                if event != None:
                  event.attach.append(item)
                #root.attach.remove(item)

    def lookup(self,index,key):
        if index.has_key(key):
            return index[key]
        else:
            return None

    def getSameFather(self,root,key1,key2):
        index = root.eventsIndex
        if index.has_key(key1):
            e1 = index[key1]
        else:
            print 'no exist e1 key',key1
            return None
        if index.has_key(key2):
            e2 = index[key2]
        else:
            print 'no exist e2 key',key2
            return None
        father = []
        #print e1.eTypeId,root.eTypeId
        #print e1.father

        while e1.eTypeId != root.eTypeId:
            if e1.eTypeId == root.eTypeId:
                break
            e1 = e1.father[0]
            father.append(e1)

        while e2.eTypeId != root.eTypeId:
            e2 = e2.father[0]
            if father.__contains__(e2) == True:
                return e2
        return None

    #向事件树种插入实例
    #向原子节点插入实例
    def insertInstance(self,instance,root):
        eventIndex = root.eventsIndex
        if instance.eTypeId in eventIndex.keys():#也可通过d.has_key('key')判断
            eventNode = eventIndex[instance.eTypeId] #通过事件索引找到要插入的事件节点
            limit = check()
            if limit.checks(eventNode,instance):
                print u'向',eventNode.eTypeId,u'节点插入实例'
                eventNode.instances.append(instance)    #向节点中插入实例
                return eventNode
            else:
                print u'不满足约束条件'
                return None
        else:
            #print u'不存在实例所对应的事件类型'
            return None


def main(argv):
    #节点操作函数
    global seq
    seq = 0
    op = operator()
    input = FileStream(argv)
    event_tree = eventTree()
    root = event_tree.getEventTree(input)
    data = {}
    data['id'] = 'E1'
    data['name'] = 'yao'
    data['password']=123
    instance = eInstance_node(seq,'E1',time.time(),time.time())
    instance.attrs['E1']=data
    seq+=1
    event_tree.insertInstance(instance,root)
    instance = eInstance_node(seq,'E2',time.time(),time.time())
    data = {}
    data['id'] = 'E2'
    data['name'] = 'yang'
    data['password']=123
    instance.attrs['E2']=data
    seq+=1
    event_tree.insertInstance(instance,root)

    forest = forest_node('forest')
    forest.members.append(root)
    #op.visit(root)
    forestOp = eventForest()
    forestOp.complexEventDetection(forest)

    limits = root.attach
    op.visitLimits(limits)





    '''
    atom_events = root.eventsIndex
    for item in atom_events:
            print atom_events[item].eTypeId
    '''

if __name__ == '__main__':
    main('input.txt')


    '''
    #lexer = ExprLexer(input)
    lexer = cedlLexer(input)
    stream = CommonTokenStream(lexer)
    #parser = ExprParser(stream)
    parser = cedlParser(stream)

    #context = parser.ProgContext(parser)
    visitor = cedl_visitor()

    listener = cedl_listener()



    try:
        tree = parser.cedl_event()

        visitor.visit(tree)

        walker = ParseTreeWalker()
        walker.walk(listener,tree)

        option = operator()
        root = visitor.root
        option.visit(root)
        limits = visitor.limits
        option.visitLimits(limits)
        root.attach = limits

        #测试事件索引
        premitive_events = visitor.premitive_events
        for item in premitive_events:
            print premitive_events[item].eTypeId





        #分层变量语法树
        #print "start"
        #op.visit(r)
        #print "end"
        #print r.getChild(0)
    except Empty:
        pass

    #printer = progPrinter()
    #walker=ParseTreeWalker()
    #walker.walk(printer,tree)#printer as listener, tree为被监听对象


    #tree = parser.NEWLINE
   # print parser.NEWLINE
    #print parser.prog
'''
