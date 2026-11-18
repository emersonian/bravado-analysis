import pandas as pd, sys
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',80)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date'])
g['y']=g.date.dt.year
print(g.dtypes); print(g.type.value_counts())
p=g.pivot_table(index='account',columns='y',values='amount',aggfunc='sum').round(2)
print(p.to_string())
print(open(D+'qb_beginning_balances.csv').read())
