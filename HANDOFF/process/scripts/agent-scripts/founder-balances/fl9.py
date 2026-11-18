exec(open('fl.py').read())
for cut in ['2026-07-22 23:59:59','2026-07-23 23:59:59']:
    g=f[(f.dt>='2026-01-01')&(f.dt<=cut)]
    inc=g[g.typ=='I'].amount.sum(); exp=g[g.typ=='X'].amount.sum()
    pya=g[g.account=='Prior year adjustment'].amount.sum(); rto=g[g.account=='Reimbursements to owners'].amount.sum()
    print(cut,'NI',round(inc-exp,2),'excl prior-yr adj',round(inc-exp+pya,2),'reimb',round(rto,2))
    h=f[f.dt<=cut]; print('  A-L-E',round(h[h.typ=='A'].amount.sum()-h[h.typ=='L'].amount.sum()-h[h.typ=='E'].amount.sum(),2))
# P&L index NI
p=pl.set_index('Account')['Year Total']; tp=pd.Series({a:typ(a) for a in p.index}); print('index NI',round(p[tp=='I'].sum()-p[tp=='X'].sum(),2))
print(p[tp=='I'])
