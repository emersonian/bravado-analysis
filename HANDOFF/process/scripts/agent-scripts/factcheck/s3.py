import pandas as pd
pd.set_option('display.width',280); pd.set_option('display.max_colwidth',90); pd.set_option('display.max_rows',600)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
s=q[q.account=='73902 Salaries & Wages']
for y in [2023,2024,2025,2026]:
    t=s[s.yr==y]
    t2=t.assign(numk=t.num.fillna('NA').str.replace(r'\d+','#',regex=True), memok=t.memo.fillna('').str.slice(0,40).str.replace(r'\d+','#',regex=True))
    print(y); print(t2.groupby(['type','numk','memok']).amount.agg(['sum','count']).round(2).to_string())
print(s[(s.yr==2025)&(~s.num.fillna('').str.contains('Gusto'))][['date','type','num','name','memo','split','amount']].to_string())
print(s[(s.yr==2026)][['date','type','num','name','memo','split','amount']].to_string())
# AJE-547 all legs
print(q[q.num=='AJE-547'][['account','date','memo','amount']].to_string())
# Gusto 10/28/2024
print(q[(q.num=='Gusto')&(q.date=='2024-10-28')][['account','date','name','memo','amount']].to_string())
