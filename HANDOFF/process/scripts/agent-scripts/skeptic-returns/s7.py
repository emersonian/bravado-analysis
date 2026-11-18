import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
A=sorted(g.account.unique())
isbs=lambda a: not re.match(r'[6-9]\d{4} ',a)
# full balance by account at each YE for BS-looking accounts (nonzero)
rows=[]
for a in A:
    r=[round(g[(g.account==a)&(g.y<=y)].amount.sum()+bb.get(a,0),2) for y in (2022,2023,2024,2025)]
    rows.append([a]+r)
t=pd.DataFrame(rows,columns=['account',2022,2023,2024,2025]).set_index('account')
pl=[a for a in A if re.match(r'[6-9]\d{4} ',a)]
# print those not P&L numbered
print(t[[isbs(a) for a in t.index]].to_string())
