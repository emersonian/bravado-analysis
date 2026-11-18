import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
pd.set_option('display.width',250); pd.set_option('display.max_rows',1000); pd.set_option('display.max_colwidth',70); pd.set_option('display.float_format',lambda x:f'{x:,.2f}')
g=pd.read_csv(D+'qb_gl.csv',low_memory=False)
g['date']=pd.to_datetime(g['date'])
g['year']=g.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
def bal(acct,asof):
    s=g[(g.account==acct)&(g.date<=asof)].amount.sum()
    return s+bb.get(acct,0)
