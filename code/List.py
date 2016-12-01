# -*- coding: utf8 -*-
from collections import OrderedDict
class List():
    def __init__(self):
        self.temp = listHead()
        self.head = self.temp
        self.current = self.temp
        self.tail = self.temp
        self.seq = 0

    def getHead(self):
        return self.head
    #insert the value after the node
    def insertAfter(self,node,value):
        new = listNode(value,self.seq)
        self.seq+=1
        temp = node.next
        node.next = new
        new.prev = node
        if temp!=None:
            new.next = temp
            temp.prev = new
        else:
            self.tail=new

    def deleteAfter(self,node):
        temp=node.next
        if temp!=None:
            temp.prev=None
        node.next=None

    def delete(self,node):
        prev = node.prev
        next = node.next
        if next==None:
            prev.next=None
            node.prev=None
        else:
            prev.next = next
            next.prev = prev
            node.prev = None
            node.next = None

class listNode():
    def __init__(self,value,seq):
        self.seq = seq
        self.prev = None
        self.next = None
        self.value = value

class listHead():
    def __init__(self):
        self.next=None