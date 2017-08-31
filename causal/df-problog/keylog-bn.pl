0.333::explorer.
0.333::acro.
0.666::net.
0.666::firefox.
0.666::notepad.
0.3333::y.
0.3333::n.
0.3333::m.

%h:-explorer,firefox,acro,net,notepad,y.
%h:-explorer,firefox,\+acro,\+net,\+notepad,m.
%h:-\+explorer,\+firefox,\+acro,\+net,\+notepad,n.

h1:-explorer,firefox,y.
h1:-\+explorer,\+firefox,n.
h1:-\+explorer,firefox,m.
h1:-explorer,\+firefox,m.

h2:-explorer,acro,net,y.
h2:-\+explorer,acro,net,m.
h2:-explorer,\+acro,net,m.
h2:-explorer,acro,\+net,m.
h2:-\+explorer,\+acro,\+net,n.
    
h3:-acro,notepad,y.
h3:-\+acro,\+notepad,n.
h3:-\+acro,notepad,m.
h3:-acro,\+notepad,m.
    
h:-h1,h2,h3,y.
h:-h1,\+h2,h3,m.
h:-\+h1,h2,h3,m.
h:-h1,h2,\+h3,m.
%h:-\+h1,\+h2,\+h3,n.

evidence(h3,true).
evidence(h1,true).
evidence(h2,true).
%evidence(h,true).

query(y).
query(n).
query(m).
