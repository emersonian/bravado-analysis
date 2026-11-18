from common import *
f=pd.read_pickle('fl_typed.pkl')
pd.set_option('display.max_colwidth',110)
C=['dt','amount','Source','Description']
for a in ['Distributions - Jeremiah Tallerine','Reimbursements to owners','Capital - Jeremiah Tallerine','Capital - Blake Benthall']:
    d=f[(f.account==a)].sort_values('dt')
    print('=====',a,len(d),d.amount.sum().round(2), '2026:',len(d[d.dt>='2026-01-01']), d[d.dt>='2026-01-01'].amount.sum().round(2))
    print(d[C].to_string(index=False))
p=f[f.account=='Payroll payable'].sort_values('dt')
print(len(p), p.amount.sum().round(2), p[p.dt>='2026-01-01'].amount.sum().round(2))
print(p.groupby(['Source']).amount.agg(['sum','count']))
print(p.groupby(['Description']).amount.agg(['sum','count']).to_string())
print(p[['dt','amount','Source','Description']].tail(15).to_string(index=False))
