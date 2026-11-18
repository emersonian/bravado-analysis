import pandas as pd, re
pd.set_option('display.width',250); pd.set_option('display.max_rows',500); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
def yr(a,y): return round(g[(g.account==a)&(g.y==y)].amount.sum(),2)
def bal(a,y): return round(g[(g.account==a)&(g.y<=y)].amount.sum()+bb.get(a,0),2)
accts=sorted(g.account.unique())
inc=[a for a in accts if re.match(r'6[1-7]\d\d\d ',a)]+['Discounts given','Sales of Product Income','Shipping Income','Uncollectible Sales']
cogs=[a for a in accts if re.match(r'71\d\d\d ',a)]+['Inventory Adjustment','Inventory Shrinkage','Marketing Allowance','On-Invoice Discounts','Pass Thru Deduction','QuickBooks Payments Fees','Spoilage Allowance','Swell Discount','Cost of Goods Sold','Expiration Allowance','Shipping/Transit Discounts']
inv=['Katana ERP Inventory','Katana Inventory_Materials','Katana Inventory_Product','Shopify/ Web Inventory','Amazon Inventory','20000 Inventory Asset','Faire Inventory','Web Inventory']
for y in (2023,2024,2025):
    I=round(sum(yr(a,y) for a in inc),2); C=round(sum(yr(a,y) for a in cogs),2)
    dAR=yr('12000 Accounts Receivable',y); dInv=round(sum(yr(a,y) for a in inv),2)
    dAP=yr('31000 Accounts Payable',y); dAcc=yr('Accrued Expense',y); dW=yr('Wages Due to Jeremiah',y); dTx=yr('Texas State Comptroller Payable',y)
    print(y,'income',I,'dAR',dAR,'I-dAR',round(I-dAR,2),'80001',yr('80001 Other Misc Income',y))
    print('  COGS',C,'dInv',dInv,'dAP',dAP,'dAcc',dAcc,'dW',dW,'dTx',dTx)
    print('  COGS+dInv-dAP-dAcc-dW-dTx', round(C+dInv-dAP-dAcc-dW-dTx,2), ' w/o dW', round(C+dInv-dAP-dAcc-dTx,2))
    # net income
    pl=[a for a in accts if re.match(r'[6-9]\d\d\d\d ',a)]
    print('  balances: AR',bal('12000 Accounts Receivable',y),'inv',round(sum(bal(a,y) for a in inv),2),'AP',bal('31000 Accounts Payable',y),'Accr',bal('Accrued Expense',y),'WD',bal('Wages Due to Jeremiah',y),'TX',bal('Texas State Comptroller Payable',y))
for y in (2022,):
    print(y,'balances: AR',bal('12000 Accounts Receivable',y),'inv',round(sum(bal(a,y) for a in inv),2),'AP',bal('31000 Accounts Payable',y),'Accr',bal('Accrued Expense',y))
print('inv detail'); 
for a in inv: print(a,[yr(a,y) for y in (2023,2024,2025)],[bal(a,y) for y in (2022,2023,2024,2025)])
# 80001 detail
x=g[g.account=='80001 Other Misc Income'][['date','type','num','name','memo','split','amount']]
print(x.to_string())
