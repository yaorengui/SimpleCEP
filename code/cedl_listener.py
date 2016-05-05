# -*- coding: utf8 -*-
from gen.cedlListener import *
class cedl_listener(cedlListener):
    def __init__(self):
        self.root=eType_node('root')

        pass
    # Exit a parse tree produced by cedlParser#pattern_operators.
    def exitPattern_operators(self, ctx):

        #print ctx.event().getText()
        #self.root.addChildren(node)
        pass
    # Enter a parse tree produced by cedlParser#premitive_event.
    def enterPremitive_event(self, ctx):
        #print 'enterPremitive'

        pass

    # Exit a parse tree produced by cedlParser#premitive_event.
    def exitPremitive_event(self, ctx):
        #print ctx.node.eTypeId
        pass
    pass