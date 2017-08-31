0.4::explorer.
0.6::firefox.
0.6::acro.
0.6::net.
0.6::mal.
0.33::y.
0.33::n.
0.33::m.

h:-explorer,firefox,acro,net,mal,y.
h:-\+explorer,\+firefox,\+acro,\+net,\+mal,n.
h:-explorer,\+firefox,\+acro,\+net,mal,m.   

evidence(h,true).

query(y).
query(n).
query(m).
