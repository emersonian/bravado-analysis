from common import *
f=pd.read_pickle('fl_typed.pkl'); g=qb()
pd.set_option('display.max_colwidth',130)
x=f[f.Description.astype(str).str.contains('ACCTVERIFY|ACCT VERIFY|VERIFY',case=False)&f.account.str.startswith(('Checking','Savings'))]
print(x.sort_values('dt')[['account','dt','amount','Description']].to_string(index=False))
# Found account: first rows / earliest date, inbound from capital one any wording
x=f[f.account.str.startswith(('Checking','Savings'))&(f.amount>0)&f.Description.astype(str).str.contains('capital one|360|5820',case=False)]
print(x.sort_values('dt')[['account','dt','amount','Description']].to_string(index=False))
# QB all-time entries of exactly 7500/8500 after 2026-01-01 none; show count overall for context
print('QB rows abs 7500/7400/8500 all years:', len(g[g.amount.abs().round(2).isin([7500,7400,8500])]), 'max date', g[g.amount.abs().round(2).isin([7500,7400,8500])].date.max())
# Mark 2024 check
print(-294662.76-(-301103), 859316.56-865758)
