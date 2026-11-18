from ld import *
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
names=list(pl.Account)
i=lambda s: names.index(s)
sales=names[:i('Discounts & promotions - Amazon Bravado Spice - United States')]
contra=names[i('Discounts & promotions - Amazon Bravado Spice - United States'):i('Cost of goods sold - Amazon Bravado Spice - United States')]
cogs=[n for n in names if n.startswith('Cost of goods sold')]
ful=names[i('External stores Fulfillment fees - Amazon Bravado Spice - United States'):i('Bad debt')]
T=pl.set_index('Account')['Year Total']
print('gross sales',T[sales].sum().round(2),'contra',T[contra].sum().round(2),'net',(T[sales].sum()-T[contra].sum()).round(2))
print('product COGS',T[cogs].sum().round(2),'fulfil/shipping/selling fees',T[ful].sum().round(2)); print(ful)
net=T[sales].sum()-T[contra].sum()
print('GM product only', round(1-T[cogs].sum()/net,4), 'GM incl fulfil+fees', round(1-(T[cogs].sum()+T[ful].sum())/net,4))
p=f[f.datetime_utc>='2026-01-01'].copy(); p['m']=p.datetime_utc.dt.to_period('M')
ms=p[p.account.isin(sales)].groupby('m').amount.sum()-p[p.account.isin(contra)].groupby('m').amount.sum()
mc=p[p.account.isin(cogs)].groupby('m').amount.sum(); mf=p[p.account.isin(ful)].groupby('m').amount.sum()
print(pd.DataFrame({'net_sales':ms,'prod_cogs':mc,'fulfil_fees':mf}).round(0).to_string())
print('Jan-Jul23 net sales',ms.sum().round(2),' Jan-Jun',ms[:6].sum().round(2), 'avg/mo Jan-Jun', (ms[:6].sum()/6).round(0))
# QB
inc=[a for a in q.account.unique() if a[:2] in ('61','63','64','65','66','67') or a in ('Sales of Product Income','Shipping Income','Discounts given','Uncollectible Sales','Marketing Allowance','On-Invoice Discounts','Shipping/Transit Discounts','Spoilage Allowance','Swell Discount','Expiration Allowance','Free fill','Remittance Discrepancy')]
x=q[q.account.isin(inc)&(q.y>=2024)]
print(x.groupby(['y','account']).amount.sum().round(0).to_string())
