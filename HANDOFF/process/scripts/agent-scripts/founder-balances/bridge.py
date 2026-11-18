import pandas as pd
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False); f['dt']=pd.to_datetime(f['datetime_utc'])
op=f[f.dt.dt.date==pd.Timestamp('2025-12-31').date()]
fo=op.groupby('account').amount.sum().round(2)
ASSET_PREFIX=('Accounts receivable','Checking','Savings','Paypal','Money in transit','Undeposited','Inventory','Prepaid','Due to/from owner','Related party balance','Other current assets','Equipment','Unidentified','Cash payments','Uncleared invoices')
def side(a):
    if a.startswith('Inventory vendors'): return 'L'
    if a.startswith(ASSET_PREFIX): return 'A'
    if a.startswith(('Capital','Distributions','Retained','Reimbursements to owners')): return 'E'
    return 'L'
s=pd.Series({a:side(a) for a in fo.index})
print('Finaloop opening: assets',round(fo[s=='A'].sum(),2),'liab',round(fo[s=='L'].sum(),2),'equity',round(fo[s=='E'].sum(),2),'A-L-E',round(fo[s=='A'].sum()-fo[s=='L'].sum()-fo[s=='E'].sum(),2))
for k in 'ALE':
    print(k); print(fo[s==k].to_string())
# QB
qbA={'cash 5189':698.43,'savings 3580':26.49,'found 1862':1254.77,'chase 8733':1166.39,'AR':17586.74,'prepaid':2377.09,'inventory':3308.41+7740.87+41533.86+5360.85,'due from james':56368.76,'due from jer':75440.62,'equip':1319.56,'accdep':-1319.56}
print('QB assets',round(sum(qbA.values()),2))
