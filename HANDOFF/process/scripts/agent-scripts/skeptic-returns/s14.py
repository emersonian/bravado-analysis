import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv'); f['dt']=pd.to_datetime(f.datetime_utc)
C=['account','datetime_utc','amount','Source','Description']
b=f[f.account.str.startswith(('Checking','Savings'))&(f.dt>='2026-04-24')&(f.dt<='2026-05-12')&(f.amount>=300)]
print(b[C].sort_values('datetime_utc').to_string())
c=f[f.Description.fillna('').str.contains('CAPITAL ONE',case=False)&(f.dt>='2026-01-01')&~f.account.str.startswith(('Money','Checking'))]
print(c[C].sort_values('datetime_utc').to_string())
print(f[f.Description.fillna('').str.contains('Benthall|Blake|Comatri|loan',case=False)&(f.dt>='2026-01-01')][C].head(40).to_string())
