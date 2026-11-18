import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',200)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
x=f[(f.amount.abs()>=7000)&(f.amount.abs()<=9000)&(f.datetime_utc>='2026-04-01')]
print(x[['account','datetime_utc','amount','Source','Description']].assign(Description=lambda d:d.Description.astype(str).str.slice(0,110)).to_string(index=False))
y=f[f.Description.astype(str).str.contains('Benthall|Blake|Comatri',case=False)|f.account.str.contains('Benthall|Blake|Comatri',case=False,na=False)]
print(y[['account','datetime_utc','amount','Source','Description']].assign(Description=lambda d:d.Description.astype(str).str.slice(0,110)).to_string(index=False))
