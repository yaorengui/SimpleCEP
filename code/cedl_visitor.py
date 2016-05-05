# -*- coding: utf8 -*-
from gen.cedlVisitor import *
class cedl_visitor(cedlVisitor):
    # Visit a parse tree produced by cedlParser#pattern_operator_n.
    def __init__(self):
        self.root = None
        self.limits = None
        self.atom_events = None
        self.complexEventID = None
        pass
      # Visit a parse tree produced by cedlParser#cedl_event.
    def visitCedl_event(self, ctx):
        self.atom_events = ctx.premitive_events
        return self.visitChildren(ctx)
    #获取事件树节点
    def visitPattern_operators(self, ctx):
        self.root=ctx.node
        #print self.root.childrenId
        pass
    #获取限制条件节点
    def visitFilters(self, ctx):
        self.limits = ctx.nodes
        pass

    def visitComplex_event(self, ctx):
        self.complexEventID = ctx.complexEventID

