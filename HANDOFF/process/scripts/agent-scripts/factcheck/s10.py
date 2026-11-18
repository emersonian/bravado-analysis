import pandas as pd, re
pd.set_option('display.width',330); pd.set_option('display.max_colwidth',100); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
FA=['33500 Due to Jeremiah','Due from Jer',"53000 Jer's Draw",'Wages Due to Jeremiah']
t=q[q.account.isin(FA)&(q.yr>=2025)].copy()
t['m']=t.memo.fillna('').str.replace('ORIG CO NAME:','').str.slice(0,100)
t['a']=t.account.str.slice(0,12)
print(t[['date','a','type','num','name','m','split','amount']].to_string())
