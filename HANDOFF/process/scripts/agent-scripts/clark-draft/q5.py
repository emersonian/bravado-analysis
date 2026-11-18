import pandas as pd, sys, itertools
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
y=g[g.date.dt.year==2025]
for a in ['80001 Other Misc Income','Charitable Contributions','Melio services fee','Remittance Discrepancy','67000 Uncategorized Income','66000 Other Income','73400 Financial Fees','Late Penalty Fees','Merchant Fees','Gas','73450 Interest Expense']:
    x=y[y.account==a]
    print('=====',a,len(x),x.amount.sum().round(2))
    print(x.drop(columns=['running_balance','account','split']).to_string()[:6000])
