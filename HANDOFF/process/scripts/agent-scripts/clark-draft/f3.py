import pandas as pd, itertools
t=pd.read_csv('fin_tb.csv',index_col=0)
x=t[t.end.abs()>0.005].end
target=5039.94
names=list(x.index); vals=list(x.values)
for r in (1,2,3):
    for c in itertools.combinations(range(len(names)),r):
        s=sum(vals[i] for i in c)
        for sg in ([1]*r,) :
            if abs(abs(2*s)-target)<0.03 or abs(abs(s)-target)<0.03: print(r,[ (names[i],vals[i]) for i in c], round(s,2))
# mixed signs for pairs
for a,b in itertools.combinations(range(len(names)),2):
    s=vals[a]-vals[b]
    if abs(abs(2*s)-target)<0.03 or abs(abs(s)-target)<0.03: print('diff',names[a],vals[a],names[b],vals[b])
