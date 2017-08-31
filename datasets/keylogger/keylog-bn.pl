0.0975::explorer.
0.0731::acro.
0.0243::net.
0.6::mal.
0.33::y.
0.33::n.
0.33::m.

h:-explorer,acro,net,mal,y.
h:-\+explorer,\+acro,\+net,\+mal,n.
h:-explorer,\+acro,\+net,mal,m.   

evidence(h,true).

query(y).
query(n).
query(m).
