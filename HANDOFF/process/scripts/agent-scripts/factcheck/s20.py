import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',100); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings'))]
b=f[f.account.isin(banks)]
w=b[(b.dt>='2026-04-27')&(b.dt<'2026-05-08')&(b.amount.abs()>=300)].sort_values('dt')
print(w[['dt','account','amount','Description']].to_string())
print('benthall/blake/coinbase/usdc/solana/comatri mentions:')
m=f[f.Description.fillna('').str.contains('(?i)benthall|blake|coinbase|usdc|solana|comatri|kraken|crypto')]
print(m[['dt','account','amount','Description']].to_string())
print('SBA payments'); m=b[b.Description.fillna('').str.contains('(?i)sba')]; print(m[['dt','account','amount','Description']].to_string())
print('inflows >= 1000 not sales, Jan-Jul'); 
m=b[(b.amount>=2000)&~b.Description.fillna('').str.contains('(?i)shopify|amazon|faire|kehe|transfer from|found orig|stripe|paypal')].sort_values('dt'); print(m[['dt','account','amount','Description']].to_string())
# liabilities accounts list
print(sorted([a for a in f.account.unique() if re.search('(?i)loan|payable|line of credit|note',a)]))
