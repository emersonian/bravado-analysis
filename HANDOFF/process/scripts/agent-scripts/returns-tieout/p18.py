exec(open('load.py').read())
pd.set_option('display.max_colwidth',110)
x=g[(g.amount.abs().round(2).isin([69033.00,157115.47,88082.47,7500.0,8500.0]))]
print(x[['account','date','type','num','name','memo','split','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,80)).to_string(index=False))
d=g[(g.account=='33500 Due to Jeremiah')&(g.year==2025)&(g.type=='Journal Entry')]
print(d[['date','num','memo','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,100)).to_string(index=False))
