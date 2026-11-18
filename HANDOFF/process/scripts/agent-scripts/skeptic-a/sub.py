from common import *
import numpy as np, itertools
x=g[(g.account=='80001 Other Misc Income')&(g.date.dt.year==2025)]
vals=list(x.amount.round(2))+[0.92]
labels=[f"{r.num or r.name}:{r.amount}" for r in x.itertuples()]+['int 0.92']
n=len(vals); print(n)
v=np.array([round(a*100) for a in vals],dtype=np.int64)
idx=np.arange(1<<n,dtype=np.int64)
s=np.zeros(1<<n,dtype=np.int64)
for i in range(n):
    s+=((idx>>i)&1)*v[i]
for target in [13178100,2431600]:
    hit=np.where(np.abs(s-target)<=60)[0]
    print(target,len(hit))
    for h in hit[:15]:
        print(s[h]/100,[labels[i] for i in range(n) if (h>>i)&1 and v[i]>100000], 'small:',sum(1 for i in range(n) if (h>>i)&1 and v[i]<=100000))
