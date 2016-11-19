# Generated from C:/Users/fit/PycharmProjects/CEP/src\cedl.g4 by ANTLR 4.5.1
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
        buf.write(u"M\u018d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
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
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00dd")
        buf.write(u"\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\5\21\u00f7\n\21\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\24\7\24\u0108\n\24\f\24\16\24\u010b\13\24\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0141\n")
        buf.write(u"\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\5\27\u0159\n\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write(u"\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\5\34\u0169\n")
        buf.write(u"\34\3\35\3\35\5\35\u016d\n\35\3\36\3\36\5\36\u0171\n")
        buf.write(u"\36\3\37\3\37\5\37\u0175\n\37\3 \3 \5 \u0179\n \3!\3")
        buf.write(u"!\5!\u017d\n!\3\"\3\"\3#\3#\5#\u0183\n#\3$\3$\3%\3%\3")
        buf.write(u"&\3&\3\'\3\'\3\'\2\2(\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL\2\t\3\2\6\7\4")
        buf.write(u"\2??AA\7\2\22\23\26\27\31\31\33\33\35\35\4\2/\6488\3")
        buf.write(u"\2\16\21\3\2\4$\3\2\',\u018b\2O\3\2\2\2\4S\3\2\2\2\6")
        buf.write(u"b\3\2\2\2\be\3\2\2\2\nh\3\2\2\2\fk\3\2\2\2\16\u0082\3")
        buf.write(u"\2\2\2\20\u0084\3\2\2\2\22\u0087\3\2\2\2\24\u0093\3\2")
        buf.write(u"\2\2\26\u00a6\3\2\2\2\30\u00dc\3\2\2\2\32\u00de\3\2\2")
        buf.write(u"\2\34\u00e0\3\2\2\2\36\u00e2\3\2\2\2 \u00f6\3\2\2\2\"")
        buf.write(u"\u00f8\3\2\2\2$\u00fe\3\2\2\2&\u0101\3\2\2\2(\u0140\3")
        buf.write(u"\2\2\2*\u0142\3\2\2\2,\u0158\3\2\2\2.\u015a\3\2\2\2\60")
        buf.write(u"\u015e\3\2\2\2\62\u0161\3\2\2\2\64\u0164\3\2\2\2\66\u0168")
        buf.write(u"\3\2\2\28\u016c\3\2\2\2:\u0170\3\2\2\2<\u0174\3\2\2\2")
        buf.write(u">\u0178\3\2\2\2@\u017c\3\2\2\2B\u017e\3\2\2\2D\u0182")
        buf.write(u"\3\2\2\2F\u0184\3\2\2\2H\u0186\3\2\2\2J\u0188\3\2\2\2")
        buf.write(u"L\u018a\3\2\2\2NP\5\4\3\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2")
        buf.write(u"\2QR\3\2\2\2R\3\3\2\2\2ST\5\6\4\2TU\5\n\6\2UW\5\22\n")
        buf.write(u"\2VX\5$\23\2WV\3\2\2\2WX\3\2\2\2X[\3\2\2\2Y\\\5.\30\2")
        buf.write(u"Z\\\5\60\31\2[Y\3\2\2\2[Z\3\2\2\2[\\\3\2\2\2\\^\3\2\2")
        buf.write(u"\2]_\5\62\32\2^]\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\b\3\1")
        buf.write(u"\2a\5\3\2\2\2bc\t\2\2\2cd\5\b\5\2d\7\3\2\2\2ef\58\35")
        buf.write(u"\2fg\b\5\1\2g\t\3\2\2\2hi\7\b\2\2ij\5\f\7\2j\13\3\2\2")
        buf.write(u"\2kl\5\16\b\2ls\b\7\1\2mn\7F\2\2no\5\16\b\2op\b\7\1\2")
        buf.write(u"pr\3\2\2\2qm\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\r")
        buf.write(u"\3\2\2\2us\3\2\2\2vw\5\20\t\2wx\b\b\1\2x\u0083\3\2\2")
        buf.write(u"\2yz\5\30\r\2z{\b\b\1\2{\u0083\3\2\2\2|}\5\"\22\2}~\b")
        buf.write(u"\b\1\2~\u0083\3\2\2\2\177\u0080\5 \21\2\u0080\u0081\b")
        buf.write(u"\b\1\2\u0081\u0083\3\2\2\2\u0082v\3\2\2\2\u0082y\3\2")
        buf.write(u"\2\2\u0082|\3\2\2\2\u0082\177\3\2\2\2\u0083\17\3\2\2")
        buf.write(u"\2\u0084\u0085\5\66\34\2\u0085\u0086\b\t\1\2\u0086\21")
        buf.write(u"\3\2\2\2\u0087\u0088\7\t\2\2\u0088\u0089\5\24\13\2\u0089")
        buf.write(u"\23\3\2\2\2\u008a\u008b\5\30\r\2\u008b\u008c\b\13\1\2")
        buf.write(u"\u008c\u0094\3\2\2\2\u008d\u008e\5 \21\2\u008e\u008f")
        buf.write(u"\b\13\1\2\u008f\u0094\3\2\2\2\u0090\u0091\5\"\22\2\u0091")
        buf.write(u"\u0092\b\13\1\2\u0092\u0094\3\2\2\2\u0093\u008a\3\2\2")
        buf.write(u"\2\u0093\u008d\3\2\2\2\u0093\u0090\3\2\2\2\u0094\u00a3")
        buf.write(u"\3\2\2\2\u0095\u009f\5\26\f\2\u0096\u0097\5\30\r\2\u0097")
        buf.write(u"\u0098\b\13\1\2\u0098\u00a0\3\2\2\2\u0099\u009a\5 \21")
        buf.write(u"\2\u009a\u009b\b\13\1\2\u009b\u00a0\3\2\2\2\u009c\u009d")
        buf.write(u"\5\"\22\2\u009d\u009e\b\13\1\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write(u"\u0096\3\2\2\2\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2")
        buf.write(u"\2\u00a0\u00a2\3\2\2\2\u00a1\u0095\3\2\2\2\u00a2\u00a5")
        buf.write(u"\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write(u"\25\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\t\3\2\2\u00a7")
        buf.write(u"\27\3\2\2\2\u00a8\u00a9\7\24\2\2\u00a9\u00aa\7B\2\2\u00aa")
        buf.write(u"\u00ab\5\16\b\2\u00ab\u00ac\7C\2\2\u00ac\u00ad\3\2\2")
        buf.write(u"\2\u00ad\u00ae\b\r\1\2\u00ae\u00dd\3\2\2\2\u00af\u00b0")
        buf.write(u"\7\30\2\2\u00b0\u00b1\7B\2\2\u00b1\u00b2\5\16\b\2\u00b2")
        buf.write(u"\u00b3\7F\2\2\u00b3\u00b4\5@!\2\u00b4\u00b5\7C\2\2\u00b5")
        buf.write(u"\u00b6\3\2\2\2\u00b6\u00b7\b\r\1\2\u00b7\u00dd\3\2\2")
        buf.write(u"\2\u00b8\u00b9\7\32\2\2\u00b9\u00ba\7B\2\2\u00ba\u00bb")
        buf.write(u"\5\16\b\2\u00bb\u00c3\7F\2\2\u00bc\u00bd\5<\37\2\u00bd")
        buf.write(u"\u00be\5F$\2\u00be\u00c4\3\2\2\2\u00bf\u00c0\5\34\17")
        buf.write(u"\2\u00c0\u00c1\7F\2\2\u00c1\u00c2\5\36\20\2\u00c2\u00c4")
        buf.write(u"\3\2\2\2\u00c3\u00bc\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c4")
        buf.write(u"\u00c5\3\2\2\2\u00c5\u00c6\7C\2\2\u00c6\u00c7\3\2\2\2")
        buf.write(u"\u00c7\u00c8\b\r\1\2\u00c8\u00dd\3\2\2\2\u00c9\u00ca")
        buf.write(u"\7\36\2\2\u00ca\u00cb\7B\2\2\u00cb\u00cc\5\16\b\2\u00cc")
        buf.write(u"\u00cd\7F\2\2\u00cd\u00ce\5<\37\2\u00ce\u00cf\5F$\2\u00cf")
        buf.write(u"\u00d0\7C\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\b\r\1\2")
        buf.write(u"\u00d2\u00dd\3\2\2\2\u00d3\u00d4\7\37\2\2\u00d4\u00d5")
        buf.write(u"\7B\2\2\u00d5\u00d6\5\16\b\2\u00d6\u00d7\7F\2\2\u00d7")
        buf.write(u"\u00d8\5\32\16\2\u00d8\u00d9\7C\2\2\u00d9\u00da\3\2\2")
        buf.write(u"\2\u00da\u00db\b\r\1\2\u00db\u00dd\3\2\2\2\u00dc\u00a8")
        buf.write(u"\3\2\2\2\u00dc\u00af\3\2\2\2\u00dc\u00b8\3\2\2\2\u00dc")
        buf.write(u"\u00c9\3\2\2\2\u00dc\u00d3\3\2\2\2\u00dd\31\3\2\2\2\u00de")
        buf.write(u"\u00df\7&\2\2\u00df\33\3\2\2\2\u00e0\u00e1\5\32\16\2")
        buf.write(u"\u00e1\35\3\2\2\2\u00e2\u00e3\5\32\16\2\u00e3\37\3\2")
        buf.write(u"\2\2\u00e4\u00e5\7\25\2\2\u00e5\u00e6\7B\2\2\u00e6\u00e7")
        buf.write(u"\5\16\b\2\u00e7\u00e8\7F\2\2\u00e8\u00e9\5\16\b\2\u00e9")
        buf.write(u"\u00ea\7C\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b\21\1")
        buf.write(u"\2\u00ec\u00f7\3\2\2\2\u00ed\u00ee\7\34\2\2\u00ee\u00ef")
        buf.write(u"\7B\2\2\u00ef\u00f0\5\16\b\2\u00f0\u00f1\7F\2\2\u00f1")
        buf.write(u"\u00f2\5\16\b\2\u00f2\u00f3\7C\2\2\u00f3\u00f4\3\2\2")
        buf.write(u"\2\u00f4\u00f5\b\21\1\2\u00f5\u00f7\3\2\2\2\u00f6\u00e4")
        buf.write(u"\3\2\2\2\u00f6\u00ed\3\2\2\2\u00f7!\3\2\2\2\u00f8\u00f9")
        buf.write(u"\t\4\2\2\u00f9\u00fa\7B\2\2\u00fa\u00fb\5\f\7\2\u00fb")
        buf.write(u"\u00fc\7C\2\2\u00fc\u00fd\b\22\1\2\u00fd#\3\2\2\2\u00fe")
        buf.write(u"\u00ff\7\n\2\2\u00ff\u0100\5&\24\2\u0100%\3\2\2\2\u0101")
        buf.write(u"\u0102\5(\25\2\u0102\u0109\b\24\1\2\u0103\u0104\7\22")
        buf.write(u"\2\2\u0104\u0105\5(\25\2\u0105\u0106\b\24\1\2\u0106\u0108")
        buf.write(u"\3\2\2\2\u0107\u0103\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write(u"\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\'\3\2\2\2\u010b")
        buf.write(u"\u0109\3\2\2\2\u010c\u010d\5\20\t\2\u010d\u010e\7H\2")
        buf.write(u"\2\u010e\u010f\5:\36\2\u010f\u0110\5*\26\2\u0110\u0111")
        buf.write(u"\5,\27\2\u0111\u0112\3\2\2\2\u0112\u0113\b\25\1\2\u0113")
        buf.write(u"\u0141\3\2\2\2\u0114\u0115\5\20\t\2\u0115\u0116\7H\2")
        buf.write(u"\2\u0116\u0117\5:\36\2\u0117\u0118\7H\2\2\u0118\u0119")
        buf.write(u"\7 \2\2\u0119\u011a\7B\2\2\u011a\u011b\7K\2\2\u011b\u011c")
        buf.write(u"\7C\2\2\u011c\u011d\3\2\2\2\u011d\u011e\b\25\1\2\u011e")
        buf.write(u"\u0141\3\2\2\2\u011f\u0120\5\20\t\2\u0120\u0121\7H\2")
        buf.write(u"\2\u0121\u0122\5:\36\2\u0122\u0123\7H\2\2\u0123\u0124")
        buf.write(u"\7\"\2\2\u0124\u0125\7B\2\2\u0125\u0126\7K\2\2\u0126")
        buf.write(u"\u0127\7C\2\2\u0127\u0128\3\2\2\2\u0128\u0129\b\25\1")
        buf.write(u"\2\u0129\u0141\3\2\2\2\u012a\u012b\5\20\t\2\u012b\u012c")
        buf.write(u"\7H\2\2\u012c\u012d\5:\36\2\u012d\u012e\7H\2\2\u012e")
        buf.write(u"\u012f\7!\2\2\u012f\u0130\7B\2\2\u0130\u0131\7K\2\2\u0131")
        buf.write(u"\u0132\7C\2\2\u0132\u0133\3\2\2\2\u0133\u0134\b\25\1")
        buf.write(u"\2\u0134\u0141\3\2\2\2\u0135\u0136\5\20\t\2\u0136\u0137")
        buf.write(u"\7H\2\2\u0137\u0138\5:\36\2\u0138\u0139\7H\2\2\u0139")
        buf.write(u"\u013a\7#\2\2\u013a\u013b\7B\2\2\u013b\u013c\7K\2\2\u013c")
        buf.write(u"\u013d\7C\2\2\u013d\u013e\3\2\2\2\u013e\u013f\b\25\1")
        buf.write(u"\2\u013f\u0141\3\2\2\2\u0140\u010c\3\2\2\2\u0140\u0114")
        buf.write(u"\3\2\2\2\u0140\u011f\3\2\2\2\u0140\u012a\3\2\2\2\u0140")
        buf.write(u"\u0135\3\2\2\2\u0141)\3\2\2\2\u0142\u0143\t\5\2\2\u0143")
        buf.write(u"\u0144\b\26\1\2\u0144+\3\2\2\2\u0145\u0146\7\4\2\2\u0146")
        buf.write(u"\u0159\b\27\1\2\u0147\u0148\7\5\2\2\u0148\u0159\b\27")
        buf.write(u"\1\2\u0149\u014a\7J\2\2\u014a\u014b\5\20\t\2\u014b\u014c")
        buf.write(u"\7H\2\2\u014c\u014d\5:\36\2\u014d\u014e\3\2\2\2\u014e")
        buf.write(u"\u014f\b\27\1\2\u014f\u0159\3\2\2\2\u0150\u0151\5B\"")
        buf.write(u"\2\u0151\u0152\b\27\1\2\u0152\u0159\3\2\2\2\u0153\u0154")
        buf.write(u"\5D#\2\u0154\u0155\b\27\1\2\u0155\u0159\3\2\2\2\u0156")
        buf.write(u"\u0157\7K\2\2\u0157\u0159\b\27\1\2\u0158\u0145\3\2\2")
        buf.write(u"\2\u0158\u0147\3\2\2\2\u0158\u0149\3\2\2\2\u0158\u0150")
        buf.write(u"\3\2\2\2\u0158\u0153\3\2\2\2\u0158\u0156\3\2\2\2\u0159")
        buf.write(u"-\3\2\2\2\u015a\u015b\7\13\2\2\u015b\u015c\5<\37\2\u015c")
        buf.write(u"\u015d\5F$\2\u015d/\3\2\2\2\u015e\u015f\7\f\2\2\u015f")
        buf.write(u"\u0160\5> \2\u0160\61\3\2\2\2\u0161\u0162\7\r\2\2\u0162")
        buf.write(u"\u0163\5\64\33\2\u0163\63\3\2\2\2\u0164\u0165\t\6\2\2")
        buf.write(u"\u0165\65\3\2\2\2\u0166\u0169\7%\2\2\u0167\u0169\5J&")
        buf.write(u"\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169\67\3")
        buf.write(u"\2\2\2\u016a\u016d\7%\2\2\u016b\u016d\5J&\2\u016c\u016a")
        buf.write(u"\3\2\2\2\u016c\u016b\3\2\2\2\u016d9\3\2\2\2\u016e\u0171")
        buf.write(u"\7%\2\2\u016f\u0171\5J&\2\u0170\u016e\3\2\2\2\u0170\u016f")
        buf.write(u"\3\2\2\2\u0171;\3\2\2\2\u0172\u0175\7-\2\2\u0173\u0175")
        buf.write(u"\5L\'\2\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write(u"=\3\2\2\2\u0176\u0179\7-\2\2\u0177\u0179\5L\'\2\u0178")
        buf.write(u"\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179?\3\2\2\2\u017a")
        buf.write(u"\u017d\5<\37\2\u017b\u017d\5> \2\u017c\u017a\3\2\2\2")
        buf.write(u"\u017c\u017b\3\2\2\2\u017dA\3\2\2\2\u017e\u017f\5@!\2")
        buf.write(u"\u017fC\3\2\2\2\u0180\u0183\7.\2\2\u0181\u0183\5B\"\2")
        buf.write(u"\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183E\3\2\2")
        buf.write(u"\2\u0184\u0185\7$\2\2\u0185G\3\2\2\2\u0186\u0187\7.\2")
        buf.write(u"\2\u0187I\3\2\2\2\u0188\u0189\t\7\2\2\u0189K\3\2\2\2")
        buf.write(u"\u018a\u018b\t\b\2\2\u018bM\3\2\2\2\30QW[^s\u0082\u0093")
        buf.write(u"\u009f\u00a3\u00c3\u00dc\u00f6\u0109\u0140\u0158\u0168")
        buf.write(u"\u016c\u0170\u0174\u0178\u017c\u0182")
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
                     u"<INVALID>", u"'<'", u"'<='", u"'>'", u"'>='", u"'='", 
                     u"'!='", u"'<<'", u"'>>'", u"'=='", u"'<>'", u"'+'", 
                     u"'-'", u"'*'", u"'/'", u"'%'", u"'&'", u"'&&'", u"'|'", 
                     u"'||'", u"'('", u"')'", u"'{'", u"'}'", u"','", u"';'", 
                     u"'.'", u"'~'", u"'$'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"TRUE", u"FALSE", u"SELECT", 
                      u"DEFINE", u"FROM", u"PATTERN", u"LIMIT", u"TIMEWINDOW", 
                      u"LENWINDOW", u"CONTEXT", u"CHRONICLE", u"RECENT", 
                      u"CONTINUOUS", u"CUMULATIVE", u"AND", u"OR", u"NOT", 
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
    AND=16
    OR=17
    NOT=18
    XOR=19
    NAND=20
    NOR=21
    REPEAT=22
    SEQ=23
    WITHIN=24
    FOLLOWBY=25
    DURING=26
    EQUAL=27
    INTERVAL=28
    AT=29
    CONTAINS=30
    COMPARETO=31
    EQUALS=32
    MATCHES=33
    TIME_UNIT=34
    IDENTIFLER=35
    TIME_COMPLETE=36
    YEAR=37
    MON=38
    DAY=39
    HOUR=40
    MIN=41
    SEC=42
    INT=43
    NUMERIC=44
    LT=45
    LT_EQ=46
    GT=47
    GT_EQ=48
    EQ=49
    NOT_EQ1=50
    LT2=51
    GT2=52
    EQ2=53
    NOT_EQ2=54
    PLUS=55
    MINUS=56
    STAR=57
    DIV=58
    MOD=59
    AMP=60
    AMP2=61
    PIPE=62
    PIPE2=63
    OPEN_PAR=64
    CLOSE_PAR=65
    OPEN_CURLY=66
    CLOSE_CURLY=67
    COMMA=68
    SCOL=69
    DOT=70
    TILDE=71
    DOLLAR=72
    STRING=73
    SINGLE_LINE_COMMENT=74
    MULTI_LINE_COMMENT=75

    def __init__(self, input):
        super(cedlParser, self).__init__(input)
        self.checkVersion("4.5.1")
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
                self.context_clause()



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
            if token in [cedlParser.NOT, cedlParser.REPEAT, cedlParser.WITHIN, cedlParser.INTERVAL, cedlParser.AT]:
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
                if token in [cedlParser.NOT, cedlParser.REPEAT, cedlParser.WITHIN, cedlParser.INTERVAL, cedlParser.AT]:
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
            self.state = 218
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
            self.state = 220
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
            self.state = 222
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
            self.state = 224
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
            self.state = 244
            token = self._input.LA(1)
            if token in [cedlParser.XOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(cedlParser.XOR)
                self.state = 227
                self.match(cedlParser.OPEN_PAR)
                self.state = 228
                localctx.a = self.event()
                self.state = 229
                self.match(cedlParser.COMMA)
                self.state = 230
                localctx.b = self.event()
                self.state = 231
                self.match(cedlParser.CLOSE_PAR)

                localctx.node = eType_node('xor','xor')
                localctx.node.addChildren(localctx.a.node)
                localctx.node.addChildren(localctx.b.node)
                localctx.a.node.father.append(localctx.node)
                localctx.b.node.father.append(localctx.node)


            elif token in [cedlParser.DURING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(cedlParser.DURING)
                self.state = 236
                self.match(cedlParser.OPEN_PAR)
                self.state = 237
                localctx.a = self.event()
                self.state = 238
                self.match(cedlParser.COMMA)
                self.state = 239
                localctx.b = self.event()
                self.state = 240
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
            self.state = 246
            localctx.a = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.AND) | (1 << cedlParser.OR) | (1 << cedlParser.NAND) | (1 << cedlParser.NOR) | (1 << cedlParser.SEQ) | (1 << cedlParser.FOLLOWBY) | (1 << cedlParser.EQUAL))) != 0)):
                localctx.a = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 247
            self.match(cedlParser.OPEN_PAR)
            self.state = 248
            localctx.b = self.event_list()
            self.state = 249
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
            self.state = 252
            self.match(cedlParser.LIMIT)
            self.state = 253
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
            self.state = 255
            localctx.a = self.limit_filter()

            i=0
            localctx.nodes=[]
            node = attach_node(i)
            node.restrictions = localctx.a.dic
            localctx.nodes.append(node)
            i+=1

            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cedlParser.AND:
                self.state = 257
                self.match(cedlParser.AND)
                self.state = 258
                localctx.a = self.limit_filter()

                node = attach_node(i)
                node.restrictions = localctx.a.dic
                localctx.nodes.append(node)
                i+=1

                self.state = 265
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
            self.state = 318
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                localctx.e = self.premitive_event()
                self.state = 267
                self.match(cedlParser.DOT)
                self.state = 268
                localctx.attr = self.attr_name()
                self.state = 269
                localctx.op = self.filter_operator()
                self.state = 270
                localctx.v = self.filter_value()

                localctx.dic = {}
                localctx.dic['op']= localctx.op.op
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=localctx.v.v

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                localctx.e = self.premitive_event()
                self.state = 275
                self.match(cedlParser.DOT)
                self.state = 276
                localctx.attr = self.attr_name()
                self.state = 277
                self.match(cedlParser.DOT)
                self.state = 278
                localctx.fun = self.match(cedlParser.CONTAINS)
                self.state = 279
                self.match(cedlParser.OPEN_PAR)
                self.state = 280
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 281
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                localctx.e = self.premitive_event()
                self.state = 286
                self.match(cedlParser.DOT)
                self.state = 287
                localctx.attr = self.attr_name()
                self.state = 288
                self.match(cedlParser.DOT)
                self.state = 289
                localctx.fun = self.match(cedlParser.EQUALS)
                self.state = 290
                self.match(cedlParser.OPEN_PAR)
                self.state = 291
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 292
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                localctx.e = self.premitive_event()
                self.state = 297
                self.match(cedlParser.DOT)
                self.state = 298
                localctx.attr = self.attr_name()
                self.state = 299
                self.match(cedlParser.DOT)
                self.state = 300
                localctx.fun = self.match(cedlParser.COMPARETO)
                self.state = 301
                self.match(cedlParser.OPEN_PAR)
                self.state = 302
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 303
                self.match(cedlParser.CLOSE_PAR)

                localctx.dic = {}
                localctx.dic['op']=(None if localctx.fun is None else localctx.fun.text)
                localctx.dic['event_name']=(None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop)))
                localctx.dic['event_attr']=(None if localctx.attr is None else self._input.getText((localctx.attr.start,localctx.attr.stop)))
                localctx.dic['value']=(None if localctx.v_str is None else localctx.v_str.text)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 307
                localctx.e = self.premitive_event()
                self.state = 308
                self.match(cedlParser.DOT)
                self.state = 309
                localctx.attr = self.attr_name()
                self.state = 310
                self.match(cedlParser.DOT)
                self.state = 311
                localctx.fun = self.match(cedlParser.MATCHES)
                self.state = 312
                self.match(cedlParser.OPEN_PAR)
                self.state = 313
                localctx.v_str = self.match(cedlParser.STRING)
                self.state = 314
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
            self.state = 320
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
            self.state = 342
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(cedlParser.TRUE)
                localctx.v = True
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(cedlParser.FALSE)
                localctx.v = False
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(cedlParser.DOLLAR)
                self.state = 328
                localctx.a = self.premitive_event()
                self.state = 329
                self.match(cedlParser.DOT)
                self.state = 330
                localctx.b = self.attr_name()

                localctx.v = {}
                localctx.v['event_name'] = (None if localctx.a is None else self._input.getText((localctx.a.start,localctx.a.stop)))
                localctx.v['event_attr'] = (None if localctx.b is None else self._input.getText((localctx.b.start,localctx.b.stop)))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                localctx.c = self.value_num()
                localctx.v = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 337
                localctx.c = self.value_numeric()
                localctx.v = (None if localctx.c is None else self._input.getText((localctx.c.start,localctx.c.stop)))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 340
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
            self.state = 344
            self.match(cedlParser.TIMEWINDOW)
            self.state = 345
            self.time_value()
            self.state = 346
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
            self.state = 348
            self.match(cedlParser.LENWINDOW)
            self.state = 349
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
            self.state = 351
            self.match(cedlParser.CONTEXT)
            self.state = 352
            self.context_value()
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cedlParser.CHRONICLE) | (1 << cedlParser.RECENT) | (1 << cedlParser.CONTINUOUS) | (1 << cedlParser.CUMULATIVE))) != 0)):
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
            self.state = 358
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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
            self.state = 362
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
            self.state = 366
            token = self._input.LA(1)
            if token in [cedlParser.IDENTIFLER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(cedlParser.IDENTIFLER)

            elif token in [cedlParser.TRUE, cedlParser.FALSE, cedlParser.SELECT, cedlParser.DEFINE, cedlParser.FROM, cedlParser.PATTERN, cedlParser.LIMIT, cedlParser.TIMEWINDOW, cedlParser.LENWINDOW, cedlParser.CONTEXT, cedlParser.CHRONICLE, cedlParser.RECENT, cedlParser.CONTINUOUS, cedlParser.CUMULATIVE, cedlParser.AND, cedlParser.OR, cedlParser.NOT, cedlParser.XOR, cedlParser.NAND, cedlParser.NOR, cedlParser.REPEAT, cedlParser.SEQ, cedlParser.WITHIN, cedlParser.FOLLOWBY, cedlParser.DURING, cedlParser.EQUAL, cedlParser.INTERVAL, cedlParser.AT, cedlParser.CONTAINS, cedlParser.COMPARETO, cedlParser.EQUALS, cedlParser.MATCHES, cedlParser.TIME_UNIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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
            self.state = 370
            token = self._input.LA(1)
            if token in [cedlParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(cedlParser.INT)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
            self.state = 374
            token = self._input.LA(1)
            if token in [cedlParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(cedlParser.INT)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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
            self.state = 378
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.time_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
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
            self.state = 380
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
            self.state = 384
            token = self._input.LA(1)
            if token in [cedlParser.NUMERIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(cedlParser.NUMERIC)

            elif token in [cedlParser.YEAR, cedlParser.MON, cedlParser.DAY, cedlParser.HOUR, cedlParser.MIN, cedlParser.SEC, cedlParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
            self.state = 386
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
            self.state = 388
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
            self.state = 390
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
            self.state = 392
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





