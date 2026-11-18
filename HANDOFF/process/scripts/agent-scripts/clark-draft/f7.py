import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',150)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
re=f[f.account=='Retained earnings']
print(re.groupby(['d','Source']).amount.agg(['sum','count']).round(2).to_string())
print(re[re.amount.abs()>300].drop(columns=['dt','m','account','d']).to_string())
print(re.Description.astype(str).str[:60].value_counts().head(20))
# all opening entries (d<=2025-12-31) by account & source
op=f[f.d<='2025-12-31']
print(op.groupby(['account','Source','Description'],dropna=False).amount.agg(['sum','count']).round(2).to_string())
