from common import *
f=pd.read_pickle('fl_typed.pkl')
pd.set_option('display.max_colwidth',90)
banks=[a for a in f.account.unique() if a.startswith(('Checking','Savings','Credit card','Paypal'))]
b=f[f.account.isin(banks)&(f.dt>='2026-01-01')].copy()
nb=f[~f.account.isin(banks)&(f.dt>='2026-01-01')].copy()
for d in (b,nb):
    d['k']=d.Description.astype(str).str.rstrip('.').str.strip(); d['abs']=d.amount.abs().round(2)
pat='CAPITAL ONE|5820|360 Checking|Petal|CITI|CHECK #|CHASE CREDIT CRD|APPLECARD|BK OF AMER|CREDIT ONE|0002|8965|3360|Tallerine|ONEMAIN'
m=b[b.k.str.contains(pat,case=False,regex=True)].copy()
res=[]
for i,r in m.iterrows():
    c=nb[(nb.Source==r.Source)&(nb['dt']==r['dt'])&(nb['abs']==r['abs'])&(nb.k==r.k)]
    net=c.groupby('account').dr.sum().round(2); net=net[net!=0]
    res.append('; '.join(f'{a}' for a,v in net.items()) if len(net) else ('NO MATCH' if len(c)==0 else 'NETS ZERO'))
m['other']=res
m['kind']=np.select([m.k.str.contains('fee',case=False),m.k.str.contains('5820'),m.k.str.contains('CAPITAL ONE',case=False)&(m.amount<0),m.k.str.contains('CAPITAL ONE',case=False)&(m.amount>0),m.k.str.contains('Petal'),m.k.str.contains('CITI',case=False),m.k.str.contains('CHECK #'),m.k.str.contains('CHASE CREDIT CRD')],['fee','to5820','CapOne out','CapOne in','Petal','Citi','Check','ChaseCC'],'other')
m.to_pickle('m.pkl')
print(m.groupby(['kind','other']).amount.agg(['sum','count']).to_string())
print(m[m.kind.isin(['Check','Citi','ChaseCC','CapOne in','fee'])].sort_values(['kind','dt'])[['account','dt','amount','k','other']].to_string(index=False))
t=m[m.kind=='to5820']; print('to5820 total',t.amount.sum().round(2),len(t),t.dt.min(),t.dt.max())
print(t[~t.other.isin(['Distributions - Jeremiah Tallerine','Reimbursements to owners'])].sort_values('dt')[['account','dt','amount','k','other']].to_string(index=False))
print(m[m.kind=='other'].sort_values('dt')[['account','dt','amount','k','other']].to_string(index=False))
