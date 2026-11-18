import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',110)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
P=f[f.account.isin(pl.Account)]
piv=P.pivot_table(index='account',columns='m',values='amount',aggfunc='sum',fill_value=0).round(0)
piv['tot']=piv.sum(axis=1)
piv=piv.reindex(pl.Account)
print(piv.to_string())
for a in ['Due to/from owner - non-interest balance - Jeremiah Tallerine','Distributions - Jeremiah Tallerine','Reimbursements to owners','Contractors','Payroll payable']:
    x=f[(f.account==a)].sort_values('dt')
    print('=====',a,len(x),round(x.amount.sum(),2))
    print(x.groupby('m').amount.agg(['sum','count']).round(2).to_string())
    print(x[x.amount.abs()>=200].drop(columns=['dt','m','account','d']).to_string()[:12000])
print(f.d.max(), f[f.d>='2026-07-22'].groupby('d').size())
