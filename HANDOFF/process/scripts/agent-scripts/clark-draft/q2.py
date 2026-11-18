import pandas as pd, sys
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date'])
x=g[g.num.astype(str).str.contains('CPA|WSA',na=False)]
print(x.drop(columns=['running_balance','split']).to_string())
print(g[g.type=='Journal Entry'].num.astype(str).str.replace(r'\d+','#',regex=True).value_counts().head(30))
# 2024 JEs dated 12/31/2024
x=g[(g.type=='Journal Entry')&(g.date=='2024-12-31')]
print(x.drop(columns=['running_balance','split']).to_string())
