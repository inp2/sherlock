0.1::explorer.
0.1::firefox.
0.1::acro.
0.7::net.
0.33::y.
0.33::n.
0.33::m.

web:-explorer,firefox.
pdf:-firefox,acro.
mal:-acro,net.    

h:-web,pdf,mal,y.
h:-\+web,\+pdf,\+mal,n.
h:-\+web,pdf,mal,m.   
h:-\+web,\+pdf,mal,m.
h:-web,\+pdf,mal,m.    

evidence(h,true).

query(y).
query(n).
query(m).
