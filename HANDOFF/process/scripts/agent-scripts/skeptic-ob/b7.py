from common import *
f=pd.read_pickle('fl_typed.pkl')
C=['account','dt','amount','Source','Description']
b=f[f.account=='Checking - Chase - PLAT BUS CHECKING 5189'].sort_values('dt')
print(len(b), b.amount.sum().round(2))
pre=b[~((b.Source=='Finaloop'))]
print('sum excl Finaloop adj:', pre.amount.sum().round(2), 'through 4/7:', pre[pre.dt<='2026-04-07 23:59:59'].amount.sum().round(2))
print(b[b.Source=='Finaloop'][C].to_string())
print(b.tail(12)[C].to_string())
print(b.groupby(b.dt.dt.to_period('M')).amount.agg(['sum','count']))
# other reconciliation discrepancy rows
r=f[f.account=='Reconciliation discrepancies']; print(r[C].to_string())
# owner account all rows
o=f[f.account.str.startswith('Due to/from owner')].sort_values('dt'); print(o[C+['Transaction Classification']].to_string())
print(o.amount.sum().round(2), o[o.dt>='2026-01-01'].amount.sum().round(2))
