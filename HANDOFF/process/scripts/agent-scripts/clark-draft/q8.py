import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',120)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
x=g[(g.account=='Accrued Expense')&(g.date>='2025-11-30')]
print(x.drop(columns=['account','split','name']).to_string())
x=g[(g.account=='73450 Interest Expense')&(g.date>='2025-06-01')]
print(x.drop(columns=['account','running_balance']).to_string())
# AP by vendor 12/31/2025
ap=g[(g.account=='31000 Accounts Payable')&(g.date<='2025-12-31')].groupby('name').amount.sum().round(2)
print(ap[ap.abs()>0.5].sort_values(ascending=False).to_string()); print(ap.sum())
ap=g[(g.account=='31000 Accounts Payable')].groupby('name').amount.sum().round(2)
print('AP at Mar 27 2026'); print(ap[ap.abs()>0.5].sort_values(ascending=False).head(15).to_string()); print(ap.sum())
