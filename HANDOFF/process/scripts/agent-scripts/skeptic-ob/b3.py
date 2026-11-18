from common import *
f=fl()
op=f[f.dt<'2026-01-01'].copy()
# opening lines on non-RE accounts aggregated per source/desc vs RE lines
o=op[op.account.str.contains('Jeremiah|Payroll payable|Prior year|Payroll|Blake',case=False)]
print(o[['account','dt','amount','Source','Description']].to_string(index=False))
re=op[op.account=='Retained earnings']
print('RE rows',len(re), re.amount.sum())
print(re[re.amount.abs()>50000][['account','dt','amount','Source','Description']].to_string(index=False))
print(re[re.amount.abs().round(2).isin([157115.47,75440.62,5330.8,176913.7,69033.0])][['amount','Source','Description']].to_string())
# any 69033 anywhere
print(f[f.amount.abs().round(2).isin([69033.0,157115.47,88082.47])][['account','dt','amount','Source','Description']].to_string())
