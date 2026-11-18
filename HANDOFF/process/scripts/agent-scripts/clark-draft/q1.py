import pandas as pd, sys
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
print(g[g.account=='34310 Social Security'].to_string())
# find other legs
for _,r in g[(g.account=='34310 Social Security')&(g.date>='2024-01-01')].iterrows():
    print('---',r.num,r.date)
    print(g[(g.num==r.num)&(g.date==r.date)].to_string())
