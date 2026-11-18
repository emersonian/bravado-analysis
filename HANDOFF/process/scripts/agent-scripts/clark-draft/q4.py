import pandas as pd, sys, itertools
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
y=g[g.date.dt.year==2024]
for v in [411.38,440.68,26.43,1909.30,1913.54,414.25,438.66,411,412,440,441,1909,1910]:
    x=y[(y.amount.abs()-v).abs()<0.75]
    print('==',v); print(x.drop(columns=['running_balance']).to_string()[:3000])
