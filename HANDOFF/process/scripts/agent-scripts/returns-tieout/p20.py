import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',300)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
x=f[(f.datetime_utc>='2026-04-24')&(f.datetime_utc<'2026-05-08')&(f.amount.abs()>=1000)]
print(x[['account','datetime_utc','amount','Source','Description','Transaction Classification']].assign(Description=lambda d:d.Description.astype(str).str.slice(0,90)).sort_values('datetime_utc').to_string(index=False))
