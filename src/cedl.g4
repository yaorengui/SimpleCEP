grammar cedl;
@header{
from code.cedl_node import *
from collections import OrderedDict
from Queue import Queue, Empty
}
@parser::members{
#存储原始事件
global premitive_events
premitive_events = {}
}
cedl_events
    :cedl_event+
    ;

cedl_event returns [premitive_events]
    :select_clause from_clause pattern_clause (limit_clause)? (time_clause|len_clause)? (a=context_clause)?
{
$premitive_events = premitive_events
}
    ;

select_clause
    :((SELECT|DEFINE) complex_event)
    ;
complex_event returns [complexEventID]
    :a = complex_event_name {$complexEventID = $a.text}
    ;
from_clause
    :FROM event_list
    ;
event_list returns [nodes]
    :(a=event
{
$nodes = []
$nodes.append($a.node)
}
    (COMMA b=event
{
$nodes.append($b.node)
}
    )*)
    ;
event returns [node]
    :a=premitive_event
{
$node = $a.node
premitive_events[$a.text] = $node
}
    |a=pattern_event_1{$node = $a.node}
    |a=pattern_event_n{$node = $a.node}
    |a=pattern_event_2{$node = $a.node}
    //|cedl_event
    ;
premitive_event returns [node]
    :event_id=atom_event_name{$node = eType_node($event_id.text,'-1')}
    ;
pattern_clause
    :PATTERN pattern_operators
    ;
