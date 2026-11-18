from common import *
f=pd.read_pickle('fl_typed.pkl')
pd.set_option('display.max_colwidth',120)
o=f[f.account.str.startswith('Due to/from owner')&(f.dt>='2026-01-01')].sort_values('dt')

# bank accounts
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings','Credit card','Paypal'))]

b=f[f.account.isin(banks)&(f.dt>='2026-01-01')].copy()
pat='CAPITAL ONE|5820|360 Checking|Petal|CITI|CHECK #|CHASE CREDIT CRD|APPLECARD|BK OF AMER|CREDIT ONE|0002|8965|3360|Tallerine'
m=b[b.Description.astype(str).str.contains(pat,case=False,regex=True)].copy()
print(len(m))
# pair with non-bank leg: same Source, dt, |amount|, description (strip trailing '.')
nb=f[~f.account.isin(banks)&(f.dt>='2026-01-01')].copy()
nb['k']=nb.Description.astype(str).str.rstrip('.').str.strip(); m['k']=m.Description.astype(str).str.rstrip('.').str.strip()
nb['abs']=nb.amount.abs().round(2); m['abs']=m.amount.abs().round(2)
res=[]
for i,r in m.iterrows():
    c=nb[(nb.Source==r.Source)&(nb['dt']==r['dt'])&(nb['abs']==r['abs'])&(nb.k==r.k)]
    res.append('; '.join(sorted(set(c.account))) if len(c) else 'NO MATCH')
m['other']=res; m['n']=1
m['kind']=np.select([m.k.str.contains('5820'),m.k.str.contains('CAPITAL ONE',case=False)&(m.amount<0),m.k.str.contains('CAPITAL ONE',case=False)&(m.amount>0),m.k.str.contains('Petal'),m.k.str.contains('CITI',case=False),m.k.str.contains('CHECK #'),m.k.str.contains('CHASE CREDIT CRD')],['to5820','CapOne out','CapOne in','Petal','Citi','Check','ChaseCC'],'other')
m.to_pickle('m.pkl')
print(m.groupby(['kind','other']).amount.agg(['sum','count']).to_string())
print(m[m.kind.isin(['other','Check','Citi','ChaseCC','CapOne in'])].sort_values('dt')[['account','dt','amount','k','other']].to_string(index=False))
