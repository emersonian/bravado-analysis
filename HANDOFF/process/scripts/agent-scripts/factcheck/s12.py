import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',110); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed'); f['d']=f.dt.dt.date; f['M']=f.dt.dt.strftime('%Y-%m')
g=f[f.Source=='Gusto']
print(g.groupby(['account','M']).amount.agg(['sum','count']).round(2).to_string())
print('last gusto dates', sorted(g.d.unique())[-6:])
print(g[g.dt>='2026-04-01'][['dt','account','amount','Description']].to_string())
p=f[f.account=='Payroll payable'].sort_values('dt')
print(p.groupby(['M','Source']).amount.agg(['sum','count']).round(2).to_string())
print(p[p.Source!='Gusto'][['dt','amount','Source','Description']].to_string())
t=f[f.account=='Other payroll deductions payable'].sort_values('dt'); print(t.groupby(['M','Source']).amount.agg(['sum','count']).round(2)); print(t[t.Source!='Gusto'][['dt','amount','Source','Description']].to_string())
t=f[f.account=='Contractors'].sort_values('dt'); print(t.groupby('M').amount.agg(['sum','count']).round(2))
