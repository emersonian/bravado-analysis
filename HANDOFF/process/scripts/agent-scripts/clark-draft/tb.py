import pandas as pd, sys
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',60)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False)
print(g.dtypes); print(g.head(5)); print(g.date.min(), g.date.max())
g['date']=pd.to_datetime(g['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
def bal(asof):
    s=g[g.date<=asof].groupby('account').amount.sum()
    return s.add(bb,fill_value=0)
def act(y):
    return g[g.date.dt.year==y].groupby('account').amount.sum()
t=pd.DataFrame({'bal2023':bal('2023-12-31'),'bal2024':bal('2024-12-31'),'bal2025':bal('2025-12-31'),'bal2026':bal('2026-12-31'),'act2024':act(2024),'act2025':act(2025),'act2026':act(2026)}).fillna(0).round(2)
# last running balance per account for check
last=g.groupby('account').tail(1).set_index('account').running_balance
t['lastrun']=last
print(t.to_string())
t.to_csv('tb.csv')
