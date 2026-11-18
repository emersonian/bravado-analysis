import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
ar=g[g.account=='12000 Accounts Receivable'].copy()
ar['cust']=ar.name.fillna('(none)').str.split(':').str[0]
b25=ar[ar.date<='2025-12-31'].groupby('cust').amount.sum().round(2)
b25=b25[b25.abs()>0.5].sort_values(ascending=False)
print(b25.to_string()); print('total',b25.sum())
y=ar[ar.date>'2025-12-31']
print(y.groupby('type').amount.agg(['sum','count']).round(2))
p=y.pivot_table(index='cust',columns='type',values='amount',aggfunc='sum',fill_value=0).round(2)
p['open']=b25.reindex(p.index).fillna(0); print(p.sort_values('open',ascending=False).to_string())
# aging of 12/31/2025 open AR: by invoice num
inv=ar[ar.date<='2025-12-31']
