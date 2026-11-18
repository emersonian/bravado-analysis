from common import *
pd.set_option('display.max_colwidth',75)
pat='blake|benthall|usdc|coinbase|solana|crypto|comatri'
m=f.Description.str.contains(pat,case=False)|f.Source.str.contains(pat,case=False)
print('keyword rows:',m.sum()); print(f[m][['account','dt','amount','Description']].to_string())
a=f.amount.abs().round(2)
print('7500/8500 rows all dates:', f[a.isin([7500,8500])][['account','dt','amount','Description']].to_string())
bank=[x for x in f.account.unique() if x.startswith(('Checking','Savings'))]
m=f.account.isin(bank)&f.Description.str.contains('capital one|5820',case=False)
x=f[m].sort_values('dt'); print(x.assign(account=x.account.str[11:40],Description=x.Description.str[:70])[['account','dt','amount','Description']].to_string())
print('in',x[x.amount>0].amount.sum(),'out',x[x.amount<0].amount.sum())
# where each capital one bank line was classified: match by description+date in non-bank accounts
nb=f[~f.account.isin(bank)&f.Description.str.contains('capital one|5820',case=False)&~f.account.isin(['Money-in','Money-out','Money in transit'])]
print(nb.groupby('account').amount.agg(['sum','count']))
# inflows >=1000 Apr 28 - May 10
x=f[f.account.isin(bank)&(f.dt>='2026-04-28')&(f.dt<'2026-05-11')&(f.amount>=1000)]
print(x[['account','dt','amount','Description']].to_string())
# QB: last date and any blake
print(g.date.max()); m=g.memo.str.contains(pat,case=False)|g.name.str.contains(pat,case=False)
print(g[m&(g.date>='2026-01-01')][['account','date','amount','name','memo']].to_string())
