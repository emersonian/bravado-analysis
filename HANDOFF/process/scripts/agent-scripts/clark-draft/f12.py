import pandas as pd, sys
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str)
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv'); p=list(pl.Account)
def rng(a,b): return p[p.index(a):p.index(b)+1]
inc=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale'); con=rng('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart')
cos=rng('Cost of goods sold - Amazon Bravado Spice - United States','Inventory reimbursement - Amazon Bravado Spice - United States')
opx=rng('Bad debt','R&D expenses'); oi=['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']; oe=['Bank charges & fees','Foreign Exchange Gain or Loss','Interest & financing fees','Auto-class in progress - Money spent','Reconciliation discrepancies','Money-out']
for cut in ['2026-06-30','2026-07-22','2026-07-23']:
    x=f[(f.d<=cut)&(f.d>'2025-12-31')].groupby('account').amount.sum()
    s=lambda a: x.reindex(a).fillna(0).sum()
    net=s(inc)-s(con); op=net-s(cos)-s(opx); ni=op+s(oi)-s(oe)
    print(cut,'net rev',round(net,2),'cos',round(s(cos),2),'opex',round(s(opx),2),'op loss',round(op,2),'other inc',round(s(oi),2),'other exp',round(s(oe),2),'NI',round(ni,2), 'PYA',round(s(['Prior year adjustment']),2),'bad debt',round(s(['Bad debt']),2))
