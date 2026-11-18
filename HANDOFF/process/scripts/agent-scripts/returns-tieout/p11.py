import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',1000); pd.set_option('display.max_colwidth',90); pd.set_option('display.float_format',lambda x:f'{x:,.2f}')
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f.datetime_utc,utc=True,errors='coerce')
print(f.dt.min(), f.dt.max())
o=f[f.dt<'2026-01-01']
print(len(o)); print(o.groupby('account').amount.agg(['sum','count']).to_string())
x=o[o.account.str.contains('owner|Distribution|Capital|Payroll payable|James|Nelson|Retained|Opening',case=False,na=False)]
print(x[['account','datetime_utc','amount','Source','Description','Transaction Classification']].to_string(index=False))
