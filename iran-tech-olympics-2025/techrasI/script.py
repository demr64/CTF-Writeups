from sage.all import *
from Crypto.Util.number import long_to_bytes
es = []
cts = []
with open('output.txt', 'r') as a:
    n = a.readline()
    for i in range(1, 110):
        x = a.readline()
        es.append(int(x[-11:]))
        cts.append(int(x[4:-11]))


n = int(n[4:])

for i in range(0, len(es)):
    for j in range(i+1, len(es)):
        d, u, v = xgcd(es[i], es[j]) 
        msg = pow(cts[i], u, n)*pow(cts[j], v, n)
        try:
            print(long_to_bytes(int(msg)).decode())
        except:
            continue
     
