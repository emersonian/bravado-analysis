import pandas as pd, sys
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',80); pd.set_option('display.max_rows',500)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
print(q.dtypes); print(q.head(5)); print(q.date.min(), q.date.max())
q['date']=pd.to_datetime(q['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
accts=sorted(q.account.unique())
for a in accts: print(repr(a), len(q[q.account==a]), round(q[q.account==a].amount.sum(),2))
print(q.type.value_counts())
