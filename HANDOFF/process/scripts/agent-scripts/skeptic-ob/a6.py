from common import *
g=qb()
pd.set_option('display.max_colwidth',100)
C=['account','date','type','num','name','memo','split','amount']
print(g[g.num.isin(['7588','7590','7589','7591'])][C].to_string(index=False))
j=g[(g.date>='2026-01-01')&(g.amount.abs().round(2).isin([3250.0,180.0,400.0,1700.0,1500.0,1000.0]))&(g.date<='2026-02-28')]
print(j[C].to_string(index=False))
print(g[(g.account=='33500 Due to Jeremiah')&(g.date>='2026-01-01')][C].to_string(index=False))
print(g[g.name.astype(str).str.contains('Beacher|Finnacle',case=False)][C].to_string(index=False))
print(g[g.memo.astype(str).str.contains('2D Deposit|Lease App',case=False)][C].to_string(index=False))
# last dates per bank account
bk=g[g.account.str.contains('Chase|Found|Paypal|Savings')]
print(bk.groupby('account').date.max())
