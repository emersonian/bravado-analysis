import pandas as pd
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',110); pd.set_option('display.max_rows',600)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc'],utc=True,format='mixed')
for a in ['Reimbursements to owners','Distributions - Jeremiah Tallerine','Capital - Jeremiah Tallerine','Capital - Blake Benthall']:
    t=f[f.account==a].sort_values('dt')
    print('=====',a,round(t.amount.sum(),2),len(t))
    print(t[['dt','amount','Source','Description','Transaction Classification']].to_string())
