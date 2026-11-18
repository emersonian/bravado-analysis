import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',100)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
C=['account','date','type','num','name','memo','split','amount']
x=g[(g.date=='2023-03-07')&(g.type=='Deposit')]; print(x[C].to_string())
x=g[g.memo.fillna('').str.contains('box truck',case=False)]; print(x[C].to_string())
x=g[(g.account=='73450 Interest Expense')&(g.y==2025)&g.name.fillna('').str.contains('Nguyen')]; print(x[C].to_string())
x=g[(g.y==2025)&(g.date.isin(pd.to_datetime(['2025-07-07','2025-07-28','2025-08-30','2025-09-02'])))&(g.account.isin(['73450 Interest Expense','11200 Chase Checking 5189','Loan From Nguyen','31000 Accounts Payable']))&(g.amount.abs().isin([4707,1000,963,925,3707,3744,3782]))]; print(x[C].to_string())
# 2023 dues: look for 1100 / 1099.88 entries in 73500 2023, and anything amount 1100 dated 2023 edited after Apr 23 2024?
x=g[(g.y==2023)&(g.amount.abs().round(2).isin([1100.0,1099.88]))]; print(x[C].to_string())
# 5039: payments 2025
# Spark 2025
x=g[(g.account=='32400 Spark Business Credit Card - 4964')&(g.y==2025)]; print(x[C].to_string())
