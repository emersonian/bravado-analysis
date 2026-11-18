import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
x=f[(f.datetime_utc.str.startswith('2025-12-31'))&(f.account.str.contains('owner|Payroll payable|James|Line of credit|Nguyen|Capital -',case=False,na=False))]
for _,r in x.iterrows():
    print(r.account,'|',r.datetime_utc,'|',r.amount,'|',r.Source,'|',str(r.Description)[:400],'|',r['Transaction Classification']); print()
# Blake 7500 loan check
y=f[(f.amount.abs().isin([7500.0,8500.0]))]
print(y[['account','datetime_utc','amount','Source','Description']].to_string())
