from common import *
g=qb(); b=bb()
print(g.dtypes); print(g.date.min(), g.date.max())
accts=[a for a in g.account.unique() if any(k in a for k in ['Jer','James','Tallerine','Wages Due'])]
print(accts)
for y in range(2019,2026):
    cut=pd.Timestamp(f'{y}-12-31')
    s=g[g.date<=cut].groupby('account').amount.sum()
    print(y,{a: round(s.get(a,0)+b.get(a,0),2) for a in accts})
s=g.groupby('account').amount.sum()
print('all',{a: round(s.get(a,0)+b.get(a,0),2) for a in accts})
