import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',600)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
print(f.dtypes); print(f.head(3).to_string())
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
print(f.dt.min(), f.dt.max())
print(f.Source.value_counts().head(20))
print(f['Transaction Classification'].value_counts().head(60))
o=f[f.account.str.contains('Jeremiah|James Nelson|Blake|Payroll payable|Nguyen|Tallerine|Clark',na=False)]
print(o.groupby('account').amount.agg(['sum','count']).round(2))
j=f[f.account.str.contains('Due to/from owner')].sort_values('dt')
print(j[['dt','amount','Source','Description','Transaction Classification']].to_string())
