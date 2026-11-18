from common import *
pd.set_option('display.max_colwidth',80)
bank=[a for a in f.account.unique() if a.startswith(('Checking','Savings','Paypal','Credit card'))]
x=f[f.account.isin(bank)&(f.dt>='2026-04-20')&(f.dt<'2026-05-20')&(f.amount.abs()>=300)].sort_values('dt')
print(x[['account','dt','amount','Source','Description','Transaction Classification']].assign(account=x.account.str[:28],Source=x.Source.str[:30]).to_string())
print('--- 7500/8500 any')
a=f.amount.abs().round(2)
print(f[a.isin([7500,8500,1000.0,2900.0,4600.0])&(f.dt>='2026-04-01')][['account','dt','amount','Source','Description']].to_string())
pat='blake|benthall|usdc|coinbase|solana|crypto|comatri|kraken|gemini|binance|wire|zelle|venmo'
m=f.Description.str.contains(pat,case=False)|f.Source.str.contains(pat,case=False)|f.account.str.contains(pat,case=False)
print(f[m].groupby(['account']).amount.agg(['sum','count']))
print(f[m&~f.account.str.contains('Capital - Blake')][['account','dt','amount','Source','Description']].head(40).to_string())
print('--- capital one inflows/outflows')
m=f.Description.str.contains('capital one|5820|360 checking',case=False)
print(f[m].sort_values('dt')[['account','dt','amount','Description']].assign(account=f.account.str[:40]).to_string())
