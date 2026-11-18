import pandas as pd, sys
pd.set_option('display.width',280); pd.set_option('display.max_colwidth',70); pd.set_option('display.max_rows',1000)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date'])
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
T=["33500 Due to Jeremiah","Due from Jer","53000 Jer's Draw","Wages Due to Jeremiah","Member Equity - Tallerine","Due from James","54000 James' Draw","Member Equity - Nelson"]
rows=[]
for a in T:
    r={'acct':a,'open2020':bb.get(a,0)}
    for y in range(2019,2026):
        r[y]=round(bb.get(a,0)+q[(q.account==a)&(q.date<=f'{y}-12-31')].amount.sum(),2)
    r['2026-03-27']=round(bb.get(a,0)+q[(q.account==a)].amount.sum(),2)
    rows.append(r)
print(pd.DataFrame(rows).to_string())
# verify vs running_balance
for a in T:
    x=q[q.account==a]
    for y in range(2020,2026):
        xx=x[x.date<=f'{y}-12-31']
        if len(xx): print(a,y,'last running_balance in file order:',xx.iloc[-1].running_balance, xx.iloc[-1].date.date())
# activity by year
for a in T:
    x=q[q.account==a]
    print(a); print(x.groupby([x.date.dt.year,'type']).amount.agg(['sum','count']).round(2))
