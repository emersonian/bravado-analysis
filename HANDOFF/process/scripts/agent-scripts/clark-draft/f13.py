import pandas as pd, sys, re
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',120)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
x=f[f.account=='Reimbursements to owners'].copy()
def k(d):
    d=str(d)
    if 'Personal Checking 5820' in d or '360 Checking' in d: return 'transfer to personal checking 5820'
    if 'CAPITAL ONE' in d.upper(): return 'Capital One card payment'
    return 'other: '+d[:50]
x['k']=x.Description.map(k)
print(x.groupby('k').amount.agg(['sum','count']).round(2))
print(x[['datetime_utc','amount','Description','Transaction Classification']].sort_values('datetime_utc').to_string())
print(x['Transaction Classification'].value_counts(dropna=False))
