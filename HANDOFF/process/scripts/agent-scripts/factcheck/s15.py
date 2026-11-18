import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',120); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
t=q[(q.yr==2026)&(q.num.fillna('').isin(['7588','7590','7589'])|q.memo.fillna('').str.contains(r'(?i)7588|7590|lease app|whitenton|finnacle'))]
print(t[['account','date','type','num','name','memo','split','amount']].to_string())
t=q[(q.yr==2026)&(q.amount.abs().isin([3250.0,250.0]))&(q.date<='2026-02-05')]
print(t[['account','date','type','num','name','memo','split','amount']].to_string())
# 2025 mastercard payments expensed to bank fees
t=q[(q.yr==2025)&q.memo.fillna('').str.contains('(?i)mastercard payment|citi card|citi autopay|bk of amer|applecard|capital one (mobile|online)|credit one|chase card ending')&~q.account.isin(['33500 Due to Jeremiah','Due from Jer',"53000 Jer's Draw",'Wages Due to Jeremiah'])&~q.account.str.contains('Chase|Checking|Savings')]
print(t[['account','date','type','name','memo','split','amount']].to_string())
# QB 2026: all bank lines to personal accts
b=q[(q.yr==2026)&q.account.str.contains('Chase|Checking|Savings')&q.memo.fillna('').str.contains(r'(?i)5820|capital one|citi|0002|petal|apple')]
print(b[['account','date','type','name','memo','split','amount']].assign(memo=b.memo.str.slice(0,70)).to_string())
print(q.date.max(), q[q.yr==2026].groupby(q.date.dt.month).size())
