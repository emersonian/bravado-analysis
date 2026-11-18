import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',150)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
for n in ['AJE-455','AJE-456','AJE-380','AJE-422','AJE-229','AJE-253','AJE-270']:
    print('---',n); print(g[g.num==n].drop(columns=['running_balance','split','name']).to_string())
# 2026 QB P&L quick: interest, AMEX etc
print(g[(g.account=='Business AMEX Card_3007')&(g.date>='2025-12-01')].drop(columns=['running_balance','account']).to_string()[:3000])
