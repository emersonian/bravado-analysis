import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_rows',1000); pd.set_option('display.max_columns',30); pd.set_option('display.max_colwidth',80)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',parse_dates=['date'])
q['y']=q.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
f=pd.read_csv(D+'finaloop_gl.csv',parse_dates=['datetime_utc'])
f['d']=f.datetime_utc.dt.date
def bal(acct,asof):
    return bb.get(acct,0)+q[(q.account==acct)&(q.date<=asof)].amount.sum()
