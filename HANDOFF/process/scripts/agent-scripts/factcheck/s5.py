import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',600)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
def bal(a,d):
    return round(bb.get(a,0)+q[(q.account==a)&(q.date<=d)].amount.sum(),2)
for a in ['33500 Due to Jeremiah','Due from Jer','Due from James',"53000 Jer's Draw","54000 James' Draw",'Wages Due to Jeremiah','Loan From Nguyen','33100 Anthony Tallerine LOC','Member Equity - Coinbase','Member Equity - Nguyen','Member Equity - Clark','Member Equity - Tallerine','Member Equity - Nelson','Loan From Mark Clark','Debt to Equity - Hugh and Christy Nguyen','SBA Disaster Loan']:
    print(a, {d:bal(a,d) for d in ['2022-12-31','2023-12-31','2024-12-31','2025-12-31','2026-03-27']})
print(q[q.account=="53000 Jer's Draw"].groupby('yr').amount.sum().round(2))
n=q[q.account=='Loan From Nguyen']
print(n[['date','type','num','name','memo','split','amount','running_balance']].to_string())
t=q[q.account=='33100 Anthony Tallerine LOC']
print(t[t.date>='2024-01-01'][['date','type','num','name','memo','split','amount','running_balance']].to_string())
c=q[q.account=='Member Equity - Coinbase']
print(c[['date','type','num','name','memo','split','amount','running_balance']].to_string())
