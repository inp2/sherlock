0.22::explorer.
0.22::acro.
0.66::notepad.
0.11::firefox.
0.66::dropbox.
0.66::net.    
0.33::y.
0.33::n.
0.33::m.

h1 :- explorer,firefox,dropbox.
h2 :- explorer,acro,notepad.
h3 :- explorer,acro,net.

    evidence(h1, true).
    evidence(h3, true).
    
y :- h1,h2,h3.
n :- \+h1,\+h2,\+h3.
m :- \+h1,h2,h3.
m :- h1,\+h2,h3.
m :- h1,h2,\+h3.

query(y).
query(m).
query(n).   