pattern_operators returns [node]
    :(a=pattern_event_1
{
$node = eType_node("root","root")
$node.addChildren($a.node)
$a.node.father.append($node)#便于查询两个原子事件的最近共同祖先
}
    |a=pattern_event_2
{
$node = eType_node("root","root")
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |a=pattern_event_n
{
$node = eType_node("root","root")
$node.addChildren($a.node)
$a.node.father.append($node)
}
    )
    (
    link_operator
    (a=pattern_event_1
{
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |a=pattern_event_2
{
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |a=pattern_event_n
{
$node.addChildren($a.node)
$a.node.father.append($node)
}
    )
    )*
    ;
link_operator
    :AMP2
    |PIPE2
    ;
pattern_event_1 returns [node]
    :(NOT OPEN_PAR a=event CLOSE_PAR)
{
$node = eType_node('not','not')
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |(REPEAT OPEN_PAR a=event COMMA b=repeat_num CLOSE_PAR)
{
$node = eType_node('repeat','repeat')
$node.repeatNum = $b.text
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |(WITHIN OPEN_PAR a=event COMMA ((b=time_value c=time_unit)|(time_start COMMA time_end)) CLOSE_PAR)
 {
$node = eType_node('within','within')
$node.timeval = $b.text
$node.timeunit = $c.text

$node.addChildren($a.node)
$a.node.father.append($node)
 }
    |(INTERVAL OPEN_PAR a=event COMMA b= time_value c=time_unit CLOSE_PAR)
{
$node = eType_node('interval','interval')
$node.timeval = $b.text
$node.timeunit = $c.text

$node.addChildren($a.node)
$a.node.father.append($node)
}
    |(AT OPEN_PAR a=event COMMA time CLOSE_PAR)
{
$node = eType_node('at','at')
$node.addChildren($a.node)
$a.node.father.append($node)
}
    |(AVG OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'avg',str($b.text),str($c.text),str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
    |(SUM OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'sum',$b.text,$c.text,str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
    |(MINOP OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'min',$b.text,$c.text,str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
    |(MAX OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'max',$b.text,$c.text,str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
  |(DEC OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'dec',$b.text,$c.text,str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
  |(INC OPEN_PAR a =event COMMA b=len_value COMMA c=attr_name COMMA d = attr_name CLOSE_PAR)
{
$node = aggregationNode(str($d.text),'inc',$b.text,$c.text,str($d.text))
$node.addChildren($a.node)
$a.node.father.append($node)

premitive_events[str($d.text)] = $node
}
    ;

time
    :TIME_COMPLETE
    ;
time_start
    :time
    ;
time_end
    :time
    ;
pattern_event_2 returns [node]
    :(XOR OPEN_PAR a=event COMMA b=event CLOSE_PAR)
{
$node = eType_node('xor','xor')
$node.addChildren($a.node)
$node.addChildren($b.node)
$a.node.father.append($node)
$b.node.father.append($node)
}
    |(DURING OPEN_PAR a=event COMMA b=event CLOSE_PAR)
{
$node = eType_node('during','during')
$node.addChildren($a.node)
$node.addChildren($b.node)
$a.node.father.append($node)
$b.node.father.append($node)
}
    ;
pattern_event_n returns [node]
    :a=(AND|OR|NAND|NOR|SEQ|FOLLOWBY|EQUAL) OPEN_PAR b=event_list CLOSE_PAR
{
$node = eType_node($a.text,$a.text)
for item in $b.nodes:
  $node.addChildren(item)
  item.father.append($node)
}
    ;

limit_clause
    :LIMIT filters
    ;
filters returns [nodes]
    :a=limit_filter
{
i=0
$nodes=[]
node = attach_node(i)
node.restrictions = $a.dic
$nodes.append(node)
i+=1
}
    (
    AND a=limit_filter
{
node = attach_node(i)
node.restrictions = $a.dic
$nodes.append(node)
i+=1
}
    )*
    ;
limit_filter returns [dic]
    :(e=premitive_event DOT attr=attr_name op=filter_operator v=filter_value)
{
$dic = {}
$dic['op']= str($op.op)
$dic['event_name']=str($e.text)
$dic['event_attr']=str($attr.text)
$dic['value']=$v.v
}
    |(e=premitive_event DOT attr=attr_name DOT fun=CONTAINS OPEN_PAR  v_str=STRING  CLOSE_PAR)
{
$dic = {}
$dic['op']=$fun.text
$dic['event_name']=$e.text
$dic['event_attr']=$attr.text
$dic['value']=$v_str.text
}
    |(e=premitive_event DOT attr=attr_name DOT fun=EQUALS OPEN_PAR  v_str=STRING CLOSE_PAR)
{
$dic = {}
$dic['op']=$fun.text
$dic['event_name']=$e.text
$dic['event_attr']=$attr.text
$dic['value']=$v_str.text
}
    |(e=premitive_event DOT attr=attr_name DOT fun=COMPARETO OPEN_PAR v_str=STRING CLOSE_PAR)
{
$dic = {}
$dic['op']=$fun.text
$dic['event_name']=$e.text
$dic['event_attr']=$attr.text
$dic['value']=$v_str.text
}
    |(e=premitive_event DOT attr=attr_name DOT fun=MATCHES OPEN_PAR v_str=STRING CLOSE_PAR)
{
$dic = {}
$dic['op']=$fun.text
$dic['event_name']=$e.text
$dic['event_attr']=$attr.text
$dic['value']=$v_str.text
}
    ;
filter_operator returns [op]
    :a=(EQ|GT|GT_EQ|LT|LT_EQ|NOT_EQ1|NOT_EQ2){$op = $a.text}
    ;

filter_value returns [v]
    :
    TRUE {$v = True}
    |FALSE {$v = False}
    |( DOLLAR a = premitive_event DOT b=attr_name) //使用DOLLAR是为了避免引起与BOOL变量的岐义
{
$v = {}
$v['event_name'] = $a.text
$v['event_attr'] = $b.text
}
    |c=value_num{$v = $c.text}//包含INT
    |c=value_numeric{$v = $c.text}//包含INT
    |d=STRING {$v = str($d.text)}
    ;

time_clause
     :TIMEWINDOW time_value time_unit
     ;

len_clause
    :LENWINDOW len_value
    ;

context_clause returns [context]
    :CONTEXT a=context_value{$context=$a.text}
    ;
context_value returns [contextValue]
    :CHRONICLE{$contextValue='chronicle'}
    |RECENT{$contextValue='recent'}
    |CONTINUOUS{$contextValue='recent'}
    |CUMULATIVE{$contextValue='cumulative'}
    ;
atom_event_name
    :IDENTIFLER
    |string_key
    ;
complex_event_name
    :IDENTIFLER
    |string_key
    ;

attr_name
    :IDENTIFLER
    |string_key//若没有该行，则关键字不属于attr_name
    ;
time_value
    :INT
    |num_key
    ;
len_value
    :INT
    |num_key
    ;
repeat_num
    :time_value
    |len_value
    ;
value_num
    :repeat_num
    ;
value_numeric
    :NUMERIC
    |value_num
    ;
time_unit
    :TIME_UNIT
    ;

numeric
    :NUMERIC
    ;

string_key:TRUE|FALSE|SELECT|DEFINE|FROM|PATTERN|LIMIT|TIMEWINDOW|LENWINDOW|CONTEXT|
           CHRONICLE|RECENT|CONTINUOUS|CUMULATIVE|
           AND|OR|NOT|XOR|NAND|NOR|REPEAT|
           SEQ|WITHIN|FOLLOWBY|DURING|EQUAL|INTERVAL|AT|
           CONTAINS|COMPARETO|EQUALS|MATCHES|
           TIME_UNIT
    ;
num_key:YEAR|MON|DAY|HOUR|MIN|SEC;

 //跳过空格符、制表符、换行符
 WS
    : ( ' ' | '\t' | '\n' | '\r' )+ -> skip
    ;
 /*
 词法规则
 */
 //主要关键词

 TRUE:T R U E;
 FALSE:F A L S E;
 SELECT:S E L E C T;
 DEFINE:D E F I N E;
 FROM:F R O M;
 PATTERN:P A T T E R N;
 LIMIT:L I M I T;
 TIMEWINDOW:T I M E W I N D O W;
 LENWINDOW:L E N W I N D O W;
 CONTEXT:C O N T E X T;
 //CONTEXT的关键词
 CHRONICLE:C H R O N I C L E;
 RECENT:R E C E N T;
 CONTINUOUS:C O N T I N U O U S;
 CUMULATIVE:C U M U L A T I V E;
 //新增操作符
 AVG:A V G;
 SUM:S U M;
 MINOP:M I N;
 MAX:M A X;
 COUNT:C O U N T;
 DEC:D E C;
 INC:I N C;
 //基本逻辑操作符
 AND:A N D;
 OR:O R;
 NOT:N O T;
 XOR:X O R;
 NAND:N A N D;
 NOR:N O R;
 REPEAT:R E P E A T;
 //时态逻辑操作符
 SEQ:S E Q;
 WITHIN: W I T H I N;
 FOLLOWBY:F O L L O W B Y;
 DURING:D U R I N G;
 EQUAL:E Q U A L;
 INTERVAL:I N T E R V A L;
 AT:A T;
//字符匹配约束符
CONTAINS:C O N T A I N S?;
COMPARETO:C O M P A R E T O;
EQUALS:E Q U A L S?;
MATCHES:M A T C H E S?;

TIME_UNIT:((S)|(M)|(H)|(D)|(S E C S?)|(M I N S?)|(H O U R S?)|(D A Y S?));

//标识
//优先识别前面的关键字，识别失败时才匹配为IDENTIFLER
IDENTIFLER
    :[a-zA-Z_][a-zA-Z_0-9]*
    ;
//与数字有关
TIME_COMPLETE
    :(YEAR('-'MON)('-'DAY)('-'HOUR)('-'MIN)('-'SEC)?)
    |(YEAR('-'MON)('-'DAY)('-'HOUR))
    |(YEAR('-'MON)('-'DAY))
    |(YEAR('-'MON))
   // |YEAR
    ;

YEAR:([2]|[1])([0-9][0-9][0-9]);
MON:(([0]?[1-9])|([1][0])|([1][1])|([1][2]));
DAY:(([0]?[1-9])|(([1]|[2])[0-9])|([3]([0]|[1])));
HOUR:(([0]?[1-9])|([1][0-9])|([2]([0]|[1]|[2]|[3])));
MIN:([0]?[1-9])|(([1]|[2]|[3]|[4]|[5])[0-9]);
SEC:([0]?[1-9])|(([1]|[2]|[3]|[4]|[5])[0-9]);

INT
    :[0]
    |[1-9][0-9]*
    |YEAR
    |MON
    |DAY
    |HOUR
    |MIN
    |SEC
    ;

NUMERIC
    :[-+]?DIGIT+('.'DIGIT*)?(E[-+]?DIGIT+)?
    |'.'DIGIT+(E[-+]?DIGIT+)?
    ;


 //基本比较符
 LT : '<';
 LT_EQ : '<=';
 GT : '>';
 GT_EQ : '>=';
 EQ : '=';
 NOT_EQ1 : '!=';


 LT2 : '<<';
 GT2 : '>>';
 EQ2 : '==';
 NOT_EQ2 : '<>';

  //基本运算符
 PLUS : '+';
 MINUS : '-';
 STAR : '*';
 DIV : '/';
 MOD : '%';
//逻辑运算符
 AMP : '&';
 AMP2: '&&';
 PIPE : '|';
 PIPE2 : '||';
 //基本符号
 OPEN_PAR : '(';
 CLOSE_PAR : ')';
 OPEN_CURLY: '{';
 CLOSE_CURLY: '}';
 COMMA : ',';
 SCOL : ';';
 DOT : '.';
 TILDE : '~';

 //特殊符号
 DOLLAR:'$';

 //字符串
STRING
    : ('\'')( ~'\'' | '\'\'' )*('\'')
   |(('"') ( ~'\'' | '\'\'' )*('"'))
    ;

//布尔值
//BOOL:TRUE|FALSE;
//TRUE:T R U E;
//FALSE:F A L S E;
//TRUE:T R U E;
//FALSE:F A L S E;

 //单行注释
SINGLE_LINE_COMMENT
    : '--' ~[\r\n]* -> channel(HIDDEN)
    ;
//多行注释
MULTI_LINE_COMMENT
    : '/*' .*? ( '*/' | EOF ) -> channel(HIDDEN)
    ;
fragment CC:( ~'\'' | '\'\'' )*;
fragment NUM:[1-9][0-9]+;
fragment DIGIT : [0-9];

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

