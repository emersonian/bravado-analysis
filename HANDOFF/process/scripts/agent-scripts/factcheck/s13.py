import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',140); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed'); f['d']=f.dt.dt.date; f['M']=f.dt.dt.strftime('%Y-%m')
s=f[f.account=='Salaries & wages (via Gusto)']
print(s.Description.str.replace(r'\d{2}/\d{2}/\d{4}','D',regex=True).value_counts().head(30))
print(s.sort_values('dt')[['dt','amount','Description']].tail(30).to_string())
print(s.groupby('d').amount.agg(['sum','count']).round(2).to_string())
c=f[f.account=='Contractors'].sort_values('dt'); print(c[['dt','amount','Source','Description']].to_string())
