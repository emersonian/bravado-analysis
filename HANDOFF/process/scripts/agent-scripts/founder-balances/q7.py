import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False); q['date']=pd.to_datetime(q['date'])
x=q[q.account=='Wages Due to Jeremiah'].sort_values('date'); x['run']=x.amount.cumsum().round(2)
for _,r in x.iterrows():
    print(f"{r.date.date()}|{r.type[:14]}|{str(r.num)[:10]}|{str(r['name'])[:20]}|{str(r.memo)[:95]}|{str(r.split)[:26]}|{r.amount:.2f}|{r.run}")
print(x.groupby([x.date.dt.year,x.type]).amount.sum())
x=q[(q.account=='33500 Due to Jeremiah')&(q.date>='2025-01-01')].sort_values('date'); x['run']=x.amount.cumsum().round(2)
print('33500 2025+ by split/type'); print(x.groupby([x.date.dt.year,x.type,x.split.astype(str).str[:30]]).amount.agg(['sum','count']).round(2).to_string())
