exec(open('fl.py').read())
g=f[f.dt>='2026-01-01'].copy()
BANK=g.account.str.startswith(('Checking','Savings','Credit card','Paypal'))
b=g[BANK].copy(); d=b.Description.astype(str)
def tot(mask,label):
    x=b[mask]; print(label, round(x.amount.sum(),2), len(x), x.dt.min().date() if len(x) else None, x.dt.max().date() if len(x) else None)
tot(d.str.contains('Transfer fee for Transfer to 360 Checking'),'fees 5820')
tot(d.str.contains('CITI'),'citi')
tot(d.str.contains('CHASE CREDIT CRD'),'chase credit crd epay')
tot(d.str.contains(r'5820')&~d.str.contains('Transfer fee'),'all transfers to 5820')
tot(d.str.contains(r'CAPITAL ONE (ONLINE|MOBILE) PMT|ORIG CO NAME:CAPITAL ONE'),'capital one card pmts')
tot(d.str.contains('Petal'),'petal')
tot(d.str.contains('CHECK # 7590'),'chk 7590'); tot(d.str.contains('CHECK # 7588'),'chk 7588')
tot(d.str.contains('STATE FARM'),'state farm')
# non-bank legs for chase credit crd
nb=g[~BANK]; x=nb[nb.Description.astype(str).str.contains('CHASE CREDIT CRD|CITI|STATE FARM|7588')&~nb.account.isin(['Money-out','Money-in'])]
print(x.groupby(['account',x.Description.astype(str).str[:22]]).amount.agg(['sum','count']).round(2).to_string())
# Money-out net by description (unclassified residual)
mo=g[g.account=='Money-out']; r=mo.groupby(mo.Description.astype(str).str.rstrip('. ').str[:70]).amount.sum().round(2); print(r[r.abs()>0.01].to_string())
# last gusto dates
gu=g[g.Source.astype(str).str.contains('Gusto',case=False)]; print('last gusto',gu.dt.max(), gu[gu.account=='Salaries & wages (via Gusto)'].dt.max())
# personal charges sum and healthcare share
o=g[(g.account.str.startswith('Due to/from owner'))&(g.amount>0)]; print('personal +',round(o.amount.sum(),2),len(o))
hc=o[o.Description.str.contains('TALKIATRY|THERAPY|PHARMACY',case=False)]; print('healthcare',round(hc.amount.sum(),2),len(hc))
print('owner acct bal by date:'); oo=f[f.account.str.startswith('Due to/from owner')].sort_values('dt'); print(round(oo.amount.sum(),2), oo.dt.max())
