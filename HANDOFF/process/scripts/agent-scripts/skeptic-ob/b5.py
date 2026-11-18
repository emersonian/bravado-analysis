from common import *
f=fl()
typ=pd.read_pickle('bstyp.pkl').to_dict()
inc_pat=['Sales - ','Gift wrap','Shipping income','Fulfillment services reimbursement','Inventory reimbursement','Interest income','Cashback','Money-in','Money received','Foreign Exchange']
def t(a):
    if a in typ: return typ[a]
    return 'I' if any(a.startswith(p) or p in a for p in inc_pat) and not a.startswith('Sales commissions') else 'X'
f['t']=f.account.map(t)
f['dr']=np.where(f.t.isin(['A','X']),f.amount,-f.amount)
f.to_pickle('fl_typed.pkl')
print(f[f.t=='I'].account.unique())
pl=f[f.t.isin(['I','X'])]
print('PL total (inc - exp):', round(-pl.dr.sum(),2))
print('total dr-cr:', round(f.dr.sum(),2))
f['day']=f.dt.dt.date
d=f.groupby('day').dr.sum().round(2); print(d[d!=0])
f['mon']=f.dt.dt.to_period('M')
print(f.groupby('mon').dr.sum().round(2))
# opening
op=f[f.dt<'2026-01-01']
print('opening A,L,E:',op.groupby('t').amount.sum().round(2).to_dict(), 'dr',round(op.dr.sum(),2))
for cut in ['2026-07-22 23:59:59','2026-07-23 23:59:59']:
    c=f[f.dt<=cut]; p=c[c.t.isin(['I','X'])&(c.dt>='2026-01-01')]
    print(cut,'PL',round(-p.dr.sum(),2),'A-L-E',round(c[c.t=='A'].amount.sum()-c[c.t=='L'].amount.sum()-c[c.t=='E'].amount.sum(),2), 'n after 7/22', len(f[f.dt>'2026-07-22 23:59:59']))
c=f[f.dt<'2026-07-22']; p=c[c.t.isin(['I','X'])&(c.dt>='2026-01-01')]
print('<7/22 00:00 PL',round(-p.dr.sum(),2),'A-L-E',round(c[c.t=='A'].amount.sum()-c[c.t=='L'].amount.sum()-c[c.t=='E'].amount.sum(),2))
