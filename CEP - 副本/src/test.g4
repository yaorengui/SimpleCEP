grammar test;
e returns [v]
    :a = e op = '*' b = e {$v = $a.v*$b.v}
    |a = e op = '/' b = e {$v = $a.v/$b.v}
    |a = e op = '+' b = e {$v = $a.v+$b.v}
    |a = e op = '-' b = e {$v = $a.v-$b.v}
    |'('e')' {$v = $e.v}
    |INT
    ;
 INT:([1-9]([0-9])*|[0]);
 //indentifier:^((?!hede).)*;
 //indentifier1:

WS: (' ' | '\t' | '\n' | '\r' )+ -> skip;