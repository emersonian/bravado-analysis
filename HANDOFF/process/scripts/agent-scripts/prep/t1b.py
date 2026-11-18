from ld import *
ap=q[q.account=='31000 Accounts Payable']
x=ap[ap['name'].isna()]
print(x[x.amount.abs()>1000][['date','type','num','memo','split','amount']].to_string())
for n in ['Mark Clark','Endorphin Farms']:
    x=ap[ap['name']==n]
    print('\n',n); print(x[x.date>='2023-06-01'][['date','type','num','memo','split','amount']].to_string())
print(f[f.account.str.contains('Endorphin')][['datetime_utc','amount','Source','Description']].to_string())
print(f[f.Source.astype(str).str.contains('Mark Clark|Endorphin|Total Debt',case=False)|f.Description.astype(str).str.contains('Mark Clark|Endorphin',case=False)][['account','datetime_utc','amount','Source','Description']].to_string())
