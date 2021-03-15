from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot.node('A', 'King Arthur')
dot.render('test-output/round-table.gv', view=True) 

digraph G {
//graph [ratio=.48];
node [style=filled, color=black, shape=circle, width=.6
  fontname=Helvetica, fontweight=bold, fontcolor=white,
  fontsize=24, fixedsize=true];
  B1[label = 35];
    B2[label = 10];
    B3[label = 25];
  B4[label = 40];

  node [style=filled, color=red, shape=circle, width=.6
    fontname=Helvetica, fontweight=bold, fontcolor=white,
    fontsize=24, fixedsize=true];

    R1[label = 15];
    R2[label = 5];
    R3[label = 20];
    R4[label = 30];
    R5[label = 45];

    node  [label = "NIL", style=filled, color=black, shape=record, width=.4,height=.25,
      fontname=Helvetica, fontweight=bold, fontcolor=white,
      fontsize=16, fixedsize=true];
    N1[];
    N2[];
    N3[];
    N4[];
    N5[];
    N6[];
    N7[];
    N8[];
    N9[];
    N10[];

    B1 -> B4;
    B1 -> R1;
    R1 -> B2;
    R1 -> B3;
    B4 -> N1;
    B4 -> R5;

}