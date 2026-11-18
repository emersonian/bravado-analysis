import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',70); pd.set_option('display.max_rows',500)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
q=pd.read_csv(D+'qb_gl.csv',low_memory=False)
q['date']=pd.to_datetime(q['date'])
q['yr']=q.date.dt.year
print(q.dtypes)
accts=sorted(q.account.dropna().unique())
for a in accts:
    if any(k in a.lower() for k in ['jer','james','wage','salar','payroll','nguyen','tallerine','equity','clark','coinbase','due','loan','note']):
        print(a)
