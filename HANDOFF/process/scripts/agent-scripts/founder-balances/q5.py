import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False); q['date']=pd.to_datetime(q['date'])
def show(x):
    for _,r in x.sort_values('date').iterrows():
        print(f"{r.date.date()}|{r.account[:28]}|{r.type[:14]}|{str(r.num)[:16]}|{str(r['name'])[:25]}|{str(r.memo)[:110]}|{str(r.split)[:28]}|{r.amount:.2f}")
for a in ['Loan From Nguyen','SBA Disaster Loan','33100 Anthony Tallerine LOC','Member Equity - Coinbase','Member Equity - Nguyen','Member Equity - Clark','Debt to Equity - Hugh and Christy Nguyen','Loan From Mark Clark']:
    print('=====',a); show(q[q.account==a])
print('===== 2026 founder accts'); show(q[(q.date>='2026-01-01')&q.account.isin(["33500 Due to Jeremiah","Due from Jer","53000 Jer's Draw","Wages Due to Jeremiah"])])
print('===== 2026 QB rows mentioning capital one / 5820 / check 7588/7590 / SBA')
x=q[(q.date>='2026-01-01')&(q.memo.astype(str).str.contains('CAPITAL ONE|5820|7588|7590|SBA|EIDL|Lease App',case=False)|q['name'].astype(str).str.contains('SBA|Small Business',case=False))]
show(x)
