from common import *
pd.set_option('display.max_colwidth',70)
x=g[(g.account=='12000 Accounts Receivable')&(g.date>='2026-01-01')]
print(x.groupby('type').amount.agg(['sum','count']))
print('blank names',(x.name=='').sum(),len(x))
print(x.groupby(['name','type']).amount.sum().unstack().fillna(0).to_string())
# 12/31/2025 open AR by customer (name-based)
y=g[(g.account=='12000 Accounts Receivable')&(g.date<='2025-12-31')]
c=y.groupby('name').amount.sum(); c=c[c.abs()>1].sort_values(); print(c.to_string()); print(c.sum())
for a in ['Cash payments received for store orders','Accounts receivable (A/R)','Unidentified payouts & transfers','Sales - Other','Accounts receivable (A/R) - Shopify - bravado-spice']:
    z=f[f.account==a].sort_values('dt'); print('\n##',a,len(z),z.amount.sum())
    print(z.assign(Source=z.Source.str[:40],Description=z.Description.str[:60])[['dt','amount','Source','Description']].head(30).to_string())
