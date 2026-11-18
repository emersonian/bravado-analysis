import pandas as pd, sys
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',dtype=str,keep_default_na=False)
g['amount']=g['amount'].astype(float); g['date']=pd.to_datetime(g['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
pd.set_option('display.width',250,'display.max_rows',500,'display.float_format','{:,.2f}'.format)
def bal(d):
    s=g[g.date<=d].groupby('account').amount.sum()
    return s.add(bb,fill_value=0)
def act(y):
    return g[g.date.dt.year==y].groupby('account').amount.sum()
df=pd.DataFrame({'b2023':bal('2023-12-31'),'b2024':bal('2024-12-31'),'b2025':bal('2025-12-31'),'b2026':bal('2026-12-31'),'a2024':act(2024),'a2025':act(2025),'a2026':act(2026)}).fillna(0)
print(df.round(2).to_string())
