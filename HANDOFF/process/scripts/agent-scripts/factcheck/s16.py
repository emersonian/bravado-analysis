import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
s=q[q.account.str.contains('Spark')]
print(s.groupby('yr').amount.agg(['sum','count']).round(2)); print(s[s.yr>=2024][['date','type','name','memo','split','amount','running_balance']].tail(12).to_string())
# 2025 two mastercard payments bank fees
t=q[(q.yr==2025)&(q.account=='73410 Bank Fees')&(q.name=='Mastercard Payment')]
print(t[['date','memo','split','amount']].to_string())
# 2025 JE legs for itemized entries
je=q[(q.yr==2025)&(q.account=='33500 Due to Jeremiah')&(q.type=='Journal Entry')&(q.amount>0)]
nums=je.num.tolist()
legs=q[q.num.isin(nums)&(q.yr==2025)&(q.account!='33500 Due to Jeremiah')]
print(legs.groupby('account').amount.agg(['sum','count']).round(2).sort_values('sum',ascending=False).to_string())
print(len(nums), je.amount.sum().round(2))
for n in ['AJE-406','AJE-506','AJE-540','AJE-546']:
    print(q[q.num==n][['account','date','memo','amount']].assign(memo=lambda d:d.memo.str.slice(0,90)).to_string())
