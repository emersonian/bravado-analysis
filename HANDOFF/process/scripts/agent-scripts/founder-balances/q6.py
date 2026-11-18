import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False); q['date']=pd.to_datetime(q['date'])
def show(x):
    for _,r in x.sort_values('date').iterrows():
        print(f"{r.date.date()}|{r.account[:30]}|{r.type[:18]}|{str(r.num)[:12]}|{str(r['name'])[:25]}|{str(r.memo)[:120]}|{str(r.split)[:28]}|{r.amount:.2f}")
print('--- Nguyen 2024-2026'); show(q[(q.date>='2024-01-02')&(q['name'].astype(str).str.contains('Nguyen',case=False)|q.memo.astype(str).str.contains('NGUYEN',case=False))])
print('--- Anthony / Tallerine named rows 2024+'); show(q[(q.date>='2024-01-01')&(q['name'].astype(str).str.contains('Anthony|Veronica',case=False)|q.memo.astype(str).str.contains('ANTHONY TALL|VERONICA',case=False))])
print('--- last date per QB bank account'); 
for a in ['11200 Chase Checking 5189','Chase, Checking ...8733','1862 Found Chase Bank','11100 Chase Savings 3580']:
    x=q[q.account==a]; print(a, x.date.max().date(), len(x[x.date>='2026-01-01']))
print('--- SBA payments in QB (any year)'); show(q[q.memo.astype(str).str.contains('SBA EIDL|SBA LOAN',case=False)])
