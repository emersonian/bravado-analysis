import pandas as pd
pd.set_option('display.width',280); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',100)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv'); f['dt']=pd.to_datetime(f.datetime_utc)
o=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
s=o.groupby('account').amount.agg(['sum','count']).round(2)
print(s.to_string())
k=o[o.account.str.contains('owner|Related|Payroll payable|Capital|Distrib|Loan|Credit card|Checking|Savings|Retained|equity|Equity',case=False,regex=True)]
print(k[['account','datetime_utc','amount','Source','Description']].to_string())
