import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
# Jer's draw 2025 lines
t=q[(q.account=="53000 Jer's Draw")&(q.yr==2025)]; print(t[['date','memo','amount']].to_string())
# audit log AJE-547
import glob,csv
for p in glob.glob('/home/user/bravado-analysis/Financials/Quickbooks/Audit Log - 2026.csv'):
    a=pd.read_csv(p,low_memory=False,dtype=str)
    print(a.columns.tolist())
    m=a[a.apply(lambda r: r.astype(str).str.contains('AJE-547|69,033|69033').any(),axis=1)]
    print(m.to_string()[:3000])
