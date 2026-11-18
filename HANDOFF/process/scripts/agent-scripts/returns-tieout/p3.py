exec(open('load.py').read())
import sys
cols=['date','type','num','name','memo','split','amount']
for a in ['80001 Other Misc Income','80000 Interest Earned','80005 Rent Income','Gains/Loss on Asset Sale/Disposal','34310 Social Security','Security Deposits','Loan Receivable - Specialty Bottling Group','Accrued Expense','Wages Due to Jeremiah','Texas State Comptroller Payable']:
    d=g[(g.account==a)&(g.year>=2023)]
    if a=='80000 Interest Earned': d=d[d.amount.abs()>1]
    print('=====',a, len(d)); print(d[cols].to_string(index=False))
