import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',150)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
for n in ['AJE-541','AJE-542','AJE-543','AJE-397']:
    print('---',n); print(g[g.num==n].drop(columns=['running_balance','split','name']).to_string())
print(g[(g.account=='SBA Disaster Loan')].drop(columns=['running_balance','split','name','memo']).to_string())
x=g[g.memo.astype(str).str.contains('SBA',case=False)&(g.date>='2025-01-01')&(g.account.str.contains('Interest|Checking|Found|SBA'))]
print(x.drop(columns=['running_balance','split','name']).to_string()[:5000])
