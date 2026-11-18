from ld import *
o=f[f.datetime_utc<'2026-01-01'].copy()
g=o.groupby(['account']).amount.agg(['sum','count'])
print(g.round(2).to_string())
big=o[o.amount.abs()>2000]
for _,r in big.sort_values(['account','datetime_utc']).iterrows():
    print(str(r.datetime_utc)[:16], f"{r.amount:>12.2f}", '|', r.account[:55], '|', str(r.Source)[:30], '|', str(r.Description)[-70:])
x=q[(q.account=='73902 Salaries & Wages')&(q.y==2025)]
print(x.groupby(['type']).amount.sum())
j=x[x.type=='Journal Entry']
print(j[~j.num.astype(str).str.contains('Gusto')][['date','num','memo','amount']].to_string())
print(j.groupby(j.num.astype(str).str[:6]).amount.agg(['sum','count']).to_string())
print(x[x.type!='Journal Entry'][['date','type','name','memo','amount','split']].to_string())
