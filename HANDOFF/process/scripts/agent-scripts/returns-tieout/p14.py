exec(open('load.py').read())
pd.set_option('display.max_colwidth',100)
for a in ['Member Equity - Coinbase','Member Equity - Clark','Member Equity - Nguyen','Debt to Equity - Hugh and Christy Nguyen','Debt to Equity - Mark Clark','Loan From Nguyen','Loan From Mark Clark','29000 Company Vehicle - Box Truck','27000 Machinery & Equipment','Member Equity - Tallerine','Forward Financing Loan','33100 Anthony Tallerine LOC']:
    d=g[(g.account==a)&(g.year>=2023)].copy()
    d['memo']=d.memo.fillna('').str.slice(0,95); d['split']=d.split.fillna('').str.slice(0,28)
    if len(d)>14: 
        print('=====',a,'(n=%d) by year/type'%len(d)); print(d.groupby(['year','type']).amount.agg(['sum','count'])); continue
    print('=====',a); print(d[['date','type','num','name','memo','split','amount']].to_string(index=False))
