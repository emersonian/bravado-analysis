import pandas as pd, sys
pd.set_option('display.width',260); pd.set_option('display.max_colwidth',75); pd.set_option('display.max_rows',2000)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date'])
T=["33500 Due to Jeremiah","Due from Jer","53000 Jer's Draw","Wages Due to Jeremiah","Member Equity - Tallerine","Due from James","54000 James' Draw","Member Equity - Nelson"]
je=q[(q.account.isin(T))&(q.type=='Journal Entry')].sort_values(['date','num'])
je['memo']=je.memo.astype(str).str[:75]
je['d']=je.date.dt.strftime('%Y-%m-%d')
je['account']=je.account.str[:22]
print(je[['account','d','num','memo','amount']].to_string(index=False))
