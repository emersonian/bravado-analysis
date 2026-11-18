import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',300)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
x=f[f.account.str.contains('Ondeck',case=False,na=False)]
print(x.groupby('account').amount.agg(['sum','count']))
print(x[['account','datetime_utc','amount','Description']].assign(Description=lambda d:d.Description.astype(str).str.slice(0,70)).sort_values('datetime_utc').tail(8).to_string(index=False))
x=f[f.account.str.contains('Capital - Blake|Capital - Jeremiah|Distributions',case=False,na=False)]
print(x.groupby('account').amount.agg(['sum','count']))
# Capital One transfers in 2026
y=f[f.Description.astype(str).str.contains('CAPITAL ONE',case=False)&(f.account.str.startswith('Checking'))]
print(y[['account','datetime_utc','amount','Description']].assign(Description=lambda d:d.Description.astype(str).str.slice(0,80)).sort_values('datetime_utc').to_string(index=False))
