import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv'); f['dt']=pd.to_datetime(f.datetime_utc)
C=['account','datetime_utc','amount','Source','Description']
a=f[(f.dt>='2026-04-01')&(f.amount.abs()>=7000)&(f.amount.abs()<=9000)]
print('7000-9000 after Apr 1:',len(a)); print(a[C].to_string())
a=f[(f.dt>='2026-01-01')&(f.amount.abs().round(2).isin([7500.0,8500.0,1000.0]))]
print(a[C].to_string())
print(f[f.account.str.contains('Benthall|Capital -')&(f.dt>='2026-01-01')][C].to_string())
a=f[(f.dt>='2026-04-20')&(f.dt<='2026-05-10')&(f.amount.abs()>=2000)]
print(a[C].to_string())
o=f[f.account.str.contains('Ondeck|OnDeck',case=False)]
print(o[C].to_string()); print(o.amount.sum().round(2))
# loans/owner 2026 accounts list
print(f[f.account.str.contains('loan|Loan|Line of credit|Due to/from|Related party')].groupby('account').amount.agg(['sum','count']).round(2))
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date'])
x=g[(g.amount.abs().round(2).isin([7500.0,8500.0]))&(g.date>='2023-06-01')]
print(x[['account','date','type','num','name','memo','amount']].to_string())
print(g.date.max())
