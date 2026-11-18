import pandas as pd, sys
pd.set_option('display.width',330); pd.set_option('display.max_colwidth',170); pd.set_option('display.max_rows',2000)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'])
op=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()].copy()
bulk=['Amazon - Bravado Spice - United States','Amazon order - Bravado Spice - United States','Shopify - bravado-spice']
o=op[~op.Source.isin(bulk)].sort_values(['Source','account'])
o['account']=o.account.str[:62]
print(o[['datetime_utc','account','amount','Source','Description','Transaction Classification']].to_string(index=False))
print(op[op.Source.isin(bulk)].groupby(['Source','account']).amount.agg(['sum','count']).round(2))
