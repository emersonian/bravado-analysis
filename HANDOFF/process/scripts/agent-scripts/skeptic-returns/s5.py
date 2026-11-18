import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
d=g[g.account=='Wages Due to Jeremiah']
print(d[['date','type','num','memo','split','amount']].assign(memo=d.memo.fillna('').str[:100]).to_string())
for n,dt in [('Gusto','2024-10-28'),('AJE-345','2025-01-31'),('AJE-387','2025-01-31'),('AJE-388','2025-02-28'),('AJE-547','2025-12-31')]:
    x=g[(g.num==n)&(g.date==dt)]
    print(n); print(x[['account','date','memo','amount']].assign(memo=x.memo.fillna('').str[:100]).to_string())
