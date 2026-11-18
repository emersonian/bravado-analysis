from common import *
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv').set_index('Account')['Ending Balance']; pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
names=pl.Account.tolist(); v=pl['Year Total'].tolist()
def rng(a,b): 
    i,j=names.index(a),names.index(b); return sum(v[i:j+1])
inc=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale')
contra=rng('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart')
cost=rng('Cost of goods sold - Amazon Bravado Spice - United States','Inventory reimbursement - Amazon Bravado Spice - United States')
opex=rng('Bad debt','R&D expenses')
oi=rng('Interest income','Interest income')+rng('Auto-class in progress - Money received','Money-in')
oe=rng('Bank charges & fees','Interest & financing fees')+rng('Auto-class in progress - Money spent','Money-out')
print(inc,contra,cost,opex,oi,oe)
print('net',inc-contra-cost-opex+oi-oe)
# from GL by date, with sign map
sign={}
for n in names:
    i=names.index(n)
    sign[n]= 1 if (i<=names.index('Shipping income - Wholesale') or n in ['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']) else -1
plg=f[f.account.isin(names)].copy(); plg['s']=plg.account.map(sign)*plg.amount
print('net all',plg.s.sum(),'thru Jul22',plg[plg.dt<'2026-07-23'].s.sum(),'thru Jun30',plg[plg.dt<'2026-07-01'].s.sum())
print(plg.groupby(plg.dt.dt.to_period('M')).s.sum())
# balance sheet route
assets=list(bs.index[:bs.index.get_loc('Equipment - depreciation')+1])
liab=list(bs.index[bs.index.get_loc('Credit card - Chase - UnitedSM Explorer Card 5839'):bs.index.get_loc('Long-term loan payable - Small Business Administration')+1])
eq=list(bs.index[bs.index.get_loc('Retained earnings'):])
A,L,E=bs[assets].sum(),bs[liab].sum(),bs[eq].sum()
print('A',A,'L',L,'E',E,'implied NI',A-L-E)
# balance check per date: assets - liab - eq - NI should be zero each day
bsg=f[f.account.isin(bs.index)].copy(); bsg['s']=bsg.account.map(lambda a: 1 if a in assets else -1)*bsg.amount
d=pd.concat([bsg[['dt','s']],plg.assign(s=-plg.s)[['dt','s']]])
dd=d.groupby(d.dt.dt.date).s.sum(); dd=dd[dd.abs()>0.005]; print(dd.to_string()); print(dd.sum())
