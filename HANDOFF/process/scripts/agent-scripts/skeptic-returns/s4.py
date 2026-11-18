import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
w=g[g.account=='73902 Salaries & Wages'].copy()
for y in (2023,2024,2025):
    x=w[w.y==y]
    print(y, round(x.amount.sum(),2)); print(x.groupby('type').amount.agg(['sum','count']).round(2))
    j=x[x.type=='Journal Entry'].copy()
    j['k']=j.memo.fillna('').str.replace(r'\d+','#',regex=True).str[:45]
    print(j.groupby('k').amount.agg(['sum','count']).round(2).to_string())
    print(x[x.type!='Journal Entry'][['date','type','num','name','memo','amount']].to_string())
print('WAGES DUE')
d=g[g.account=='Wages Due to Jeremiah']
print(d[['date','type','num','name','memo','split','amount']].to_string())
print(d.groupby('y').apply(lambda x: pd.Series({'cr':x.amount[x.amount>0].sum(),'dr':x.amount[x.amount<0].sum(),'n+':(x.amount>0).sum(),'n-':(x.amount<0).sum()})))
