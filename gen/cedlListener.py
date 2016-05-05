# Generated from C:/Users/fit/PycharmProjects/CEP/src\cedl.g4 by ANTLR 4.5.1
from antlr4 import *

from code.cedl_node import *
from collections import OrderedDict
from Queue import Queue, Empty


# This class defines a complete listener for a parse tree produced by cedlParser.
class cedlListener(ParseTreeListener):

    # Enter a parse tree produced by cedlParser#cedl_events.
    def enterCedl_events(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#cedl_events.
    def exitCedl_events(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#cedl_event.
    def enterCedl_event(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#cedl_event.
    def exitCedl_event(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#select_clause.
    def enterSelect_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#select_clause.
    def exitSelect_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#complex_event.
    def enterComplex_event(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#complex_event.
    def exitComplex_event(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#from_clause.
    def enterFrom_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#from_clause.
    def exitFrom_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#event_list.
    def enterEvent_list(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#event_list.
    def exitEvent_list(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#event.
    def enterEvent(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#event.
    def exitEvent(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#premitive_event.
    def enterPremitive_event(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#premitive_event.
    def exitPremitive_event(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#pattern_clause.
    def enterPattern_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#pattern_clause.
    def exitPattern_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#pattern_operators.
    def enterPattern_operators(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#pattern_operators.
    def exitPattern_operators(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#link_operator.
    def enterLink_operator(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#link_operator.
    def exitLink_operator(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#pattern_event_1.
    def enterPattern_event_1(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#pattern_event_1.
    def exitPattern_event_1(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time.
    def enterTime(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time.
    def exitTime(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time_start.
    def enterTime_start(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time_start.
    def exitTime_start(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time_end.
    def enterTime_end(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time_end.
    def exitTime_end(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#pattern_event_2.
    def enterPattern_event_2(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#pattern_event_2.
    def exitPattern_event_2(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#pattern_event_n.
    def enterPattern_event_n(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#pattern_event_n.
    def exitPattern_event_n(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#limit_clause.
    def enterLimit_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#limit_clause.
    def exitLimit_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#filters.
    def enterFilters(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#filters.
    def exitFilters(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#limit_filter.
    def enterLimit_filter(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#limit_filter.
    def exitLimit_filter(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#filter_operator.
    def enterFilter_operator(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#filter_operator.
    def exitFilter_operator(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#filter_value.
    def enterFilter_value(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#filter_value.
    def exitFilter_value(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time_clause.
    def enterTime_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time_clause.
    def exitTime_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#len_clause.
    def enterLen_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#len_clause.
    def exitLen_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#context_clause.
    def enterContext_clause(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#context_clause.
    def exitContext_clause(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#context_value.
    def enterContext_value(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#context_value.
    def exitContext_value(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#atom_event_name.
    def enterAtom_event_name(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#atom_event_name.
    def exitAtom_event_name(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#complex_event_name.
    def enterComplex_event_name(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#complex_event_name.
    def exitComplex_event_name(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#attr_name.
    def enterAttr_name(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#attr_name.
    def exitAttr_name(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time_value.
    def enterTime_value(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time_value.
    def exitTime_value(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#len_value.
    def enterLen_value(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#len_value.
    def exitLen_value(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#repeat_num.
    def enterRepeat_num(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#repeat_num.
    def exitRepeat_num(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#value_num.
    def enterValue_num(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#value_num.
    def exitValue_num(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#value_numeric.
    def enterValue_numeric(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#value_numeric.
    def exitValue_numeric(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#time_unit.
    def enterTime_unit(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#time_unit.
    def exitTime_unit(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#numeric.
    def enterNumeric(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#numeric.
    def exitNumeric(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#string_key.
    def enterString_key(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#string_key.
    def exitString_key(self, ctx):
        pass


    # Enter a parse tree produced by cedlParser#num_key.
    def enterNum_key(self, ctx):
        pass

    # Exit a parse tree produced by cedlParser#num_key.
    def exitNum_key(self, ctx):
        pass


