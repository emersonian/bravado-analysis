import pandas as pd, re
pd.set_option('display.width',330); pd.set_option('display.max_colwidth',110); pd.set_option('display.max_rows',900)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date']); q['yr']=q.date.dt.year
FA=['33500 Due to Jeremiah','Due from Jer',"53000 Jer's Draw",'Wages Due to Jeremiah']
for Y in [2025,2026]:
    t=q[q.account.isin(FA)&(q.yr==Y)].copy()
    cash=t[t.type!='Journal Entry'].copy()
    cash['m']=cash.memo.fillna('')
    def cls(m):
        ml=m.lower()
        if re.search(r'chase card ending|ending 8965|in 8965|citi|capital one (mobile|online) pmt|capital one orig|capitaL one orig|bk of amer|applecard|credit one|mastercard|one orig id|pmtsec',ml): return 'card'
        if re.search(r'0002|5820|bi-monthly|virtual card|mark clark',ml): return 'transfer'
        return 'other'
    cash['c']=cash.m.apply(cls)
    print(Y, cash.groupby(['c','type']).amount.agg(['sum','count']).round(2))
    print(cash[cash.c=='other'][['date','account','type','name','m','split','amount']].to_string())
    print(cash[(cash.c=='card')].assign(k=cash.m.str.extract(r'(?i)(chase card|8965|citi|capital one|bk of amer|applecard|credit one|mastercard)')[0].str.lower()).groupby('k').amount.agg(['sum','count']).round(2))
    je=t[t.type=='Journal Entry']
    print(je[['date','account','num','memo','amount']].assign(memo=je.memo.str.slice(0,90)).to_string())
    print('JE credits to 33500', je[(je.account=='33500 Due to Jeremiah')&(je.amount>0)].amount.sum().round(2))
    if Y==2025:
        jan=cash[(cash.date<='2025-01-31')]
        print(jan[['date','account','m','amount']].assign(m=jan.m.str.slice(0,80)).to_string())
