import pandas as pd
pd.set_option('display.width',280); pd.set_option('display.max_colwidth',80); pd.set_option('display.max_rows',600)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
w=q[q.account=='Wages Due to Jeremiah']
print(w[['date','type','num','name','memo','split','amount','running_balance']].to_string())
print(w.groupby('yr').amount.sum().round(2), w.amount.sum().round(2))
print('positives by yr', w[w.amount>0].groupby('yr').amount.sum().round(2))
print('negatives by yr', w[w.amount<0].groupby('yr').amount.sum().round(2))
s=q[q.account=='73902 Salaries & Wages']
print(s.groupby('yr').amount.sum().round(2))
print(s.groupby(['yr','type']).amount.sum().round(2))
