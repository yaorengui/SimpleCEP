# Generated from E:/CEP/src\cedl.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from code.cedl_node import *
from collections import OrderedDict
from Queue import Queue, Empty

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"T\u01e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\3\2\6\2P\n\2\r\2\16\2Q\3\3\3")
        buf.write(u"\3\3\3\3\3\5\3X\n\3\3\3\3\3\5\3\\\n\3\3\3\5\3_\n\3\3")
        buf.write(u"\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\7\7r\n\7\f\7\16\7u\13\7\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0083\n\b\3\t")
        buf.write(u"\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\5\13\u0094\n\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\5\13\u00a0\n\13\7\13\u00a2")
        buf.write(u"\n\13\f\13\16\13\u00a5\13\13\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c4\n")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u012b")
        buf.write(u"\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\5\21\u0145\n\21\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\24\7\24\u0156\n\24\f\24\16\24\u0159\13\24\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u018f\n")
        buf.write(u"\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\5\27\u01a7\n\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write(u"\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u01bc\n\33\3\34\3\34\5\34\u01c0\n")
        buf.write(u"\34\3\35\3\35\5\35\u01c4\n\35\3\36\3\36\5\36\u01c8\n")
        buf.write(u"\36\3\37\3\37\5\37\u01cc\n\37\3 \3 \5 \u01d0\n \3!\3")
        buf.write(u"!\5!\u01d4\n!\3\"\3\"\3#\3#\5#\u01da\n#\3$\3$\3%\3%\3")
        buf.write(u"&\3&\3\'\3\'\3\'\2\2(\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL\2\b\3\2\6\7\4")
        buf.write(u"\2FFHH\7\2\31\32\35\36  \"\"$$\4\2\66;??\4\2\4\21\31")
        buf.write(u"+\3\2.\63\u01eb\2O\3\2\2\2\4S\3\2\2\2\6b\3\2\2\2\be\3")
        buf.write(u"\2\2\2\nh\3\2\2\2\fk\3\2\2\2\16\u0082\3\2\2\2\20\u0084")
        buf.write(u"\3\2\2\2\22\u0087\3\2\2\2\24\u0093\3\2\2\2\26\u00a6\3")
        buf.write(u"\2\2\2\30\u012a\3\2\2\2\32\u012c\3\2\2\2\34\u012e\3\2")
        buf.write(u"\2\2\36\u0130\3\2\2\2 \u0144\3\2\2\2\"\u0146\3\2\2\2")
        buf.write(u"$\u014c\3\2\2\2&\u014f\3\2\2\2(\u018e\3\2\2\2*\u0190")
        buf.write(u"\3\2\2\2,\u01a6\3\2\2\2.\u01a8\3\2\2\2\60\u01ac\3\2\2")
        buf.write(u"\2\62\u01af\3\2\2\2\64\u01bb\3\2\2\2\66\u01bf\3\2\2\2")
        buf.write(u"8\u01c3\3\2\2\2:\u01c7\3\2\2\2<\u01cb\3\2\2\2>\u01cf")
        buf.write(u"\3\2\2\2@\u01d3\3\2\2\2B\u01d5\3\2\2\2D\u01d9\3\2\2\2")
        buf.write(u"F\u01db\3\2\2\2H\u01dd\3\2\2\2J\u01df\3\2\2\2L\u01e1")
        buf.write(u"\3\2\2\2NP\5\4\3\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3")
        buf.write(u"\2\2\2R\3\3\2\2\2ST\5\6\4\2TU\5\n\6\2UW\5\22\n\2VX\5")
        buf.write(u"$\23\2WV\3\2\2\2WX\3\2\2\2X[\3\2\2\2Y\\\5.\30\2Z\\\5")
        buf.write(u"\60\31\2[Y\3\2\2\2[Z\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]_")
        buf.write(u"\5\62\32\2^]\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\b\3\1\2a\5")
        buf.write(u"\3\2\2\2bc\t\2\2\2cd\5\b\5\2d\7\3\2\2\2ef\58\35\2fg\b")
        buf.write(u"\5\1\2g\t\3\2\2\2hi\7\b\2\2ij\5\f\7\2j\13\3\2\2\2kl\5")
        buf.write(u"\16\b\2ls\b\7\1\2mn\7M\2\2no\5\16\b\2op\b\7\1\2pr\3\2")
        buf.write(u"\2\2qm\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\r\3\2\2")
        buf.write(u"\2us\3\2\2\2vw\5\20\t\2wx\b\b\1\2x\u0083\3\2\2\2yz\5")
        buf.write(u"\30\r\2z{\b\b\1\2{\u0083\3\2\2\2|}\5\"\22\2}~\b\b\1\2")
        buf.write(u"~\u0083\3\2\2\2\177\u0080\5 \21\2\u0080\u0081\b\b\1\2")
        buf.write(u"\u0081\u0083\3\2\2\2\u0082v\3\2\2\2\u0082y\3\2\2\2\u0082")
        buf.write(u"|\3\2\2\2\u0082\177\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085")
        buf.write(u"\5\66\34\2\u0085\u0086\b\t\1\2\u0086\21\3\2\2\2\u0087")
        buf.write(u"\u0088\7\t\2\2\u0088\u0089\5\24\13\2\u0089\23\3\2\2\2")
        buf.write(u"\u008a\u008b\5\30\r\2\u008b\u008c\b\13\1\2\u008c\u0094")
        buf.write(u"\3\2\2\2\u008d\u008e\5 \21\2\u008e\u008f\b\13\1\2\u008f")
        buf.write(u"\u0094\3\2\2\2\u0090\u0091\5\"\22\2\u0091\u0092\b\13")
        buf.write(u"\1\2\u0092\u0094\3\2\2\2\u0093\u008a\3\2\2\2\u0093\u008d")
        buf.write(u"\3\2\2\2\u0093\u0090\3\2\2\2\u0094\u00a3\3\2\2\2\u0095")
        buf.write(u"\u009f\5\26\f\2\u0096\u0097\5\30\r\2\u0097\u0098\b\13")
        buf.write(u"\1\2\u0098\u00a0\3\2\2\2\u0099\u009a\5 \21\2\u009a\u009b")
        buf.write(u"\b\13\1\2\u009b\u00a0\3\2\2\2\u009c\u009d\5\"\22\2\u009d")
        buf.write(u"\u009e\b\13\1\2\u009e\u00a0\3\2\2\2\u009f\u0096\3\2\2")
        buf.write(u"\2\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\u00a2")
        buf.write(u"\3\2\2\2\u00a1\u0095\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write(u"\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\25\3\2\2\2\u00a5")
        buf.write(u"\u00a3\3\2\2\2\u00a6\u00a7\t\3\2\2\u00a7\27\3\2\2\2\u00a8")
        buf.write(u"\u00a9\7\33\2\2\u00a9\u00aa\7I\2\2\u00aa\u00ab\5\16\b")
        buf.write(u"\2\u00ab\u00ac\7J\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae")
        buf.write(u"\b\r\1\2\u00ae\u012b\3\2\2\2\u00af\u00b0\7\37\2\2\u00b0")
        buf.write(u"\u00b1\7I\2\2\u00b1\u00b2\5\16\b\2\u00b2\u00b3\7M\2\2")
        buf.write(u"\u00b3\u00b4\5@!\2\u00b4\u00b5\7J\2\2\u00b5\u00b6\3\2")
        buf.write(u"\2\2\u00b6\u00b7\b\r\1\2\u00b7\u012b\3\2\2\2\u00b8\u00b9")
        buf.write(u"\7!\2\2\u00b9\u00ba\7I\2\2\u00ba\u00bb\5\16\b\2\u00bb")
        buf.write(u"\u00c3\7M\2\2\u00bc\u00bd\5<\37\2\u00bd\u00be\5F$\2\u00be")
        buf.write(u"\u00c4\3\2\2\2\u00bf\u00c0\5\34\17\2\u00c0\u00c1\7M\2")
        buf.write(u"\2\u00c1\u00c2\5\36\20\2\u00c2\u00c4\3\2\2\2\u00c3\u00bc")
        buf.write(u"\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write(u"\u00c6\7J\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\b\r\1\2")
        buf.write(u"\u00c8\u012b\3\2\2\2\u00c9\u00ca\7%\2\2\u00ca\u00cb\7")
        buf.write(u"I\2\2\u00cb\u00cc\5\16\b\2\u00cc\u00cd\7M\2\2\u00cd\u00ce")
        buf.write(u"\5<\37\2\u00ce\u00cf\5F$\2\u00cf\u00d0\7J\2\2\u00d0\u00d1")
        buf.write(u"\3\2\2\2\u00d1\u00d2\b\r\1\2\u00d2\u012b\3\2\2\2\u00d3")
        buf.write(u"\u00d4\7&\2\2\u00d4\u00d5\7I\2\2\u00d5\u00d6\5\16\b\2")
        buf.write(u"\u00d6\u00d7\7M\2\2\u00d7\u00d8\5\32\16\2\u00d8\u00d9")
        buf.write(u"\7J\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\b\r\1\2\u00db")
        buf.write(u"\u012b\3\2\2\2\u00dc\u00dd\7\22\2\2\u00dd\u00de\7I\2")
        buf.write(u"\2\u00de\u00df\5\16\b\2\u00df\u00e0\7M\2\2\u00e0\u00e1")
        buf.write(u"\5> \2\u00e1\u00e2\7M\2\2\u00e2\u00e3\5:\36\2\u00e3\u00e4")
        buf.write(u"\7M\2\2\u00e4\u00e5\5:\36\2\u00e5\u00e6\7J\2\2\u00e6")
        buf.write(u"\u00e7\3\2\2\2\u00e7\u00e8\b\r\1\2\u00e8\u012b\3\2\2")
        buf.write(u"\2\u00e9\u00ea\7\23\2\2\u00ea\u00eb\7I\2\2\u00eb\u00ec")
        buf.write(u"\5\16\b\2\u00ec\u00ed\7M\2\2\u00ed\u00ee\5> \2\u00ee")
        buf.write(u"\u00ef\7M\2\2\u00ef\u00f0\5:\36\2\u00f0\u00f1\7M\2\2")
        buf.write(u"\u00f1\u00f2\5:\36\2\u00f2\u00f3\7J\2\2\u00f3\u00f4\3")
        buf.write(u"\2\2\2\u00f4\u00f5\b\r\1\2\u00f5\u012b\3\2\2\2\u00f6")
        buf.write(u"\u00f7\7\24\2\2\u00f7\u00f8\7I\2\2\u00f8\u00f9\5\16\b")
        buf.write(u"\2\u00f9\u00fa\7M\2\2\u00fa\u00fb\5> \2\u00fb\u00fc\7")
        buf.write(u"M\2\2\u00fc\u00fd\5:\36\2\u00fd\u00fe\7M\2\2\u00fe\u00ff")
        buf.write(u"\5:\36\2\u00ff\u0100\7J\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write(u"\u0102\b\r\1\2\u0102\u012b\3\2\2\2\u0103\u0104\7\25\2")
        buf.write(u"\2\u0104\u0105\7I\2\2\u0105\u0106\5\16\b\2\u0106\u0107")
        buf.write(u"\7M\2\2\u0107\u0108\5> \2\u0108\u0109\7M\2\2\u0109\u010a")
        buf.write(u"\5:\36\2\u010a\u010b\7M\2\2\u010b\u010c\5:\36\2\u010c")
        buf.write(u"\u010d\7J\2\2\u010d\u010e\3\2\2\2\u010e\u010f\b\r\1\2")
        buf.write(u"\u010f\u012b\3\2\2\2\u0110\u0111\7\27\2\2\u0111\u0112")
        buf.write(u"\7I\2\2\u0112\u0113\5\16\b\2\u0113\u0114\7M\2\2\u0114")
        buf.write(u"\u0115\5> \2\u0115\u0116\7M\2\2\u0116\u0117\5:\36\2\u0117")
        buf.write(u"\u0118\7M\2\2\u0118\u0119\5:\36\2\u0119\u011a\7J\2\2")
        buf.write(u"\u011a\u011b\3\2\2\2\u011b\u011c\b\r\1\2\u011c\u012b")
        buf.write(u"\3\2\2\2\u011d\u011e\7\30\2\2\u011e\u011f\7I\2\2\u011f")
        buf.write(u"\u0120\5\16\b\2\u0120\u0121\7M\2\2\u0121\u0122\5> \2")
        buf.write(u"\u0122\u0123\7M\2\2\u0123\u0124\5:\36\2\u0124\u0125\7")
        buf.write(u"M\2\2\u0125\u0126\5:\36\2\u0126\u0127\7J\2\2\u0127\u0128")
        buf.write(u"\3\2\2\2\u0128\u0129\b\r\1\2\u0129\u012b\3\2\2\2\u012a")
        buf.write(u"\u00a8\3\2\2\2\u012a\u00af\3\2\2\2\u012a\u00b8\3\2\2")
        buf.write(u"\2\u012a\u00c9\3\2\2\2\u012a\u00d3\3\2\2\2\u012a\u00dc")
        buf.write(u"\3\2\2\2\u012a\u00e9\3\2\2\2\u012a\u00f6\3\2\2\2\u012a")
        buf.write(u"\u0103\3\2\2\2\u012a\u0110\3\2\2\2\u012a\u011d\3\2\2")
        buf.write(u"\2\u012b\31\3\2\2\2\u012c\u012d\7-\2\2\u012d\33\3\2\2")
        buf.write(u"\2\u012e\u012f\5\32\16\2\u012f\35\3\2\2\2\u0130\u0131")
        buf.write(u"\5\32\16\2\u0131\37\3\2\2\2\u0132\u0133\7\34\2\2\u0133")
        buf.write(u"\u0134\7I\2\2\u0134\u0135\5\16\b\2\u0135\u0136\7M\2\2")
        buf.write(u"\u0136\u0137\5\16\b\2\u0137\u0138\7J\2\2\u0138\u0139")
        buf.write(u"\3\2\2\2\u0139\u013a\b\21\1\2\u013a\u0145\3\2\2\2\u013b")
        buf.write(u"\u013c\7#\2\2\u013c\u013d\7I\2\2\u013d\u013e\5\16\b\2")
        buf.write(u"\u013e\u013f\7M\2\2\u013f\u0140\5\16\b\2\u0140\u0141")
        buf.write(u"\7J\2\2\u0141\u0142\3\2\2\2\u0142\u0143\b\21\1\2\u0143")
        buf.write(u"\u0145\3\2\2\2\u0144\u0132\3\2\2\2\u0144\u013b\3\2\2")
        buf.write(u"\2\u0145!\3\2\2\2\u0146\u0147\t\4\2\2\u0147\u0148\7I")
        buf.write(u"\2\2\u0148\u0149\5\f\7\2\u0149\u014a\7J\2\2\u014a\u014b")
        buf.write(u"\b\22\1\2\u014b#\3\2\2\2\u014c\u014d\7\n\2\2\u014d\u014e")
        buf.write(u"\5&\24\2\u014e%\3\2\2\2\u014f\u0150\5(\25\2\u0150\u0157")
        buf.write(u"\b\24\1\2\u0151\u0152\7\31\2\2\u0152\u0153\5(\25\2\u0153")
        buf.write(u"\u0154\b\24\1\2\u0154\u0156\3\2\2\2\u0155\u0151\3\2\2")
        buf.write(u"\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158")
        buf.write(u"\3\2\2\2\u0158\'\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b")
        buf.write(u"\5\20\t\2\u015b\u015c\7O\2\2\u015c\u015d\5:\36\2\u015d")
        buf.write(u"\u015e\5*\26\2\u015e\u015f\5,\27\2\u015f\u0160\3\2\2")
        buf.write(u"\2\u0160\u0161\b\25\1\2\u0161\u018f\3\2\2\2\u0162\u0163")
        buf.write(u"\5\20\t\2\u0163\u0164\7O\2\2\u0164\u0165\5:\36\2\u0165")
        buf.write(u"\u0166\7O\2\2\u0166\u0167\7\'\2\2\u0167\u0168\7I\2\2")
        buf.write(u"\u0168\u0169\7R\2\2\u0169\u016a\7J\2\2\u016a\u016b\3")
        buf.write(u"\2\2\2\u016b\u016c\b\25\1\2\u016c\u018f\3\2\2\2\u016d")
        buf.write(u"\u016e\5\20\t\2\u016e\u016f\7O\2\2\u016f\u0170\5:\36")
        buf.write(u"\2\u0170\u0171\7O\2\2\u0171\u0172\7)\2\2\u0172\u0173")
        buf.write(u"\7I\2\2\u0173\u0174\7R\2\2\u0174\u0175\7J\2\2\u0175\u0176")
        buf.write(u"\3\2\2\2\u0176\u0177\b\25\1\2\u0177\u018f\3\2\2\2\u0178")
        buf.write(u"\u0179\5\20\t\2\u0179\u017a\7O\2\2\u017a\u017b\5:\36")
        buf.write(u"\2\u017b\u017c\7O\2\2\u017c\u017d\7(\2\2\u017d\u017e")
        buf.write(u"\7I\2\2\u017e\u017f\7R\2\2\u017f\u0180\7J\2\2\u0180\u0181")
        buf.write(u"\3\2\2\2\u0181\u0182\b\25\1\2\u0182\u018f\3\2\2\2\u0183")
        buf.write(u"\u0184\5\20\t\2\u0184\u0185\7O\2\2\u0185\u0186\5:\36")
        buf.write(u"\2\u0186\u0187\7O\2\2\u0187\u0188\7*\2\2\u0188\u0189")
        buf.write(u"\7I\2\2\u0189\u018a\7R\2\2\u018a\u018b\7J\2\2\u018b\u018c")
        buf.write(u"\3\2\2\2\u018c\u018d\b\25\1\2\u018d\u018f\3\2\2\2\u018e")
        buf.write(u"\u015a\3\2\2\2\u018e\u0162\3\2\2\2\u018e\u016d\3\2\2")
        buf.write(u"\2\u018e\u0178\3\2\2\2\u018e\u0183\3\2\2\2\u018f)\3\2")
        buf.write(u"\2\2\u0190\u0191\t\5\2\2\u0191\u0192\b\26\1\2\u0192+")
        buf.write(u"\3\2\2\2\u0193\u0194\7\4\2\2\u0194\u01a7\b\27\1\2\u0195")
        buf.write(u"\u0196\7\5\2\2\u0196\u01a7\b\27\1\2\u0197\u0198\7Q\2")
        buf.write(u"\2\u0198\u0199\5\20\t\2\u0199\u019a\7O\2\2\u019a\u019b")
        buf.write(u"\5:\36\2\u019b\u019c\3\2\2\2\u019c\u019d\b\27\1\2\u019d")
        buf.write(u"\u01a7\3\2\2\2\u019e\u019f\5B\"\2\u019f\u01a0\b\27\1")
        buf.write(u"\2\u01a0\u01a7\3\2\2\2\u01a1\u01a2\5D#\2\u01a2\u01a3")
        buf.write(u"\b\27\1\2\u01a3\u01a7\3\2\2\2\u01a4\u01a5\7R\2\2\u01a5")
        buf.write(u"\u01a7\b\27\1\2\u01a6\u0193\3\2\2\2\u01a6\u0195\3\2\2")
        buf.write(u"\2\u01a6\u0197\3\2\2\2\u01a6\u019e\3\2\2\2\u01a6\u01a1")
        buf.write(u"\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7-\3\2\2\2\u01a8\u01a9")
        buf.write(u"\7\13\2\2\u01a9\u01aa\5<\37\2\u01aa\u01ab\5F$\2\u01ab")
        buf.write(u"/\3\2\2\2\u01ac\u01ad\7\f\2\2\u01ad\u01ae\5> \2\u01ae")
        buf.write(u"\61\3\2\2\2\u01af\u01b0\7\r\2\2\u01b0\u01b1\5\64\33\2")
        buf.write(u"\u01b1\u01b2\b\32\1\2\u01b2\63\3\2\2\2\u01b3\u01b4\7")
        buf.write(u"\16\2\2\u01b4\u01bc\b\33\1\2\u01b5\u01b6\7\17\2\2\u01b6")
        buf.write(u"\u01bc\b\33\1\2\u01b7\u01b8\7\20\2\2\u01b8\u01bc\b\33")
        buf.write(u"\1\2\u01b9\u01ba\7\21\2\2\u01ba\u01bc\b\33\1\2\u01bb")
        buf.write(u"\u01b3\3\2\2\2\u01bb\u01b5\3\2\2\2\u01bb\u01b7\3\2\2")
        buf.write(u"\2\u01bb\u01b9\3\2\2\2\u01bc\65\3\2\2\2\u01bd\u01c0\7")
        buf.write(u",\2\2\u01be\u01c0\5J&\2\u01bf\u01bd\3\2\2\2\u01bf\u01be")
        buf.write(u"\3\2\2\2\u01c0\67\3\2\2\2\u01c1\u01c4\7,\2\2\u01c2\u01c4")
        buf.write(u"\5J&\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write(u"9\3\2\2\2\u01c5\u01c8\7,\2\2\u01c6\u01c8\5J&\2\u01c7")
        buf.write(u"\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8;\3\2\2\2\u01c9")
        buf.write(u"\u01cc\7\64\2\2\u01ca\u01cc\5L\'\2\u01cb\u01c9\3\2\2")
        buf.write(u"\2\u01cb\u01ca\3\2\2\2\u01cc=\3\2\2\2\u01cd\u01d0\7\64")
        buf.write(u"\2\2\u01ce\u01d0\5L\'\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce")
        buf.write(u"\3\2\2\2\u01d0?\3\2\2\2\u01d1\u01d4\5<\37\2\u01d2\u01d4")
        buf.write(u"\5> \2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write(u"A\3\2\2\2\u01d5\u01d6\5@!\2\u01d6C\3\2\2\2\u01d7\u01da")
        buf.write(u"\7\65\2\2\u01d8\u01da\5B\"\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write(u"\u01d8\3\2\2\2\u01daE\3\2\2\2\u01db\u01dc\7+\2\2\u01dc")
        buf.write(u"G\3\2\2\2\u01dd\u01de\7\65\2\2\u01deI\3\2\2\2\u01df\u01e0")
        buf.write(u"\t\6\2\2\u01e0K\3\2\2\2\u01e1\u01e2\t\7\2\2\u01e2M\3")
        buf.write(u"\2\2\2\31QW[^s\u0082\u0093\u009f\u00a3\u00c3\u012a\u0144")
        buf.write(u"\u0157\u018e\u01a6\u01bb\u01bf\u01c3\u01c7\u01cb\u01cf")
        buf.write(u"\u01d3\u01d9")
        return buf.getvalue()


class cedlParser ( Parser ):

    grammarFileName = "cedl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'<'", u"'<='", u"'>'", u"'>='", u"'='", u"'!='", 
                     u"'<<'", u"'>>'", u"'=='", u"'<>'", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'%'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"'('", u"')'", u"'{'", u"'}'", u"','", u"';'", u"'.'", 
                     u"'~'", u"'$'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"TRUE", u"FALSE", u"SELECT", 
                      u"DEFINE", u"FROM", u"PATTERN", u"LIMIT", u"TIMEWINDOW", 
                      u"LENWINDOW", u"CONTEXT", u"CHRONICLE", u"RECENT", 
                      u"CONTINUOUS", u"CUMULATIVE", u"AVG", u"SUM", u"MINOP", 
                      u"MAX", u"COUNT", u"DEC", u"INC", u"AND", u"OR", u"NOT", 
                      u"XOR", u"NAND", u"NOR", u"REPEAT", u"SEQ", u"WITHIN", 
                      u"FOLLOWBY", u"DURING", u"EQUAL", u"INTERVAL", u"AT", 
                      u"CONTAINS", u"COMPARETO", u"EQUALS", u"MATCHES", 
                      u"TIME_UNIT", u"IDENTIFLER", u"TIME_COMPLETE", u"YEAR", 
                      u"MON", u"DAY", u"HOUR", u"MIN", u"SEC", u"INT", u"NUMERIC", 
                      u"LT", u"LT_EQ", u"GT", u"GT_EQ", u"EQ", u"NOT_EQ1", 
                      u"LT2", u"GT2", u"EQ2", u"NOT_EQ2", u"PLUS", u"MINUS", 
                      u"STAR", u"DIV", u"MOD", u"AMP", u"AMP2", u"PIPE", 
                      u"PIPE2", u"OPEN_PAR", u"CLOSE_PAR", u"OPEN_CURLY", 
                      u"CLOSE_CURLY", u"COMMA", u"SCOL", u"DOT", u"TILDE", 
                      u"DOLLAR", u"STRING", u"SINGLE_LINE_COMMENT", u"MULTI_LINE_COMMENT" ]

    RULE_cedl_events = 0
    RULE_cedl_event = 1
    RULE_select_clause = 2
    RULE_complex_event = 3
    RULE_from_clause = 4
    RULE_event_list = 5
    RULE_event = 6
    RULE_premitive_event = 7
    RULE_pattern_clause = 8
    RULE_pattern_operators = 9
    RULE_link_operator = 10
    RULE_pattern_event_1 = 11
    RULE_time = 12
    RULE_time_start = 13
    RULE_time_end = 14
    RULE_pattern_event_2 = 15
    RULE_pattern_event_n = 16
    RULE_limit_clause = 17
    RULE_filters = 18
    RULE_limit_filter = 19
    RULE_filter_operator = 20
    RULE_filter_value = 21
    RULE_time_clause = 22
    RULE_len_clause = 23
    RULE_context_clause = 24
    RULE_context_value = 25
    RULE_atom_event_name = 26
    RULE_complex_event_name = 27
    RULE_attr_name = 28
    RULE_time_value = 29
    RULE_len_value = 30
    RULE_repeat_num = 31
    RULE_value_num = 32
    RULE_value_numeric = 33
    RULE_time_unit = 34
    RULE_numeric = 35
    RULE_string_key = 36
    RULE_num_key = 37

    ruleNames =  [ u"cedl_events", u"cedl_event", u"select_clause", u"complex_event", 
                   u"from_clause", u"event_list", u"event", u"premitive_event", 
                   u"pattern_clause", u"pattern_operators", u"link_operator", 
                   u"pattern_event_1", u"time", u"time_start", u"time_end", 
                   u"pattern_event_2", u"pattern_event_n", u"limit_clause", 
                   u"filters", u"limit_filter", u"filter_operator", u"filter_value", 
                   u"time_clause", u"len_clause", u"context_clause", u"context_value", 
                   u"atom_event_name", u"complex_event_name", u"attr_name", 
                   u"time_value", u"len_value", u"repeat_num", u"value_num", 
                   u"value_numeric", u"time_unit", u"numeric", u"string_key", 
                   u"num_key" ]

    EOF = Token.EOF
    WS=1
    TRUE=2
    FALSE=3
    SELECT=4
    DEFINE=5
    FROM=6
    PATTERN=7
    LIMIT=8
    TIMEWINDOW=9
    LENWINDOW=10
    CONTEXT=11
    CHRONICLE=12
    RECENT=13
    CONTINUOUS=14
    CUMULATIVE=15
    AVG=16
    SUM=17
    MINOP=18
    MAX=19
    COUNT=20
    DEC=21
    INC=22
    AND=23
    OR=24
    NOT=25
    XOR=26
    NAND=27
    NOR=28
    REPEAT=29
    SEQ=30
    WITHIN=31
    FOLLOWBY=32
    DURING=33
    EQUAL=34
    INTERVAL=35
    AT=36
    CONTAINS=37
    COMPARETO=38
    EQUALS=39
    MATCHES=40
    TIME_UNIT=41
    IDENTIFLER=42
    TIME_COMPLETE=43
    YEAR=44
    MON=45
    DAY=46
    HOUR=47
    MIN=48
    SEC=49
    INT=50
    NUMERIC=51
    LT=52
    LT_EQ=53
    GT=54
    GT_EQ=55
    EQ=56
    NOT_EQ1=57
    LT2=58
    GT2=59
    EQ2=60
    NOT_EQ2=61
    PLUS=62
    MINUS=63
    STAR=64
    DIV=65
    MOD=66
    AMP=67
    AMP2=68
    PIPE=69
    PIPE2=70
    OPEN_PAR=71
    CLOSE_PAR=72
    OPEN_CURLY=73
    CLOSE_CURLY=74
    COMMA=75
    SCOL=76
    DOT=77
    TILDE=78
    DOLLAR=79
    STRING=80
    SINGLE_LINE_COMMENT=81
    MULTI_LINE_COMMENT=82

    def __init__(self, input):
        super(cedlParser, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    #存储原始事件
    global premitive_events
    premitive_events = {}


    class Cedl_eventsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Cedl_eventsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def cedl_event(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Cedl_eventContext)
            else:
                return self.getTypedRuleContext(cedlParser.Cedl_eventContext,i)


        def getRuleIndex(self):
            return cedlParser.RULE_cedl_events

        def enterRule(self, listener):
            if hasattr(listener, "enterCedl_events"):
                listener.enterCedl_events(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCedl_events"):
                listener.exitCedl_events(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCedl_events"):
                return visitor.visitCedl_events(self)
            else:
                return visitor.visitChildren(self)




    def cedl_events(self):

        localctx = cedlParser.Cedl_eventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cedl_events)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.cedl_event()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cedlParser.SELECT or _la==cedlParser.DEFINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cedl_eventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Cedl_eventContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.premitive_events = None
            self.a = None # Context_clauseContext

        def select_clause(self):
            return self.getTypedRuleContext(cedlParser.Select_clauseContext,0)


        def from_clause(self):
            return self.getTypedRuleContext(cedlParser.From_clauseContext,0)


        def pattern_clause(self):
            return self.getTypedRuleContext(cedlParser.Pattern_clauseContext,0)


        def limit_clause(self):
            return self.getTypedRuleContext(cedlParser.Limit_clauseContext,0)


        def time_clause(self):
            return self.getTypedRuleContext(cedlParser.Time_clauseContext,0)


        def len_clause(self):
            return self.getTypedRuleContext(cedlParser.Len_clauseContext,0)


        def context_clause(self):
            return self.getTypedRuleContext(cedlParser.Context_clauseContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_cedl_event

        def enterRule(self, listener):
            if hasattr(listener, "enterCedl_event"):
                listener.enterCedl_event(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCedl_event"):
                listener.exitCedl_event(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCedl_event"):
                return visitor.visitCedl_event(self)
            else:
                return visitor.visitChildren(self)




    def cedl_event(self):

        localctx = cedlParser.Cedl_eventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cedl_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.select_clause()
            self.state = 82
            self.from_clause()
            self.state = 83
            self.pattern_clause()
            self.state = 85
            _la = self._input.LA(1)
            if _la==cedlParser.LIMIT:
                self.state = 84
                self.limit_clause()


            self.state = 89
            token = self._input.LA(1)
            if token in [cedlParser.TIMEWINDOW]:
                self.state = 87
                self.time_clause()
                pass
            elif token in [cedlParser.LENWINDOW]:
                self.state = 88
                self.len_clause()
                pass
            elif token in [cedlParser.EOF, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.CONTEXT]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 92
            _la = self._input.LA(1)
            if _la==cedlParser.CONTEXT:
                self.state = 91
                localctx.a = self.context_clause()



            localctx.premitive_events = premitive_events

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Select_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def complex_event(self):
            return self.getTypedRuleContext(cedlParser.Complex_eventContext,0)


        def SELECT(self):
            return self.getToken(cedlParser.SELECT, 0)

        def DEFINE(self):
            return self.getToken(cedlParser.DEFINE, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_select_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterSelect_clause"):
                listener.enterSelect_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelect_clause"):
                listener.exitSelect_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSelect_clause"):
                return visitor.visitSelect_clause(self)
            else:
                return visitor.visitChildren(self)




    def select_clause(self):

        localctx = cedlParser.Select_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_select_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==cedlParser.SELECT or _la==cedlParser.DEFINE):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 97
            self.complex_event()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Complex_eventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Complex_eventContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.complexEventID = None
            self.a = None # Complex_event_nameContext

        def complex_event_name(self):
            return self.getTypedRuleContext(cedlParser.Complex_event_nameContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_complex_event

        def enterRule(self, listener):
            if hasattr(listener, "enterComplex_event"):
                listener.enterComplex_event(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComplex_event"):
                listener.exitComplex_event(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitComplex_event"):
                return visitor.visitComplex_event(self)
            else:
                return visitor.visitChildren(self)




    def complex_event(self):

        localctx = cedlParser.Complex_eventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complex_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            localctx.a = self.complex_event_name()
            localctx.complexEventID = (None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class From_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.From_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(cedlParser.FROM, 0)

        def event_list(self):
            return self.getTypedRuleContext(cedlParser.Event_listContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_from_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterFrom_clause"):
                listener.enterFrom_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFrom_clause"):
                listener.exitFrom_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFrom_clause"):
                return visitor.visitFrom_clause(self)
            else:
                return visitor.visitChildren(self)




    def from_clause(self):

        localctx = cedlParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(cedlParser.FROM)
            self.state = 103
            self.event_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Event_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Event_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self.a = None # EventContext
            self.b = None # EventContext

        def event(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.EventContext)
            else:
                return self.getTypedRuleContext(cedlParser.EventContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(cedlParser.COMMA)
            else:
                return self.getToken(cedlParser.COMMA, i)

        def getRuleIndex(self):
            return cedlParser.RULE_event_list

        def enterRule(self, listener):
            if hasattr(listener, "enterEvent_list"):
                listener.enterEvent_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEvent_list"):
                listener.exitEvent_list(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitEvent_list"):
                return visitor.visitEvent_list(self)
            else:
                return visitor.visitChildren(self)




    def event_list(self):

        localctx = cedlParser.Event_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_event_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            localctx.a = self.event()

            localctx.nodes = []
            localctx.nodes.append(localctx.a.node)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cedlParser.COMMA:
                self.state = 107
                self.match(cedlParser.COMMA)
                self.state = 108
                localctx.b = self.event()

                localctx.nodes.append(localctx.b.node)

                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.EventContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # Premitive_eventContext

        def premitive_event(self):
            return self.getTypedRuleContext(cedlParser.Premitive_eventContext,0)


        def pattern_event_1(self):
            return self.getTypedRuleContext(cedlParser.Pattern_event_1Context,0)


        def pattern_event_n(self):
            return self.getTypedRuleContext(cedlParser.Pattern_event_nContext,0)


        def pattern_event_2(self):
            return self.getTypedRuleContext(cedlParser.Pattern_event_2Context,0)


        def getRuleIndex(self):
            return cedlParser.RULE_event

        def enterRule(self, listener):
            if hasattr(listener, "enterEvent"):
                listener.enterEvent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEvent"):
                listener.exitEvent(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitEvent"):
                return visitor.visitEvent(self)
            else:
                return visitor.visitChildren(self)




    def event(self):

        localctx = cedlParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_event)
        try:
            self.state = 128
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                localctx.a = self.premitive_event()

                localctx.node = localctx.a.node
                premitive_events[(None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop)))] = localctx.node

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx.a = self.pattern_event_1()
                localctx.node = localctx.a.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                localctx.a = self.pattern_event_n()
                localctx.node = localctx.a.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                localctx.a = self.pattern_event_2()
                localctx.node = localctx.a.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Premitive_eventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Premitive_eventContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.event_id = None # Atom_event_nameContext

        def atom_event_name(self):
            return self.getTypedRuleContext(cedlParser.Atom_event_nameContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_premitive_event

        def enterRule(self, listener):
            if hasattr(listener, "enterPremitive_event"):
                listener.enterPremitive_event(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPremitive_event"):
                listener.exitPremitive_event(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPremitive_event"):
                return visitor.visitPremitive_event(self)
            else:
                return visitor.visitChildren(self)




    def premitive_event(self):

        localctx = cedlParser.Premitive_eventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_premitive_event)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx.event_id = self.atom_event_name()
            localctx.node = eType_node((None if localctx.event_id is None else self._input.getText((localctx.event_id.start,localctx.event_id.stop))),'-1')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Pattern_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PATTERN(self):
            return self.getToken(cedlParser.PATTERN, 0)

        def pattern_operators(self):
            return self.getTypedRuleContext(cedlParser.Pattern_operatorsContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_pattern_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterPattern_clause"):
                listener.enterPattern_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPattern_clause"):
                listener.exitPattern_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_clause"):
                return visitor.visitPattern_clause(self)
            else:
                return visitor.visitChildren(self)




    def pattern_clause(self):

        localctx = cedlParser.Pattern_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pattern_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(cedlParser.PATTERN)
            self.state = 134
            self.pattern_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Pattern_operatorsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # Pattern_event_1Context

        def pattern_event_1(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Pattern_event_1Context)
            else:
                return self.getTypedRuleContext(cedlParser.Pattern_event_1Context,i)


        def pattern_event_2(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Pattern_event_2Context)
            else:
                return self.getTypedRuleContext(cedlParser.Pattern_event_2Context,i)


        def pattern_event_n(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Pattern_event_nContext)
            else:
                return self.getTypedRuleContext(cedlParser.Pattern_event_nContext,i)


        def link_operator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Link_operatorContext)
            else:
                return self.getTypedRuleContext(cedlParser.Link_operatorContext,i)


        def getRuleIndex(self):
            return cedlParser.RULE_pattern_operators

        def enterRule(self, listener):
            if hasattr(listener, "enterPattern_operators"):
                listener.enterPattern_operators(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPattern_operators"):
                listener.exitPattern_operators(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_operators"):
                return visitor.visitPattern_operators(self)
            else:
                return visitor.visitChildren(self)




    def pattern_operators(self):

        localctx = cedlParser.Pattern_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pattern_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            token = self._input.LA(1)
            if token in [cedlParser.AVG, cedlParser.SUM, cedlParser.MINOP, cedlParser.MAX, cedlParser.DEC, cedlParser.INC, cedlParser.NOT, cedlParser.REPEAT, cedlParser.WITHIN, cedlParser.INTERVAL, cedlParser.AT]:
                self.state = 136
                localctx.a = self.pattern_event_1()

                localctx.node = eType_node("root","root")
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)#便于查询两个原子事件的最近共同祖�?


            elif token in [cedlParser.XOR, cedlParser.DURING]:
                self.state = 139
                localctx.a = self.pattern_event_2()

                localctx.node = eType_node("root","root")
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            elif token in [cedlParser.AND, cedlParser.OR, cedlParser.NAND, cedlParser.NOR, cedlParser.SEQ, cedlParser.FOLLOWBY, cedlParser.EQUAL]:
                self.state = 142
                localctx.a = self.pattern_event_n()

                localctx.node = eType_node("root","root")
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            else:
                raise NoViableAltException(self)

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cedlParser.AMP2 or _la==cedlParser.PIPE2:
                self.state = 147
                self.link_operator()
                self.state = 157
                token = self._input.LA(1)
                if token in [cedlParser.AVG, cedlParser.SUM, cedlParser.MINOP, cedlParser.MAX, cedlParser.DEC, cedlParser.INC, cedlParser.NOT, cedlParser.REPEAT, cedlParser.WITHIN, cedlParser.INTERVAL, cedlParser.AT]:
                    self.state = 148
                    localctx.a = self.pattern_event_1()

                    localctx.node.addChildren(localctx.a.node)
                    localctx.a.node.father.append(localctx.node)


                elif token in [cedlParser.XOR, cedlParser.DURING]:
                    self.state = 151
                    localctx.a = self.pattern_event_2()

                    localctx.node.addChildren(localctx.a.node)
                    localctx.a.node.father.append(localctx.node)


                elif token in [cedlParser.AND, cedlParser.OR, cedlParser.NAND, cedlParser.NOR, cedlParser.SEQ, cedlParser.FOLLOWBY, cedlParser.EQUAL]:
                    self.state = 154
                    localctx.a = self.pattern_event_n()

                    localctx.node.addChildren(localctx.a.node)
                    localctx.a.node.father.append(localctx.node)


                else:
                    raise NoViableAltException(self)

                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Link_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Link_operatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def AMP2(self):
            return self.getToken(cedlParser.AMP2, 0)

        def PIPE2(self):
            return self.getToken(cedlParser.PIPE2, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_link_operator

        def enterRule(self, listener):
            if hasattr(listener, "enterLink_operator"):
                listener.enterLink_operator(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLink_operator"):
                listener.exitLink_operator(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLink_operator"):
                return visitor.visitLink_operator(self)
            else:
                return visitor.visitChildren(self)




    def link_operator(self):

        localctx = cedlParser.Link_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_link_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==cedlParser.AMP2 or _la==cedlParser.PIPE2):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_event_1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Pattern_event_1Context, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # EventContext
            self.b = None # Repeat_numContext
            self.c = None # Time_unitContext
            self.d = None # Attr_nameContext

        def NOT(self):
            return self.getToken(cedlParser.NOT, 0)

        def OPEN_PAR(self):
            return self.getToken(cedlParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(cedlParser.CLOSE_PAR, 0)

        def event(self):
            return self.getTypedRuleContext(cedlParser.EventContext,0)


        def REPEAT(self):
            return self.getToken(cedlParser.REPEAT, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(cedlParser.COMMA)
            else:
                return self.getToken(cedlParser.COMMA, i)

        def repeat_num(self):
            return self.getTypedRuleContext(cedlParser.Repeat_numContext,0)


        def WITHIN(self):
            return self.getToken(cedlParser.WITHIN, 0)

        def time_start(self):
            return self.getTypedRuleContext(cedlParser.Time_startContext,0)


        def time_end(self):
            return self.getTypedRuleContext(cedlParser.Time_endContext,0)


        def time_value(self):
            return self.getTypedRuleContext(cedlParser.Time_valueContext,0)


        def time_unit(self):
            return self.getTypedRuleContext(cedlParser.Time_unitContext,0)


        def INTERVAL(self):
            return self.getToken(cedlParser.INTERVAL, 0)

        def AT(self):
            return self.getToken(cedlParser.AT, 0)

        def time(self):
            return self.getTypedRuleContext(cedlParser.TimeContext,0)


        def AVG(self):
            return self.getToken(cedlParser.AVG, 0)

        def len_value(self):
            return self.getTypedRuleContext(cedlParser.Len_valueContext,0)


        def attr_name(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Attr_nameContext)
            else:
                return self.getTypedRuleContext(cedlParser.Attr_nameContext,i)


        def SUM(self):
            return self.getToken(cedlParser.SUM, 0)

        def MINOP(self):
            return self.getToken(cedlParser.MINOP, 0)

        def MAX(self):
            return self.getToken(cedlParser.MAX, 0)

        def DEC(self):
            return self.getToken(cedlParser.DEC, 0)

        def INC(self):
            return self.getToken(cedlParser.INC, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_pattern_event_1

        def enterRule(self, listener):
            if hasattr(listener, "enterPattern_event_1"):
                listener.enterPattern_event_1(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPattern_event_1"):
                listener.exitPattern_event_1(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_event_1"):
                return visitor.visitPattern_event_1(self)
            else:
                return visitor.visitChildren(self)




    def pattern_event_1(self):

        localctx = cedlParser.Pattern_event_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pattern_event_1)
        try:
            self.state = 296
            token = self._input.LA(1)
            if token in [cedlParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(cedlParser.NOT)
                self.state = 167
                self.match(cedlParser.OPEN_PAR)
                self.state = 168
                localctx.a = self.event()
                self.state = 169
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('not','not')
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            elif token in [cedlParser.REPEAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(cedlParser.REPEAT)
                self.state = 174
                self.match(cedlParser.OPEN_PAR)
                self.state = 175
                localctx.a = self.event()
                self.state = 176
                self.match(cedlParser.COMMA)
                self.state = 177
                localctx.b = self.repeat_num()
                self.state = 178
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('repeat','repeat')
                localctx.node.repeatNum = (None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            elif token in [cedlParser.WITHIN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(cedlParser.WITHIN)
                self.state = 183
                self.match(cedlParser.OPEN_PAR)
                self.state = 184
                localctx.a = self.event()
                self.state = 185
                self.match(cedlParser.COMMA)
                self.state = 193
                token = self._input.LA(1)
                if token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC, cedlParser.INT]:
                    self.state = 186
                    localctx.b = self.time_value()
                    self.state = 187
                    localctx.c = self.time_unit()

                elif token in [cedlParser.TIME_COMPLETE]:
                    self.state = 189
                    self.time_start()
                    self.state = 190
                    self.match(cedlParser.COMMA)
                    self.state = 191
                    self.time_end()

                else:
                    raise NoViableAltException(self)

                self.state = 195
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('within','within')
                localctx.node.timeval = (None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))
                localctx.node.timeunit = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))

                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)
                 

            elif token in [cedlParser.INTERVAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.match(cedlParser.INTERVAL)
                self.state = 200
                self.match(cedlParser.OPEN_PAR)
                self.state = 201
                localctx.a = self.event()
                self.state = 202
                self.match(cedlParser.COMMA)
                self.state = 203
                localctx.b = self.time_value()
                self.state = 204
                localctx.c = self.time_unit()
                self.state = 205
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('interval','interval')
                localctx.node.timeval = (None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))
                localctx.node.timeunit = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))

                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            elif token in [cedlParser.AT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(cedlParser.AT)
                self.state = 210
                self.match(cedlParser.OPEN_PAR)
                self.state = 211
                localctx.a = self.event()
                self.state = 212
                self.match(cedlParser.COMMA)
                self.state = 213
                self.time()
                self.state = 214
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('at','at')
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)


            elif token in [cedlParser.AVG]:
                self.enterOuterAlt(localctx, 6)
                self.state = 218
                self.match(cedlParser.AVG)
                self.state = 219
                self.match(cedlParser.OPEN_PAR)
                self.state = 220
                localctx.a = self.event()
                self.state = 221
                self.match(cedlParser.COMMA)
                self.state = 222
                localctx.b = self.len_value()
                self.state = 223
                self.match(cedlParser.COMMA)
                self.state = 224
                localctx.c = self.attr_name()
                self.state = 225
                self.match(cedlParser.COMMA)
                self.state = 226
                localctx.d = self.attr_name()
                self.state = 227
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'avg',str((None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))),str((None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            elif token in [cedlParser.SUM]:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.match(cedlParser.SUM)
                self.state = 232
                self.match(cedlParser.OPEN_PAR)
                self.state = 233
                localctx.a = self.event()
                self.state = 234
                self.match(cedlParser.COMMA)
                self.state = 235
                localctx.b = self.len_value()
                self.state = 236
                self.match(cedlParser.COMMA)
                self.state = 237
                localctx.c = self.attr_name()
                self.state = 238
                self.match(cedlParser.COMMA)
                self.state = 239
                localctx.d = self.attr_name()
                self.state = 240
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'sum',(None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop))),(None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            elif token in [cedlParser.MINOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 244
                self.match(cedlParser.MINOP)
                self.state = 245
                self.match(cedlParser.OPEN_PAR)
                self.state = 246
                localctx.a = self.event()
                self.state = 247
                self.match(cedlParser.COMMA)
                self.state = 248
                localctx.b = self.len_value()
                self.state = 249
                self.match(cedlParser.COMMA)
                self.state = 250
                localctx.c = self.attr_name()
                self.state = 251
                self.match(cedlParser.COMMA)
                self.state = 252
                localctx.d = self.attr_name()
                self.state = 253
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'min',(None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop))),(None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            elif token in [cedlParser.MAX]:
                self.enterOuterAlt(localctx, 9)
                self.state = 257
                self.match(cedlParser.MAX)
                self.state = 258
                self.match(cedlParser.OPEN_PAR)
                self.state = 259
                localctx.a = self.event()
                self.state = 260
                self.match(cedlParser.COMMA)
                self.state = 261
                localctx.b = self.len_value()
                self.state = 262
                self.match(cedlParser.COMMA)
                self.state = 263
                localctx.c = self.attr_name()
                self.state = 264
                self.match(cedlParser.COMMA)
                self.state = 265
                localctx.d = self.attr_name()
                self.state = 266
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'max',(None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop))),(None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            elif token in [cedlParser.DEC]:
                self.enterOuterAlt(localctx, 10)
                self.state = 270
                self.match(cedlParser.DEC)
                self.state = 271
                self.match(cedlParser.OPEN_PAR)
                self.state = 272
                localctx.a = self.event()
                self.state = 273
                self.match(cedlParser.COMMA)
                self.state = 274
                localctx.b = self.len_value()
                self.state = 275
                self.match(cedlParser.COMMA)
                self.state = 276
                localctx.c = self.attr_name()
                self.state = 277
                self.match(cedlParser.COMMA)
                self.state = 278
                localctx.d = self.attr_name()
                self.state = 279
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'dec',(None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop))),(None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            elif token in [cedlParser.INC]:
                self.enterOuterAlt(localctx, 11)
                self.state = 283
                self.match(cedlParser.INC)
                self.state = 284
                self.match(cedlParser.OPEN_PAR)
                self.state = 285
                localctx.a = self.event()
                self.state = 286
                self.match(cedlParser.COMMA)
                self.state = 287
                localctx.b = self.len_value()
                self.state = 288
                self.match(cedlParser.COMMA)
                self.state = 289
                localctx.c = self.attr_name()
                self.state = 290
                self.match(cedlParser.COMMA)
                self.state = 291
                localctx.d = self.attr_name()
                self.state = 292
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = aggregationNode(str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))),'inc',(None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop))),(None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop))),str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop)))))
                localctx.node.addChildren(localctx.a.node)
                localctx.a.node.father.append(localctx.node)

                premitive_events[str((None if localctx.d is None else self._input.getText((localctx.d.start,localctx.d.stop))))] = localctx.node


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.TimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIME_COMPLETE(self):
            return self.getToken(cedlParser.TIME_COMPLETE, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_time

        def enterRule(self, listener):
            if hasattr(listener, "enterTime"):
                listener.enterTime(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime"):
                listener.exitTime(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime"):
                return visitor.visitTime(self)
            else:
                return visitor.visitChildren(self)




    def time(self):

        localctx = cedlParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(cedlParser.TIME_COMPLETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Time_startContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Time_startContext, self).__init__(parent, invokingState)
            self.parser = parser

        def time(self):
            return self.getTypedRuleContext(cedlParser.TimeContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_time_start

        def enterRule(self, listener):
            if hasattr(listener, "enterTime_start"):
                listener.enterTime_start(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime_start"):
                listener.exitTime_start(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_start"):
                return visitor.visitTime_start(self)
            else:
                return visitor.visitChildren(self)




    def time_start(self):

        localctx = cedlParser.Time_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_time_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.time()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Time_endContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Time_endContext, self).__init__(parent, invokingState)
            self.parser = parser

        def time(self):
            return self.getTypedRuleContext(cedlParser.TimeContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_time_end

        def enterRule(self, listener):
            if hasattr(listener, "enterTime_end"):
                listener.enterTime_end(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime_end"):
                listener.exitTime_end(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_end"):
                return visitor.visitTime_end(self)
            else:
                return visitor.visitChildren(self)




    def time_end(self):

        localctx = cedlParser.Time_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_time_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.time()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_event_2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Pattern_event_2Context, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # EventContext
            self.b = None # EventContext

        def XOR(self):
            return self.getToken(cedlParser.XOR, 0)

        def OPEN_PAR(self):
            return self.getToken(cedlParser.OPEN_PAR, 0)

        def COMMA(self):
            return self.getToken(cedlParser.COMMA, 0)

        def CLOSE_PAR(self):
            return self.getToken(cedlParser.CLOSE_PAR, 0)

        def event(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.EventContext)
            else:
                return self.getTypedRuleContext(cedlParser.EventContext,i)


        def DURING(self):
            return self.getToken(cedlParser.DURING, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_pattern_event_2

        def enterRule(self, listener):
            if hasattr(listener, "enterPattern_event_2"):
                listener.enterPattern_event_2(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPattern_event_2"):
                listener.exitPattern_event_2(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_event_2"):
                return visitor.visitPattern_event_2(self)
            else:
                return visitor.visitChildren(self)




    def pattern_event_2(self):

        localctx = cedlParser.Pattern_event_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pattern_event_2)
        try:
            self.state = 322
            token = self._input.LA(1)
            if token in [cedlParser.XOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(cedlParser.XOR)
                self.state = 305
                self.match(cedlParser.OPEN_PAR)
                self.state = 306
                localctx.a = self.event()
                self.state = 307
                self.match(cedlParser.COMMA)
                self.state = 308
                localctx.b = self.event()
                self.state = 309
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('xor','xor')
                localctx.node.addChildren(localctx.a.node)
                localctx.node.addChildren(localctx.b.node)
                localctx.a.node.father.append(localctx.node)
                localctx.b.node.father.append(localctx.node)


            elif token in [cedlParser.DURING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(cedlParser.DURING)
                self.state = 314
                self.match(cedlParser.OPEN_PAR)
                self.state = 315
                localctx.a = self.event()
                self.state = 316
                self.match(cedlParser.COMMA)
                self.state = 317
                localctx.b = self.event()
                self.state = 318
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('during','during')
                localctx.node.addChildren(localctx.a.node)
                localctx.node.addChildren(localctx.b.node)
                localctx.a.node.father.append(localctx.node)
                localctx.b.node.father.append(localctx.node)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_event_nContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Pattern_event_nContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # Token
            self.b = None # Event_listContext

        def OPEN_PAR(self):
            return self.getToken(cedlParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(cedlParser.CLOSE_PAR, 0)

        def event_list(self):
            return self.getTypedRuleContext(cedlParser.Event_listContext,0)


        def AND(self):
            return self.getToken(cedlParser.AND, 0)

        def OR(self):
            return self.getToken(cedlParser.OR, 0)

        def NAND(self):
            return self.getToken(cedlParser.NAND, 0)

        def NOR(self):
            return self.getToken(cedlParser.NOR, 0)

        def SEQ(self):
            return self.getToken(cedlParser.SEQ, 0)

        def FOLLOWBY(self):
            return self.getToken(cedlParser.FOLLOWBY, 0)

        def EQUAL(self):
            return self.getToken(cedlParser.EQUAL, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_pattern_event_n

        def enterRule(self, listener):
            if hasattr(listener, "enterPattern_event_n"):
                listener.enterPattern_event_n(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPattern_event_n"):
                listener.exitPattern_event_n(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_event_n"):
                return visitor.visitPattern_event_n(self)
            else:
                return visitor.visitChildren(self)




    def pattern_event_n(self):

        localctx = cedlParser.Pattern_event_nContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pattern_event_n)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            localctx.a = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.AND) | (1 << cedlParser.OR) | (1 << cedlParser.NAND) | (1 << cedlParser.NOR) | (1 << cedlParser.SEQ) | (1 << cedlParser.FOLLOWBY) | (1 << cedlParser.EQUAL))) != 0)):
                localctx.a = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 325
            self.match(cedlParser.OPEN_PAR)
            self.state = 326
            localctx.b = self.event_list()
            self.state = 327
            self.match(cedlParser.CLOSE_PAR)

            localctx.node = eType_node((None if localctx.a is None else localctx.a.text),(None if localctx.a is None else localctx.a.text))
            for item in localctx.b.nodes:
              localctx.node.addChildren(item)
              item.father.append(localctx.node)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Limit_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Limit_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(cedlParser.LIMIT, 0)

        def filters(self):
            return self.getTypedRuleContext(cedlParser.FiltersContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_limit_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterLimit_clause"):
                listener.enterLimit_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLimit_clause"):
                listener.exitLimit_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLimit_clause"):
                return visitor.visitLimit_clause(self)
            else:
                return visitor.visitChildren(self)




    def limit_clause(self):

        localctx = cedlParser.Limit_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_limit_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(cedlParser.LIMIT)
            self.state = 331
            self.filters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FiltersContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.FiltersContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self.a = None # Limit_filterContext

        def limit_filter(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(cedlParser.Limit_filterContext)
            else:
                return self.getTypedRuleContext(cedlParser.Limit_filterContext,i)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(cedlParser.AND)
            else:
                return self.getToken(cedlParser.AND, i)

        def getRuleIndex(self):
            return cedlParser.RULE_filters

        def enterRule(self, listener):
            if hasattr(listener, "enterFilters"):
                listener.enterFilters(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilters"):
                listener.exitFilters(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFilters"):
                return visitor.visitFilters(self)
            else:
                return visitor.visitChildren(self)




    def filters(self):

        localctx = cedlParser.FiltersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            localctx.a = self.limit_filter()

            i=0
            localctx.nodes=[]
            node = attach_node(i)
            node.restrictions = localctx.a.dic
            localctx.nodes.append(node)
            i+=1

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cedlParser.AND:
                self.state = 335
                self.match(cedlParser.AND)
                self.state = 336
                localctx.a = self.limit_filter()

                node = attach_node(i)
                node.restrictions = localctx.a.dic
                localctx.nodes.append(node)
                i+=1

                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Limit_filterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Limit_filterContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.dic = None
            self.e = None # Premitive_eventContext
            self.attr = None # Attr_nameContext
            self.op = None # Filter_operatorContext
            self.v = None # Filter_valueContext
            self.fun = None # Token
            self.v_str = None # Token

        def DOT(self, i=None):
            if i is None:
                return self.getTokens(cedlParser.DOT)
            else:
                return self.getToken(cedlParser.DOT, i)

        def premitive_event(self):
            return self.getTypedRuleContext(cedlParser.Premitive_eventContext,0)


        def attr_name(self):
            return self.getTypedRuleContext(cedlParser.Attr_nameContext,0)


        def filter_operator(self):
            return self.getTypedRuleContext(cedlParser.Filter_operatorContext,0)


        def filter_value(self):
            return self.getTypedRuleContext(cedlParser.Filter_valueContext,0)


        def OPEN_PAR(self):
            return self.getToken(cedlParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(cedlParser.CLOSE_PAR, 0)

        def CONTAINS(self):
            return self.getToken(cedlParser.CONTAINS, 0)

        def STRING(self):
            return self.getToken(cedlParser.STRING, 0)

        def EQUALS(self):
            return self.getToken(cedlParser.EQUALS, 0)

        def COMPARETO(self):
            return self.getToken(cedlParser.COMPARETO, 0)

        def MATCHES(self):
            return self.getToken(cedlParser.MATCHES, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_limit_filter

        def enterRule(self, listener):
            if hasattr(listener, "enterLimit_filter"):
                listener.enterLimit_filter(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLimit_filter"):
                listener.exitLimit_filter(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLimit_filter"):
                return visitor.visitLimit_filter(self)
            else:
                return visitor.visitChildren(self)




    def limit_filter(self):

        localctx = cedlParser.Limit_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_limit_filter)
        try:
            self.state = 396
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                localctx.e = self.premitive_event()
                self.state = 345
                self.match(cedlParser.DOT)
                self.state = 346
                localctx.attr = self.attr_name()
                self.state = 347
                localctx.op = self.filter_operator()
                self.state = 348
                localctx.v = self.filter_value()

                localctx.dic = {}
                localctx.dic['op']= str(localctx.op.op)
                localctx.dic['event_name']=str((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))))
                localctx.dic['event_attr']=str((None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop))))
                localctx.dic['value']=localctx.v.v

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                localctx.e = self.premitive_event()
                self.state = 353
                self.match(cedlParser.DOT)
                self.state = 354
                localctx.attr = self.attr_name()
                self.state = 355
                self.match(cedlParser.DOT)
                self.state = 356
                localctx.fun = self.match(cedlParser.CONTAINS)
                self.state = 357
                self.match(cedlParser.OPEN_PAR)
                self.state = 358
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 359
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                localctx.e = self.premitive_event()
                self.state = 364
                self.match(cedlParser.DOT)
                self.state = 365
                localctx.attr = self.attr_name()
                self.state = 366
                self.match(cedlParser.DOT)
                self.state = 367
                localctx.fun = self.match(cedlParser.EQUALS)
                self.state = 368
                self.match(cedlParser.OPEN_PAR)
                self.state = 369
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 370
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                localctx.e = self.premitive_event()
                self.state = 375
                self.match(cedlParser.DOT)
                self.state = 376
                localctx.attr = self.attr_name()
                self.state = 377
                self.match(cedlParser.DOT)
                self.state = 378
                localctx.fun = self.match(cedlParser.COMPARETO)
                self.state = 379
                self.match(cedlParser.OPEN_PAR)
                self.state = 380
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 381
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 385
                localctx.e = self.premitive_event()
                self.state = 386
                self.match(cedlParser.DOT)
                self.state = 387
                localctx.attr = self.attr_name()
                self.state = 388
                self.match(cedlParser.DOT)
                self.state = 389
                localctx.fun = self.match(cedlParser.MATCHES)
                self.state = 390
                self.match(cedlParser.OPEN_PAR)
                self.state = 391
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 392
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filter_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Filter_operatorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None
            self.a = None # Token

        def EQ(self):
            return self.getToken(cedlParser.EQ, 0)

        def GT(self):
            return self.getToken(cedlParser.GT, 0)

        def GT_EQ(self):
            return self.getToken(cedlParser.GT_EQ, 0)

        def LT(self):
            return self.getToken(cedlParser.LT, 0)

        def LT_EQ(self):
            return self.getToken(cedlParser.LT_EQ, 0)

        def NOT_EQ1(self):
            return self.getToken(cedlParser.NOT_EQ1, 0)

        def NOT_EQ2(self):
            return self.getToken(cedlParser.NOT_EQ2, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_filter_operator

        def enterRule(self, listener):
            if hasattr(listener, "enterFilter_operator"):
                listener.enterFilter_operator(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilter_operator"):
                listener.exitFilter_operator(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFilter_operator"):
                return visitor.visitFilter_operator(self)
            else:
                return visitor.visitChildren(self)




    def filter_operator(self):

        localctx = cedlParser.Filter_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_filter_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            localctx.a = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.LT) | (1 << cedlParser.LT_EQ) | (1 << cedlParser.GT) | (1 << cedlParser.GT_EQ) | (1 << cedlParser.EQ) | (1 << cedlParser.NOT_EQ1) | (1 << cedlParser.NOT_EQ2))) != 0)):
                localctx.a = self._errHandler.recoverInline(self)
            else:
                self.consume()
            localctx.op = (None if localctx.a is None else localctx.a.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filter_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Filter_valueContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.a = None # Premitive_eventContext
            self.b = None # Attr_nameContext
            self.c = None # Value_numContext
            self.d = None # Token

        def TRUE(self):
            return self.getToken(cedlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(cedlParser.FALSE, 0)

        def DOLLAR(self):
            return self.getToken(cedlParser.DOLLAR, 0)

        def DOT(self):
            return self.getToken(cedlParser.DOT, 0)

        def premitive_event(self):
            return self.getTypedRuleContext(cedlParser.Premitive_eventContext,0)


        def attr_name(self):
            return self.getTypedRuleContext(cedlParser.Attr_nameContext,0)


        def value_num(self):
            return self.getTypedRuleContext(cedlParser.Value_numContext,0)


        def value_numeric(self):
            return self.getTypedRuleContext(cedlParser.Value_numericContext,0)


        def STRING(self):
            return self.getToken(cedlParser.STRING, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_filter_value

        def enterRule(self, listener):
            if hasattr(listener, "enterFilter_value"):
                listener.enterFilter_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilter_value"):
                listener.exitFilter_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFilter_value"):
                return visitor.visitFilter_value(self)
            else:
                return visitor.visitChildren(self)




    def filter_value(self):

        localctx = cedlParser.Filter_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_filter_value)
        try:
            self.state = 420
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(cedlParser.TRUE)
                localctx.v = True
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.match(cedlParser.FALSE)
                localctx.v = False
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.match(cedlParser.DOLLAR)
                self.state = 406
                localctx.a = self.premitive_event()
                self.state = 407
                self.match(cedlParser.DOT)
                self.state = 408
                localctx.b = self.attr_name()

                localctx.v = {}
                localctx.v['event_name'] = (None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop)))
                localctx.v['event_attr'] = (None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                localctx.c = self.value_num()
                localctx.v = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 415
                localctx.c = self.value_numeric()
                localctx.v = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 418
                localctx.d = self.match(cedlParser.STRING)
                localctx.v = str((None if localctx.d is None else localctx.d.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Time_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Time_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMEWINDOW(self):
            return self.getToken(cedlParser.TIMEWINDOW, 0)

        def time_value(self):
            return self.getTypedRuleContext(cedlParser.Time_valueContext,0)


        def time_unit(self):
            return self.getTypedRuleContext(cedlParser.Time_unitContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_time_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterTime_clause"):
                listener.enterTime_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime_clause"):
                listener.exitTime_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_clause"):
                return visitor.visitTime_clause(self)
            else:
                return visitor.visitChildren(self)




    def time_clause(self):

        localctx = cedlParser.Time_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_time_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(cedlParser.TIMEWINDOW)
            self.state = 423
            self.time_value()
            self.state = 424
            self.time_unit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Len_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Len_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LENWINDOW(self):
            return self.getToken(cedlParser.LENWINDOW, 0)

        def len_value(self):
            return self.getTypedRuleContext(cedlParser.Len_valueContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_len_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterLen_clause"):
                listener.enterLen_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLen_clause"):
                listener.exitLen_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLen_clause"):
                return visitor.visitLen_clause(self)
            else:
                return visitor.visitChildren(self)




    def len_clause(self):

        localctx = cedlParser.Len_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_len_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(cedlParser.LENWINDOW)
            self.state = 427
            self.len_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Context_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Context_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.context = None
            self.a = None # Context_valueContext

        def CONTEXT(self):
            return self.getToken(cedlParser.CONTEXT, 0)

        def context_value(self):
            return self.getTypedRuleContext(cedlParser.Context_valueContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_context_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterContext_clause"):
                listener.enterContext_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContext_clause"):
                listener.exitContext_clause(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitContext_clause"):
                return visitor.visitContext_clause(self)
            else:
                return visitor.visitChildren(self)




    def context_clause(self):

        localctx = cedlParser.Context_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_context_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(cedlParser.CONTEXT)
            self.state = 430
            localctx.a = self.context_value()
            localctx.context=(None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Context_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Context_valueContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.contextValue = None

        def CHRONICLE(self):
            return self.getToken(cedlParser.CHRONICLE, 0)

        def RECENT(self):
            return self.getToken(cedlParser.RECENT, 0)

        def CONTINUOUS(self):
            return self.getToken(cedlParser.CONTINUOUS, 0)

        def CUMULATIVE(self):
            return self.getToken(cedlParser.CUMULATIVE, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_context_value

        def enterRule(self, listener):
            if hasattr(listener, "enterContext_value"):
                listener.enterContext_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContext_value"):
                listener.exitContext_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitContext_value"):
                return visitor.visitContext_value(self)
            else:
                return visitor.visitChildren(self)




    def context_value(self):

        localctx = cedlParser.Context_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_context_value)
        try:
            self.state = 441
            token = self._input.LA(1)
            if token in [cedlParser.CHRONICLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(cedlParser.CHRONICLE)
                localctx.contextValue='chronicle'

            elif token in [cedlParser.RECENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(cedlParser.RECENT)
                localctx.contextValue='recent'

            elif token in [cedlParser.CONTINUOUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(cedlParser.CONTINUOUS)
                localctx.contextValue='recent'

            elif token in [cedlParser.CUMULATIVE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                self.match(cedlParser.CUMULATIVE)
                localctx.contextValue='cumulative'

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_event_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Atom_event_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFLER(self):
            return self.getToken(cedlParser.IDENTIFLER, 0)

        def string_key(self):
            return self.getTypedRuleContext(cedlParser.String_keyContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_atom_event_name

        def enterRule(self, listener):
            if hasattr(listener, "enterAtom_event_name"):
                listener.enterAtom_event_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtom_event_name"):
                listener.exitAtom_event_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtom_event_name"):
                return visitor.visitAtom_event_name(self)
            else:
                return visitor.visitChildren(self)




    def atom_event_name(self):

        localctx = cedlParser.Atom_event_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_atom_event_name)
        try:
            self.state = 445
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.string_key()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Complex_event_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Complex_event_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFLER(self):
            return self.getToken(cedlParser.IDENTIFLER, 0)

        def string_key(self):
            return self.getTypedRuleContext(cedlParser.String_keyContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_complex_event_name

        def enterRule(self, listener):
            if hasattr(listener, "enterComplex_event_name"):
                listener.enterComplex_event_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComplex_event_name"):
                listener.exitComplex_event_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitComplex_event_name"):
                return visitor.visitComplex_event_name(self)
            else:
                return visitor.visitChildren(self)




    def complex_event_name(self):

        localctx = cedlParser.Complex_event_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_complex_event_name)
        try:
            self.state = 449
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.string_key()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Attr_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFLER(self):
            return self.getToken(cedlParser.IDENTIFLER, 0)

        def string_key(self):
            return self.getTypedRuleContext(cedlParser.String_keyContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_attr_name

        def enterRule(self, listener):
            if hasattr(listener, "enterAttr_name"):
                listener.enterAttr_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttr_name"):
                listener.exitAttr_name(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAttr_name"):
                return visitor.visitAttr_name(self)
            else:
                return visitor.visitChildren(self)




    def attr_name(self):

        localctx = cedlParser.Attr_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_attr_name)
        try:
            self.state = 453
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.string_key()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Time_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Time_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(cedlParser.INT, 0)

        def num_key(self):
            return self.getTypedRuleContext(cedlParser.Num_keyContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_time_value

        def enterRule(self, listener):
            if hasattr(listener, "enterTime_value"):
                listener.enterTime_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime_value"):
                listener.exitTime_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_value"):
                return visitor.visitTime_value(self)
            else:
                return visitor.visitChildren(self)




    def time_value(self):

        localctx = cedlParser.Time_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_time_value)
        try:
            self.state = 457
            token = self._input.LA(1)
            if token in [cedlParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(cedlParser.INT)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.num_key()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Len_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Len_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(cedlParser.INT, 0)

        def num_key(self):
            return self.getTypedRuleContext(cedlParser.Num_keyContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_len_value

        def enterRule(self, listener):
            if hasattr(listener, "enterLen_value"):
                listener.enterLen_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLen_value"):
                listener.exitLen_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLen_value"):
                return visitor.visitLen_value(self)
            else:
                return visitor.visitChildren(self)




    def len_value(self):

        localctx = cedlParser.Len_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_len_value)
        try:
            self.state = 461
            token = self._input.LA(1)
            if token in [cedlParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.match(cedlParser.INT)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.num_key()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Repeat_numContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Repeat_numContext, self).__init__(parent, invokingState)
            self.parser = parser

        def time_value(self):
            return self.getTypedRuleContext(cedlParser.Time_valueContext,0)


        def len_value(self):
            return self.getTypedRuleContext(cedlParser.Len_valueContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_repeat_num

        def enterRule(self, listener):
            if hasattr(listener, "enterRepeat_num"):
                listener.enterRepeat_num(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRepeat_num"):
                listener.exitRepeat_num(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitRepeat_num"):
                return visitor.visitRepeat_num(self)
            else:
                return visitor.visitChildren(self)




    def repeat_num(self):

        localctx = cedlParser.Repeat_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_repeat_num)
        try:
            self.state = 465
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.time_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.len_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_numContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Value_numContext, self).__init__(parent, invokingState)
            self.parser = parser

        def repeat_num(self):
            return self.getTypedRuleContext(cedlParser.Repeat_numContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_value_num

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_num"):
                listener.enterValue_num(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_num"):
                listener.exitValue_num(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitValue_num"):
                return visitor.visitValue_num(self)
            else:
                return visitor.visitChildren(self)




    def value_num(self):

        localctx = cedlParser.Value_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_value_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.repeat_num()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_numericContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Value_numericContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC(self):
            return self.getToken(cedlParser.NUMERIC, 0)

        def value_num(self):
            return self.getTypedRuleContext(cedlParser.Value_numContext,0)


        def getRuleIndex(self):
            return cedlParser.RULE_value_numeric

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_numeric"):
                listener.enterValue_numeric(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_numeric"):
                listener.exitValue_numeric(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitValue_numeric"):
                return visitor.visitValue_numeric(self)
            else:
                return visitor.visitChildren(self)




    def value_numeric(self):

        localctx = cedlParser.Value_numericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_value_numeric)
        try:
            self.state = 471
            token = self._input.LA(1)
            if token in [cedlParser.NUMERIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(cedlParser.NUMERIC)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC, cedlParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.value_num()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Time_unitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Time_unitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIME_UNIT(self):
            return self.getToken(cedlParser.TIME_UNIT, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_time_unit

        def enterRule(self, listener):
            if hasattr(listener, "enterTime_unit"):
                listener.enterTime_unit(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime_unit"):
                listener.exitTime_unit(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_unit"):
                return visitor.visitTime_unit(self)
            else:
                return visitor.visitChildren(self)




    def time_unit(self):

        localctx = cedlParser.Time_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_time_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(cedlParser.TIME_UNIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.NumericContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC(self):
            return self.getToken(cedlParser.NUMERIC, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_numeric

        def enterRule(self, listener):
            if hasattr(listener, "enterNumeric"):
                listener.enterNumeric(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumeric"):
                listener.exitNumeric(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNumeric"):
                return visitor.visitNumeric(self)
            else:
                return visitor.visitChildren(self)




    def numeric(self):

        localctx = cedlParser.NumericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_numeric)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(cedlParser.NUMERIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_keyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.String_keyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(cedlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(cedlParser.FALSE, 0)

        def SELECT(self):
            return self.getToken(cedlParser.SELECT, 0)

        def DEFINE(self):
            return self.getToken(cedlParser.DEFINE, 0)

        def FROM(self):
            return self.getToken(cedlParser.FROM, 0)

        def PATTERN(self):
            return self.getToken(cedlParser.PATTERN, 0)

        def LIMIT(self):
            return self.getToken(cedlParser.LIMIT, 0)

        def TIMEWINDOW(self):
            return self.getToken(cedlParser.TIMEWINDOW, 0)

        def LENWINDOW(self):
            return self.getToken(cedlParser.LENWINDOW, 0)

        def CONTEXT(self):
            return self.getToken(cedlParser.CONTEXT, 0)

        def CHRONICLE(self):
            return self.getToken(cedlParser.CHRONICLE, 0)

        def RECENT(self):
            return self.getToken(cedlParser.RECENT, 0)

        def CONTINUOUS(self):
            return self.getToken(cedlParser.CONTINUOUS, 0)

        def CUMULATIVE(self):
            return self.getToken(cedlParser.CUMULATIVE, 0)

        def AND(self):
            return self.getToken(cedlParser.AND, 0)

        def OR(self):
            return self.getToken(cedlParser.OR, 0)

        def NOT(self):
            return self.getToken(cedlParser.NOT, 0)

        def XOR(self):
            return self.getToken(cedlParser.XOR, 0)

        def NAND(self):
            return self.getToken(cedlParser.NAND, 0)

        def NOR(self):
            return self.getToken(cedlParser.NOR, 0)

        def REPEAT(self):
            return self.getToken(cedlParser.REPEAT, 0)

        def SEQ(self):
            return self.getToken(cedlParser.SEQ, 0)

        def WITHIN(self):
            return self.getToken(cedlParser.WITHIN, 0)

        def FOLLOWBY(self):
            return self.getToken(cedlParser.FOLLOWBY, 0)

        def DURING(self):
            return self.getToken(cedlParser.DURING, 0)

        def EQUAL(self):
            return self.getToken(cedlParser.EQUAL, 0)

        def INTERVAL(self):
            return self.getToken(cedlParser.INTERVAL, 0)

        def AT(self):
            return self.getToken(cedlParser.AT, 0)

        def CONTAINS(self):
            return self.getToken(cedlParser.CONTAINS, 0)

        def COMPARETO(self):
            return self.getToken(cedlParser.COMPARETO, 0)

        def EQUALS(self):
            return self.getToken(cedlParser.EQUALS, 0)

        def MATCHES(self):
            return self.getToken(cedlParser.MATCHES, 0)

        def TIME_UNIT(self):
            return self.getToken(cedlParser.TIME_UNIT, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_string_key

        def enterRule(self, listener):
            if hasattr(listener, "enterString_key"):
                listener.enterString_key(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitString_key"):
                listener.exitString_key(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitString_key"):
                return visitor.visitString_key(self)
            else:
                return visitor.visitChildren(self)




    def string_key(self):

        localctx = cedlParser.String_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_string_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.TRUE) | (1 << cedlParser.FALSE) | (1 << cedlParser.SELECT) | (1 << cedlParser.DEFINE) | (1 << cedlParser.FROM) | (1 << cedlParser.PATTERN) | (1 << cedlParser.LIMIT) | (1 << cedlParser.TIMEWINDOW) | (1 << cedlParser.LENWINDOW) | (1 << cedlParser.CONTEXT) | (1 << cedlParser.CHRONICLE) | (1 << cedlParser.RECENT) | (1 << cedlParser.CONTINUOUS) | (1 << cedlParser.CUMULATIVE) | (1 << cedlParser.AND) | (1 << cedlParser.OR) | (1 << cedlParser.NOT) | (1 << cedlParser.XOR) | (1 << cedlParser.NAND) | (1 << cedlParser.NOR) | (1 << cedlParser.REPEAT) | (1 << cedlParser.SEQ) | (1 << cedlParser.WITHIN) | (1 << cedlParser.FOLLOWBY) | (1 << cedlParser.DURING) | (1 << cedlParser.EQUAL) | (1 << cedlParser.INTERVAL) | (1 << cedlParser.AT) | (1 << cedlParser.CONTAINS) | (1 << cedlParser.COMPARETO) | (1 << cedlParser.EQUALS) | (1 << cedlParser.MATCHES) | (1 << cedlParser.TIME_UNIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Num_keyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(cedlParser.Num_keyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def YEAR(self):
            return self.getToken(cedlParser.YEAR, 0)

        def MON(self):
            return self.getToken(cedlParser.MON, 0)

        def DAY(self):
            return self.getToken(cedlParser.DAY, 0)

        def HOUR(self):
            return self.getToken(cedlParser.HOUR, 0)

        def MIN(self):
            return self.getToken(cedlParser.MIN, 0)

        def SEC(self):
            return self.getToken(cedlParser.SEC, 0)

        def getRuleIndex(self):
            return cedlParser.RULE_num_key

        def enterRule(self, listener):
            if hasattr(listener, "enterNum_key"):
                listener.enterNum_key(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNum_key"):
                listener.exitNum_key(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNum_key"):
                return visitor.visitNum_key(self)
            else:
                return visitor.visitChildren(self)




    def num_key(self):

        localctx = cedlParser.Num_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_num_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.YEAR) | (1 << cedlParser.MON) | (1 << cedlParser.DAY) | (1 << cedlParser.HOUR) | (1 << cedlParser.MIN) | (1 << cedlParser.SEC))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





