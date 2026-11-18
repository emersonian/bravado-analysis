import pandas as pd, sys, itertools
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',130)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
c=['account','datetime_utc','amount','Source','Description','Transaction Classification']
print('--- 7500/8500 amounts'); print(f[f.amount.abs().isin([7500,8500,7400,7600])][c].to_string())
print('--- Blake/USDC/coinbase/solana/crypto'); print(f[f.Description.astype(str).str.contains('blake|benthall|usdc|coinbase|solana|crypto|kraken|comatri',case=False)|f.Source.astype(str).str.contains('blake|benthall|coinbase|comatri',case=False)][c].to_string()[:3000])
print('--- amex'); x=f[f.Description.astype(str).str.contains('amex|american express',case=False)]; print(x.groupby(['account','Transaction Classification'],dropna=False).amount.agg(['sum','count'])); print(x[c].sort_values('datetime_utc').head(40).to_string())
print('--- nguyen/frost'); print(f[f.Description.astype(str).str.contains('nguyen|frost bank',case=False)][c].to_string()[:3000])
print('--- sba'); print(f[f.Description.astype(str).str.contains('sba',case=False)][c].to_string()[:3000])
print('--- tallerine loan accounts / loan taken'); print(f[f['Transaction Classification'].astype(str).str.contains('Loan taken|loan',case=False)].groupby(['account','Transaction Classification']).amount.agg(['sum','count']).to_string())
print('--- Other payroll deductions payable last dates'); x=f[f.account=='Other payroll deductions payable']; print(x.groupby('m').amount.sum().round(2)); 
x=f[f.account=='Payroll payable']; print(x.groupby('m').amount.sum().round(2)); print(x[x.amount.abs()>1500][c].to_string())
print('--- deposits Apr 28 - May 6 into bank accounts > 1000')
x=f[(f.d>='2026-04-28')&(f.d<='2026-05-06')&f.account.str.startswith('Checking')&(f.amount.abs()>=1000)]; print(x[c].sort_values('datetime_utc').to_string())
