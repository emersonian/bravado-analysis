import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',75); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
pat='(?i)mastercard payment|citi card|citi autopay|bk of amer|applecard|capital one (mobile|online)|capital one orig|credit one|chase card ending|ending 8965|in 8965|petal'
isbank=q.account.str.contains(r'Chase, Checking|Chase Checking|Chase Savings|Found')
for Y in [2025]:
    b=q[(q.yr==Y)&~isbank&q.split.fillna('').str.contains(r'Chase, Checking|Chase Checking|Chase Savings|Found')&q.memo.fillna('').str.contains(pat)]
    b=b.assign(m=b.memo.str.replace('ORIG CO NAME:','').str.slice(0,60))
    print(b.groupby('account').amount.agg(['sum','count']).round(2).to_string())
    print(b[~b.account.str.contains("Jeremiah|Jer")][['date','account','name','m','split','amount']].to_string())
