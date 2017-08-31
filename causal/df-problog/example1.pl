0.7::e1.
0.9::e2.
0.9::e3.
0.7::e4.
0.33::y.
0.33::n.
0.33::m.    

h:- e1,e2,e3,e4,y.
h:- \+e1,\+e2,\+e3,\+e4,\+n.
h:- e1,\+e2,\+e3,\+e4,m.    
    
evidence(h,true).
    
query(y).
query(n).
query(m).    
