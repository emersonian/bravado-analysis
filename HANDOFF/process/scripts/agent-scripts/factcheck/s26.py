import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',100); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings'))]
b=f[f.account.isin(banks)&(f.dt<'2026-07-23')]
m=b[b.Description.fillna('').str.contains(r'(?i)chase card ending|chase credit crd')]
m=m.assign(card=m.Description.str.extract(r'ending in (\d{4})')[0].fillna('EPAY'))
print(m.groupby('card').amount.agg(['sum','count']).round(2))
# counter classification for card 8965 lines
x=f[f.Description.fillna('').str.contains('ending in 8965')&~f.account.isin(banks)]
print(x.groupby(['account','Transaction Classification'],dropna=False).amount.agg(['sum','count']).round(2))
print(x.sort_values('dt')[['dt','account','amount','Description']].head(40).to_string())
# zelle/others to Jeremiah or Marisa
z=b[b.Description.fillna('').str.contains(r'(?i)zelle|venmo|cash app|wire')&(b.amount<0)]
print(z.assign(who=z.Description.str.extract(r'(?i)(?:to|transfer to) ([A-Za-z ]+?)(?: \d|\.|$)')[0]).groupby('who').amount.agg(['sum','count']).round(2).to_string())
