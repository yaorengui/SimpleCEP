# -*- coding: utf8 -*-
class check():
    def __init__(self):
        self.op = {}
        self.op['<'] = self.LT
        self.op['<='] = self.LT_EQ
        self.op['>'] = self.GT
        self.op['>='] = self.GT_EQ
        self.op['='] = self.EQ
        self.op['!='] = self.NOT_EQ1
        self.op['<>'] = self.NOT_EQ2
        self.op['contains'] = self.CONTAINS
        self.op['equals'] = self.EQUALS
        self.op['compareto'] = self.COMPARETO
        self.op['matches'] = self.MATCHES

    def checks(self,node,instance):
        limits = node.attach
        for item in limits:
            symbol =  item.restrictions['op']
            event_name =  item.restrictions['event_name']
            attr_name =  item.restrictions['event_attr']
            value =  item.restrictions['value']

            if instance.attrs.has_key(event_name) == False:
                #print 'no exist  attr',event_name
                return False
            if instance.attrs[event_name].has_key(attr_name) == False:
                #print 'no exist attr:',attr_name
                return False
            v1 = instance.attrs[event_name][attr_name]
            if type(value) == type({}):
                if instance.attrs.has_key(value['event_name']) == False:
                    print 'no exist key1',value['event_name']
                    return False
                if instance.attrs[value['event_name']].has_key(value['event_attr']) == False:
                    print 'no exist key2',value['event_attr']
                    return False

                v2 = instance.attrs[value['event_name']][value['event_attr']]
            else:
                v2 = value
            if self.check(symbol,v1,v2) == False:
                return False
        return True


    def check(self,symbol,v1,v2):

        v2 = type(v1)(v2) #先转换为类型相同，再比较
        #print 'symbol;',symbol
        return self.op[symbol](v1,v2)


    def LT(self,v1,v2):
        if v1 < v2:
            return True
        else:
            return False
    def LT_EQ(self,v1,v2):
        if v1 <= v2:
            return True
        else:
            return False
    def GT(self,v1,v2):
        if v1 > v2:
            return True
        else:
            return False
    def GT_EQ(self,v1,v2):
        if v1 >= v2:
            return True
        else:
            return False

    def EQ(self,v1,v2):
        #print 'dd',v1,int(v2)
        if v1 == v2:
            return True
        else:
            return False
    def NOT_EQ1(self,v1,v2):
        if v1!=v2:
            return True
        else:
            return False
    def NOT_EQ2(self,v1,v2):
        if(v1!=v2):
            return True
        else:
            return False

    def CONTAINS(self,v1,v2):
        v1 = str(v1)
        v2 = str(v2)
        if v1.__contains__(v2):
            return True
        else:
            return False

    def EQUALS(self,v1,v2):
        v1 = str(v1)
        v2 = str(v2)
        if v1 == v2:
            return True
        else:
          return True

    def COMPARETO(self,v1,v2):
        v1 = str(v1)
        v2 = str(v2)
        return True

    def MATCHES(self,v1,v2):
        v1 = str(v1)
        v2 = str(v2)
        return True