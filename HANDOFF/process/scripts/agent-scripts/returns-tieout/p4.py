exec(open('load.py').read())
d=g[(g.account=='Wages Due to Jeremiah')].copy()
d['memo']=d.memo.fillna('').str.slice(0,90); d['split']=d.split.fillna('').str.slice(0,35)
print(d[['date','type','num','memo','split','amount']].to_string(index=False))
print(d.groupby(['year','type']).amount.agg(['sum','count']))
for y in (2023,2024,2025):
    x=d[d.year==y]; print(y,'credits',x[x.amount>0].amount.sum(),'debits',x[x.amount<0].amount.sum())
