import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',80)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',low_memory=False); g['date']=pd.to_datetime(g['date']); g['y']=g.date.dt.year
inc=[a for a in g.account.unique() if a[:2] in ('61','63','64','65','66','67')]
for y in (2024,2025):
    x=g[(g.y==y)&g.account.isin(inc)]
    print(y,'income total',round(x.amount.sum(),2))
    prod=x[x.account.str[:3].isin(['612','613','614','615'])]
    print(' per-product accounts',round(prod.amount.sum(),2)); print(prod.groupby('type').amount.sum().round(2).to_string())
    top=prod.groupby('name').amount.sum().sort_values(ascending=False).head(8).round(0); print(top.to_string())
    for a in ['61600 Faire Sales','64000 Online Sales','65100 Amazon US Market Sales','66000 Other Income','67000 Uncategorized Income']:
        print('  ',a,round(x[x.account==a].amount.sum(),2))
    cos={'product (71000,71300,71400,71500,Inventory Adjustment,Inventory Shrinkage)':['71000 Cost of Sales (COS)','71300 Ingredients - COS','71400 Co-Packer - COGS','71500 Materials - COS','Inventory Adjustment','Inventory Shrinkage','Cost of Goods Sold'],
         'shipping 71100':['71100 Shipping & Delivery - COS'],'other costs 71200':['71200 Other Costs - COS'],'placement 71600':['71600 Placement/Freefill - COS'],
         'trade deductions (Swell, On-Invoice, Pass Thru, Spoilage, Marketing Allowance)':['Swell Discount','On-Invoice Discounts','Pass Thru Deduction','Spoilage Allowance','Marketing Allowance'],'QB payments fees':['QuickBooks Payments Fees']}
    tot=0
    S=x.amount.sum()
    for k,v in cos.items():
        s=g[(g.y==y)&g.account.isin(v)].amount.sum(); tot+=s; print('  COS',k,round(s,2),f'{s/S:.1%}')
    print('  COS total',round(tot,2), f'GM {(S-tot)/S:.2%}')
    o=g[(g.y==y)&(g.account=='71200 Other Costs - COS')]
    print(o.groupby('name',dropna=False).amount.sum().sort_values(ascending=False).head(8).round(0).to_string())
    print(g[(g.y==y)&(g.account=='71400 Co-Packer - COGS')].groupby('type').amount.sum().round(0).to_string())
    print(g[(g.y==y)&(g.account=='Swell Discount')].groupby('name',dropna=False).amount.sum().sort_values(ascending=False).head(5).round(0).to_string())
