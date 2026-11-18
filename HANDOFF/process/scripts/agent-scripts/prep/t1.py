from ld import *
# Q1: cash and AP
print('--- QB cash-like balances 12/31/2025 and 3/27/2026')
for a in ['11100 Chase Savings 3580','11200 Chase Checking 5189','Chase, Checking ...8733','1862 Found Chase Bank','11500 Cash on hand','Paypal','QuickBooks Checking Account','15000 Undeposited Funds']:
    print(a, round(bal(a,'2025-12-31'),2), round(bal(a,'2026-03-27'),2))
ap=q[q.account=='31000 Accounts Payable']
for asof in ['2024-12-31','2025-12-31','2026-03-27']:
    x=ap[ap.date<=asof]
    v=x.groupby(x['name'].fillna('(none)')).agg(bal=('amount','sum'),last=('date','max'),lastbill=('date',lambda s: s[x.loc[s.index,'amount']>0].max())).round(2)
    v=v[v.bal.abs()>0.5].sort_values('bal',ascending=False)
    print('\n--- QB A/P by vendor as of',asof,'total',round(v.bal.sum(),2), 'vendors',len(v))
    print(v.head(25).to_string())
    if asof=='2025-12-31':
        v['age']=pd.cut((pd.Timestamp(asof)-v.lastbill).dt.days,[-1,90,180,365,10000],labels=['<=90d','91-180d','181-365d','>365d'])
        print(v.groupby('age',observed=False).bal.agg(['sum','count']).round(2))
# Finaloop cash and AP at end
fb=f.groupby('account').amount.sum()
cash=[a for a in fb.index if a.startswith(('Checking','Savings','Paypal','Money in transit','Undeposited'))]
print('\n--- Finaloop cash-like at Jul 23 2026'); print(fb[cash].round(2).to_string()); print('checking+savings',round(fb[[a for a in cash if a.startswith(('Checking','Savings'))]].sum(),2))
for a in ['Inventory vendors - bills','Operational vendors - bills']:
    x=f[f.account==a]
    print('\n---',a,round(x.amount.sum(),2))
    x=x.assign(m=x.datetime_utc.dt.to_period('M'))
    print(x.groupby('m').amount.agg(['sum','count']).round(2).to_string())
    o=x[x.datetime_utc<'2026-01-01']
    print(o[['amount','Source','Description']].to_string())
    print(x[(x.datetime_utc>='2026-01-01')&(x.amount.abs()>2500)][['datetime_utc','amount','Source','Description']].to_string())
