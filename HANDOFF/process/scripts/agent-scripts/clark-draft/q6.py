import itertools, numpy as np
items={'AJE380 ERC':17248.74,'ERC 3/10':7329.17,'ERC 5/6':62268.27,'AJE422':911.02,'AJE455':7661.73,'AJE456':43743.70,'AJE496':3034.90,'ERC 12/5':14443.33,'intearn':0.92,'66000':62.03,'67000':1500.00,'charit':-900,'melio':-278.5,'remit':-12.95,'latefee':-912.52,'finfee':-100}
k=list(items); v=np.array([items[x] for x in k])
for target in (131781,24316):
  print('target',target)
  for r in range(1,len(k)+1):
    for c in itertools.combinations(range(len(k)),r):
        s=v[list(c)].sum()
        if abs(s-target)<=1.6: print(round(s,2),[k[i] for i in c])
