import pandas as pd
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',100)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
print(g[(g.amount.abs().round(2)==69033.00)][['account','date','type','num','memo','amount']])
x=g[(g.account=='33500 Due to Jeremiah')&(g.y==2025)]
print(len(x), x.amount.sum().round(2)); print(x[x.type=='Journal Entry'][['date','num','memo','amount']].to_string())
print(x.groupby('type').amount.agg(['sum','count']))
print(g[(g.account=="53000 Jer's Draw")&(g.y>=2024)][['date','type','num','memo','split','amount']].to_string())
x=g[(g.account=='Due from Jer')&(g.y>=2023)]; print(x[['date','type','num','memo','split','amount']].to_string())
x=g[(g.account=='33500 Due to Jeremiah')&(g.y==2024)]; print(x.amount.sum(), x[x.type=='Journal Entry'][['date','num','memo','amount']].to_string())
# JE 2022-11-28 on 2023-03-31
x=g[(g.num=='2022-11-28')]; print(x[['account','date','memo','amount']].to_string())
x=g[(g.account=='Loan Receivable - Specialty Bottling Group')]; print(x[['date','type','num','memo','split','amount']].to_string())
# Nguyen payments 2025
x=g[g.name.fillna('').str.contains('Nguyen')&(g.y==2025)]; print(x[['account','date','type','num','memo','split','amount']].to_string())
