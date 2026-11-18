exec(open('load.py').read())
pd.set_option('display.max_colwidth',110)
for a in ['33500 Due to Jeremiah','Due from Jer','Due from James',"53000 Jer's Draw"]:
    d=g[(g.account==a)&(g.year>=2022)].copy()
    print('=====',a); print(d.groupby(['year','type']).amount.agg(['sum','count']))
    j=d[(d.type=='Journal Entry')&(d.amount.abs()>=2000)]
    j['memo']=j.memo.fillna('').str.slice(0,105)
    print(j[['date','num','memo','amount']].to_string(index=False))
# running 33500 around 2024
d=g[(g.account=='33500 Due to Jeremiah')&(g.year==2024)].sort_values('date')
print('33500 2024: n',len(d),'sum',d.amount.sum(), 'debits',d[d.amount<0].amount.sum(),'credits',d[d.amount>0].amount.sum())
print(d[d.date>='2024-12-01'][['date','type','num','memo','split','amount']].assign(memo=lambda x:x.memo.fillna('').str.slice(0,80)).tail(15).to_string(index=False))
