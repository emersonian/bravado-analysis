import pandas as pd
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',120)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv'); f['dt']=pd.to_datetime(f.datetime_utc); 
print(f.dt.min(), f.dt.max(), len(f))
o=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
print(len(o)); print(o[['account','datetime_utc','amount','Source','Description']].to_string())
print('sum opening',round(o.amount.sum(),2))
