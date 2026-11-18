from common import *
f=fl()
op=f[f.dt<'2026-01-01']
print(len(op), op.dt.min(), op.dt.max())
agg=op.groupby('account').amount.agg(['sum','count']).round(2)
print(agg.to_string())
own=f[f.account.str.contains('Jeremiah|owner|Payroll payable|Retained|Prior year',case=False)]
print(own.account.value_counts())
o2=op[op.account.str.contains('Jeremiah|Payroll payable|Retained earnings|Prior year',case=False)]
print(o2.sort_values(['Source','Description','account'])[['account','dt','amount','Source','Description']].to_string(index=False))
