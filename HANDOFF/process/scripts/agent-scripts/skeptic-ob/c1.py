from common import *
f=pd.read_pickle('fl_typed.pkl'); g=qb()
pd.set_option('display.max_colwidth',110)
C=['account','dt','amount','Source','Description']
x=f[(f.dt>='2026-01-01')&(f.amount.abs().round(2).isin([7500,7400,8500,7499,7600,7399,7401,7450,7300,7000,1000.0+7500]))]
print('amount hits',len(x)); print(x[C].to_string())
kw='USDC|Coinbase|Benthall|Comatri|Blake|crypto|Solana|Circle|Kraken|Binance|wallet|Phantom|bridge'
for col in ['Description','Source','account','Transaction Classification']:
    x=f[f[col].astype(str).str.contains(kw,case=False,regex=True)]
    print(col,len(x)); print(x.groupby(['account','Source']).amount.agg(['sum','count']).head(20).to_string()); print(x[C].head(12).to_string())
# liabilities list
typ=pd.read_pickle('bstyp.pkl')
print([a for a,t in typ.items() if t=='L'])
# inbound bank >=1000 Apr 25 - May 31
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings','Paypal'))]
x=f[f.account.isin(banks)&(f.dt>='2026-04-20')&(f.dt<'2026-06-15')&(f.amount>=500)]
print(x.sort_values('dt')[C].to_string())
# QB
for col in ['memo','name','account','split']:
    x=g[(g.date>='2026-01-01')&g[col].astype(str).str.contains(kw,case=False,regex=True)]
    print('QB',col,len(x)); print(x[['account','date','name','memo','amount']].head(10).to_string())
x=g[(g.date>='2026-01-01')&(g.amount.abs().round(2).isin([7500,7400,8500]))]; print('QB amt',len(x)); print(x[['account','date','name','memo','amount']].to_string())
print([a for a in g.account.unique() if 'Coinbase' in a or 'Benthall' in a or 'Blake' in a or 'Comatri' in a])
