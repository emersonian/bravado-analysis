from common import *
g=qb()
d=g[g.account=='Due from Jer'].sort_values('date')
print(d[['date','type','num','name','memo','split','amount']].to_string(index=False))
print('--- Wages Due')
d=g[g.account=='Wages Due to Jeremiah'].sort_values('date')
print(d[['date','type','num','name','memo','split','amount']].to_string(index=False))
print(d.groupby([d.date.dt.year,'type']).amount.agg(['sum','count']))
print('--- 33500 & draw 2025+ non-expense types / by type')
for a in ['33500 Due to Jeremiah',"53000 Jer's Draw"]:
    d=g[(g.account==a)&(g.date>='2025-01-01')]
    print(a); print(d.groupby([d.date.dt.year,'type']).amount.agg(['sum','count']))
    print(d[d.type=='Journal Entry'][['date','type','num','name','memo','split','amount']].to_string(index=False))
    print(d[d.date>='2025-12-01'][['date','type','num','name','memo','split','amount']].to_string(index=False))
