import pandas as pd, re
pd.set_option('display.width',330); pd.set_option('display.max_colwidth',95); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings'))]
b=f[f.account.isin(banks)].copy()
b['d']=b.Description.fillna('').str.replace(r'ORIG CO NAME:','',regex=True).str.slice(0,95)
pat=r'(?i)5820|360 checking|capital one|citi|petal|apple ?card|applecard|credit one|bk of amer|bank of america|onemain|chase credit|check #|epay'
m=b[b.Description.fillna('').str.contains(pat)].sort_values('dt')
m['acct']=m.account.str.extract(r'(\d{4})$')
print(m[['dt','acct','amount','d','Transaction Classification']].to_string())
