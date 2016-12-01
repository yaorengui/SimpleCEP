# Generated from E:/CEP/src\cedl.g4 by ANTLR 4.5.3
from antlr4 import *

from code.cedl_node import *
from collections import OrderedDict
from Queue import Queue, Empty


# This class defines a complete generic visitor for a parse tree produced by cedlParser.

class cedlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cedlParser#cedl_events.
    def visitCedl_events(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#cedl_event.
    def visitCedl_event(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#select_clause.
    def visitSelect_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#complex_event.
    def visitComplex_event(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#from_clause.
    def visitFrom_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#event_list.
    def visitEvent_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#event.
    def visitEvent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#premitive_event.
    def visitPremitive_event(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#pattern_clause.
    def visitPattern_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#pattern_operators.
    def visitPattern_operators(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#link_operator.
    def visitLink_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#pattern_event_1.
    def visitPattern_event_1(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time.
    def visitTime(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time_start.
    def visitTime_start(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time_end.
    def visitTime_end(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#pattern_event_2.
    def visitPattern_event_2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#pattern_event_n.
    def visitPattern_event_n(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#limit_clause.
    def visitLimit_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#filters.
    def visitFilters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#limit_filter.
    def visitLimit_filter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#filter_operator.
    def visitFilter_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#filter_value.
    def visitFilter_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time_clause.
    def visitTime_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#len_clause.
    def visitLen_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#context_clause.
    def visitContext_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#context_value.
    def visitContext_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#atom_event_name.
    def visitAtom_event_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#complex_event_name.
    def visitComplex_event_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#attr_name.
    def visitAttr_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time_value.
    def visitTime_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#len_value.
    def visitLen_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#repeat_num.
    def visitRepeat_num(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#value_num.
    def visitValue_num(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#value_numeric.
    def visitValue_numeric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#time_unit.
    def visitTime_unit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#numeric.
    def visitNumeric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#string_key.
    def visitString_key(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cedlParser#num_key.
    def visitNum_key(self, ctx):
        return self.visitChildren(ctx)


