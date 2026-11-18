import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',110); pd.set_option('display.max_rows',2000)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'])
op=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
print(len(op)); print(op.datetime_utc.value_counts().head(10)); print(op.Source.value_counts(dropna=False)); print(op['Transaction Classification'].value_counts(dropna=False))
g=op.groupby('account').agg(n=('amount','size'),amt=('amount','sum')).round(2)
print(g.to_string())
