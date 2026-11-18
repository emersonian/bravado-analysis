import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',120)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
for a in ['Accrued Expense','Loan From Nguyen','SBA Disaster Loan','Texas State Comptroller Payable']:
    x=g[(g.account==a)&(g.date>='2025-01-01')]
    print('=====',a); print(x.drop(columns=['account']).to_string()[:7000])
for n in ['AJE-484','AJE-493','AJE-501','AJE-527','AJE-547']:
    print('---',n); print(g[g.num==n].drop(columns=['running_balance']).to_string())
# QB 2026 activity summary Jan1-Mar27
y=g[g.date>='2026-01-01']
print(y.groupby('account').amount.sum().round(2).to_string())
