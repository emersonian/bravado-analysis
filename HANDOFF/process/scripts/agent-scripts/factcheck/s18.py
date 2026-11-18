import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',110); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
t=q[q.name.fillna('').str.contains('(?i)nguyen')|q.memo.fillna('').str.contains('(?i)nguyen')]
print(t[['account','date','type','num','name','memo','split','amount']].assign(memo=t.memo.fillna('').str.slice(0,80)).to_string())
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
t=f[f.Description.fillna('').str.contains('(?i)nguyen|frost bank')|f.account.str.contains('Nguyen')]
print(t[['account','datetime_utc','amount','Source','Description']].to_string())
t=f[f.account.str.contains('Tallerine')&f.account.str.contains('Line of credit')]; print(t[['account','datetime_utc','amount','Source','Description']].to_string())
t=f[f.Description.fillna('').str.contains('(?i)veronica|anthony')]; print(t[['account','datetime_utc','amount','Source','Description']].to_string())
print(f[f.account=='Bad debt'][['datetime_utc','amount','Source','Description']].to_string())
