import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',140)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
x=g[(g.account=='31000 Accounts Payable')&(g.name.isna())]
print(x.drop(columns=['account','name','running_balance']).to_string())
x=g[(g.account=='31000 Accounts Payable')&(g.name.isin(['Mark Clark','Endorphin Farms']))&(g.date>='2024-06-01')]
print(x.drop(columns=['account','running_balance']).to_string()[:6000])
