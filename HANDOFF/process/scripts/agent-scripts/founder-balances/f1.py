import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',2000)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
print(f.dtypes); print(f.head(3).T)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,errors='coerce')
print(f.dt.min(), f.dt.max(), f.dt.isna().sum())
print(f.Source.value_counts().head(40))
print(f['Transaction Classification'].value_counts().head(80))
op=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
print(len(op)); print(op.datetime_utc.value_counts().head(10))
print(op[['account','amount','Source','Description','Transaction Classification']].to_string())
