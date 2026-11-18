import pandas as pd, sys
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',parse_dates=['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
print(sorted(q.account.unique()))
q['y']=q.date.dt.year
pv=q.pivot_table(index='account',columns='y',values='amount',aggfunc='sum').fillna(0)
pv.insert(0,'bb',bb.reindex(pv.index).fillna(0))
cum=pv.cumsum(axis=1)
keys=[a for a in pv.index if any(k in a for k in ['Jer','James','Due','Wages','Equity','Nguyen','Tallerine','Loan','Note','Coinbase','Clark','Retained','Payable','Accrued'])]
print(pv.loc[keys].round(2))
print(cum.loc[keys].round(2))
