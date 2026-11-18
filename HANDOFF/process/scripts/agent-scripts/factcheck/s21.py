import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',100); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
t=q[(q.account=='Due from James')&(q.date>='2023-07-01')]
print(t[['date','type','num','memo','split','amount','running_balance']].to_string())
t=q[(q.account=='Member Equity - Nelson')|(q.account=="54000 James' Draw")]
print(t[t.date>='2023-12-01'][['account','date','type','num','memo','split','amount','running_balance']].to_string())
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
for a in ['Loan payable - American Express','Loan payable - Ondeck Capital','Loan payable - Shopify Capital','Long-term loan payable - Small Business Administration','Credit card - Shopify Credit']:
    t=f[f.account==a].copy(); t['M']=t.datetime_utc.str.slice(0,7)
    print(a, round(t.amount.sum(),2)); print(t.groupby('M').amount.sum().round(2).to_dict())
# P&L net through Jul 22 not needed. A/R at 12/31/2025 in QB
ar=q[q.account.str.contains('Accounts Receivable',case=False)]
print(ar.groupby('account').amount.sum().round(2), ar[ar.date<='2025-12-31'].amount.sum().round(2))
