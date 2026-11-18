from common import *
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv').set_index('Account')['Ending Balance']; pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv'); names=pl.Account.tolist()
assets=list(bs.index[:bs.index.get_loc('Equipment - depreciation')+1])
inc_last=names.index('Shipping income - Wholesale')
def run(flip):
    sign={n:(1 if (i<=inc_last or n in ['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']+flip) else -1) for i,n in enumerate(names)}
    x=f.copy()
    x['s']=0.0
    isbs=x.account.isin(bs.index)
    x.loc[isbs,'s']=x[isbs].account.map(lambda a: 1 if a in assets else -1)*x[isbs].amount
    x.loc[~isbs,'s']=-x[~isbs].account.map(sign)*x[~isbs].amount
    d=x.groupby(x.dt.dt.date).s.sum(); d=d[d.abs()>0.005]
    ni=(x[~isbs].account.map(sign)*x[~isbs].amount).sum()
    return ni,d
for flip in [[],['Fulfillment services reimbursement - Amazon Bravado Spice - United States','Fulfillment services reimbursement - Walmart'],['Inventory reimbursement - Amazon Bravado Spice - United States'],['Fulfillment services reimbursement - Amazon Bravado Spice - United States','Fulfillment services reimbursement - Walmart','Inventory reimbursement - Amazon Bravado Spice - United States']]:
    ni,d=run(flip); print(len(flip),'NI',round(ni,2),'imbalance',round(d.sum(),2),'days',len(d)); 
print(d.to_string())
flip=['Fulfillment services reimbursement - Amazon Bravado Spice - United States','Fulfillment services reimbursement - Walmart','Inventory reimbursement - Amazon Bravado Spice - United States']
sign={n:(1 if (i<=inc_last or n in ['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']+flip) else -1) for i,n in enumerate(names)}
p=f[f.account.isin(names)].copy(); p['s']=p.account.map(sign)*p.amount
print('thru cutoff',round(p.s.sum(),2),'thru Jul22',round(p[p.dt<'2026-07-23'].s.sum(),2),'thru Jun30',round(p[p.dt<'2026-07-01'].s.sum(),2))
print(f[(f.dt.dt.date==pd.Timestamp('2026-04-15').date())&(f.amount.abs().round(2)==160.52)][['account','dt','amount','Source','Description']].to_string())
for a in flip:
    z=f[f.account==a]; print(a, len(z), z.amount.sum()); print(z[['dt','amount','Source','Description']].head(3).to_string())
