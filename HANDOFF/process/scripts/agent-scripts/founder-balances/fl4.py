exec(open('fl.py').read())
b=bs.set_index('Account')['Ending Balance']
t=pd.Series({a:typ(a) for a in b.index})
A=b[t=='A'].sum(); L=b[t=='L'].sum(); E=b[t=='E'].sum()
p=pl.set_index('Account')['Year Total']; tp=pd.Series({a:typ(a) for a in p.index})
NI=p[tp=='I'].sum()-p[tp=='X'].sum()
print('BS index: A',round(A,2),'L',round(L,2),'E',round(E,2),'A-L-E',round(A-L-E,2),'P&L index NI',round(NI,2),'gap',round(A-L-E-NI,2))
g=f[f.dt>='2026-01-01']
ni_gl=g[g.typ=='I'].amount.sum()-g[g.typ=='X'].amount.sum(); print('GL NI 2026',round(ni_gl,2))
print('latest dates:', f.dt.max(), f[f.typ.isin(['A','L','E'])].dt.max())
# monthly balance of owner accounts
for a in ['Due to/from owner - non-interest balance - Jeremiah Tallerine','Distributions - Jeremiah Tallerine','Reimbursements to owners','Capital - Jeremiah Tallerine','Payroll payable']:
    x=f[f.account==a]; print(a); print(x.groupby(x.dt.dt.to_period('M')).amount.sum().round(2).to_string())
pp=f[(f.account=='Payroll payable')]
print(pp.groupby([pp.Source.astype(str),pp.Description.astype(str).str[:45]],dropna=False).amount.agg(['sum','count']).round(2).to_string())
print(pp.amount.sum())
