import pandas as pd, sys
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
y=g[g.date.dt.year==2024]
for a in ['74000 Bad Debts','Remittance Discrepancy','75500 Reimbursements','80001 Other Misc Income','Melio Credit card fee','66000 Other Income','Free fill','Slotting Fees','72601 Marketing Scanbacks']:
    x=y[y.account==a]
    print('=====',a,len(x),x.amount.sum().round(2))
    print(x.drop(columns=['running_balance','account']).to_string())
