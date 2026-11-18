exec(open('load.py').read())
def tb(asof):
    s=g[g.date<=asof].groupby('account').amount.sum()
    return s.add(bb,fill_value=0)
def A(s,*n): return sum(s.get(x,0.0) for x in n)
R={2022:dict(cash=44600,oca=39998,loans_sh=43295,other_assets=8800,ocl=240518,loans_from_sh=0,notes=152600,apic=0,re=-256425),
   2023:dict(cash=166501,oca=31814,loans_sh=100231,other_assets=8800,ocl=418389,loans_from_sh=0,notes=222026,apic=0,re=-333069),
   2024:dict(cash=17458,oca=3238,loans_sh=131809,other_assets=0,ocl=182412,loans_from_sh=100000,notes=62931,apic=189010,re=-381848),
   2025:dict(cash=3146,oca=2377,loans_sh=294256,other_assets=0,ocl=87313,loans_from_sh=88767,notes=364430,apic=189010,re=-429741)}
cards=['32400 Spark Business Credit Card - 4964','32600 Southwest Airlines Rapid Rewards Credit Card 7510',"32700 Vince's Southwest Airlines Rapid Rewards 7528","32800 James's Chase Ink Card",'Business AMEX Card_3007','Chase 5039','Chase 7084','Credit card (9532)','Shopify Credit']
inv=['Katana ERP Inventory','Katana Inventory_Materials','Katana Inventory_Product','Shopify/ Web Inventory','Amazon Inventory','20000 Inventory Asset']
for y in (2022,2023,2024,2025):
    s=tb(f'{y}-12-31'); L={}
    L['cash']=A(s,'11100 Chase Savings 3580','11200 Chase Checking 5189','11500 Cash on hand','15000 Undeposited Funds','1862 Found Chase Bank','Chase, Checking ...8733','QuickBooks Checking Account')
    L['oca']=A(s,'13000 Prepaid Expenses','Loan Receivable - Specialty Bottling Group','Faire Clearing Account')
    L['loans_sh']=A(s,'Due from James','Due from Jer')-A(s,'33500 Due to Jeremiah')-A(s,"53000 Jer's Draw","54000 James' Draw")+(69033.0 if y==2025 else 0)
    L['other_assets']=A(s,'Security Deposits')
    loc=A(s,'33100 Anthony Tallerine LOC','33200 BlueVine LOC','33300 Fundbox Invoice Advances')
    L['ocl']=A(s,*cards)+loc+A(s,'34100 Employer Benefit Liabilities','34310 Social Security','Debt to Equity - Hugh and Christy Nguyen','Debt to Equity - Mark Clark','Forward Financing Loan','Loan From Mark Clark')
    nguyen=A(s,'Loan From Nguyen')
    L['loans_from_sh']=nguyen if y>=2024 else 0
    L['notes']=A(s,'35000 Loan Payable - Chevrolet','Quickbooks Capital Loan','Amazon Loan','Funding Circle Loan','Parafin Capital','Shopify Capital','SBA Disaster Loan','Loan - Intuit Financing','Loan from Shopify')+(nguyen if y==2023 else 0)
    L['apic']=A(s,'Member Equity - Clark','Member Equity - Coinbase','Member Equity - Nguyen')
    L['re']=L['cash']+L['oca']+L['loans_sh']+L['other_assets']-L['ocl']-L['loans_from_sh']-L['notes']-L['apic']
    print('=====',y)
    for k in R[y]: print(f'  {k:14s} return {R[y][k]:>10,}  ledger {L[k]:>13,.2f}  diff {L[k]-R[y][k]:>8.2f}')
    print('  cards',round(A(s,*cards),2),'LOC',round(loc,2))
    absent={k:round(s.get(k,0),2) for k in ['31000 Accounts Payable','Accrued Expense','Wages Due to Jeremiah','Texas State Comptroller Payable']}
    print('  absent liabilities',absent,'total',round(sum(absent.values()),2))
    print('  absent assets: AR',round(s.get('12000 Accounts Receivable',0),2),'inventory',round(A(s,*inv),2))
    print('  loans_sh parts: James',round(s.get('Due from James',0),2),'Jer',round(s.get('Due from Jer',0),2),'33500',round(s.get('33500 Due to Jeremiah',0),2),'draw',round(s.get("53000 Jer's Draw",0),2))
