from common import *
f=pd.read_pickle('fl_typed.pkl'); g=qb()
pd.set_option('display.max_colwidth',120)
C=['account','dt','amount','Source','Description']
x=f[f.Description.astype(str).str.contains(r'SBA|EIDL|SMALL BUSINESS|TREAS|MYSBA|1201',case=False,regex=True)|f.account.str.contains('Small Business')]
print(x.sort_values('dt')[C].to_string())
print(f[f.account.str.contains('Small Business')].amount.sum())
print(f[f.amount.abs().round(2)==1705.0][C].to_string())
for a in ['Related party loan payable - Hugh & Christy Nguyen','Line of credit - Anthony Tallerine','Loan payable - Ondeck Capital','Related party balance - non interest bearing - Endorphin Farms','Related party balance - non interest bearing - James Nelson','Other payroll deductions payable']:
    d=f[f.account==a]; print(a,len(d),d.amount.sum().round(2)); print(d.sort_values('dt')[C].head(8).to_string())
print('---QB')
Q=['account','date','type','num','name','memo','split','amount']
for a in ['SBA Disaster Loan','Loan From Nguyen','33100 Anthony Tallerine LOC']:
    print(g[g.account==a][Q].to_string())
x=g[g.name.astype(str).str.contains('Nguyen',case=False)|g.memo.astype(str).str.contains('Nguyen',case=False)]
print(x[x.date>='2025-01-01'][Q].to_string())
x=g[(g.memo.astype(str).str.contains('SBA|EIDL',case=False))&(g.date>='2025-01-01')]
print(x[Q].to_string())
