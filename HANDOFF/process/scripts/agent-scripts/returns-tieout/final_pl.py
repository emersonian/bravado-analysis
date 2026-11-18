exec(open('load.py').read())
exec(open('p1.py').read().split("for y in (2022")[0].split("exec(open('load.py').read())")[1])
def S(y):
    return g[g.year==y].groupby('account').amount.sum()
def A(s,*names): return sum(s.get(n,0.0) for n in names)
out=[]
def line(y,name,ret,led,how):
    out.append((y,name,ret,round(led,2),round(led-ret,2),how))
# ---- 2023
s=S(2023); I=A(s,*inc); C=A(s,*cogs); dAR=s['12000 Accounts Receivable']; dAP=s['31000 Accounts Payable']; dInv=A(s,*inv)
line(2023,'gross receipts',1868988,I-dAR,'accrual income - dAR')
line(2023,'COGS',863959,C+dInv-dAP-s['Accrued Expense']-s['Wages Due to Jeremiah'],'COGS+dInv-dAP-dAccrued-dWagesDue')
line(2023,'COGS (adj 1100 & 27.59)',863959,C+dInv-dAP-s['Accrued Expense']-s['Wages Due to Jeremiah']-1100-27.59,'... -1100 -27.59')
line(2023,'4797 gain',16500,-s['Gains/Loss on Asset Sale/Disposal'],'gain acct')
line(2023,'officer+salaries',10039+384873,s['73902 Salaries & Wages'],'73902 total')
line(2023,'repairs',5081,s['76000 Repair & Maintenance'],'')
line(2023,'bad debts',333,s['74000 Bad Debts'],'')
line(2023,'rents',122807,s['73100 Rent or Lease'],'')
line(2023,'taxes',32862,A(s,'73901 Payroll Taxes','73800 Taxes & Licenses'),'73901+73800')
line(2023,'interest',64336,s['73450 Interest Expense'],'')
line(2023,'emp benefits',15117,s['73640 Insurance - Health'],'')
mk=['72000 Marketing/Advertising','72100 Freight & Delivery - Marketing','72200 Social Media Marketing','72300 Promotional','72400 Travel','72500 Events/Shows','72600 In Store Marketing','72601 Marketing Scanbacks','72700 Website/Design','Slotting Fees','Free fill']
od={'auto':(378,A(s,'Gas')),'bank':(18151,A(s,'73410 Bank Fees','73420 Credit Card Fees','73430 PayPal Fees','Melio Credit card fee','73400 Financial Fees')),'dues':(52345,s['73500 Dues & Subscriptions']),'contractor':(65251,s['73900 1099 Non-Employee Compensation']),'insurance':(6999,s['73600 Insurance']),'liability':(11740,s['73620 Insurance - Liability']),'legal':(44035,s['73700 Professional Fees']),'marketing':(175002,A(s,*mk)),'meals50':(3981,s['73220 Food Expense']/2),'misc':(3582,A(s,'75500 Reimbursements','Remittance Discrepancy')),'office':(15617,A(s,'73200 Office Expenses','73000 Overhead Expenses (G&A)','Reconciliation Discrepancies')),'postage':(630,s['73210 Shipping Supplies']),'travel':(38646,s['75000 Travel']),'utilities':(22387,A(s,'73300 Utilities','Electricity'))}
for k,(r,l) in od.items(): line(2023,'OD '+k,r,l,'')
# ---- 2024
s=S(2024); I=A(s,*inc); C=A(s,*cogs); dAR=s['12000 Accounts Receivable']; dAP=s['31000 Accounts Payable']; dInv=A(s,*inv)
line(2024,'gross receipts',862582,I-dAR+s['80001 Other Misc Income'],'income - dAR + 80001')
line(2024,'COGS',396370,C+dInv-dAP,'COGS+dInv-dAP')
line(2024,'COGS (+1100)',396370,C+dInv-dAP+1100,'COGS+dInv-dAP+1100')
line(2024,'4797 gain',15735,-s['Gains/Loss on Asset Sale/Disposal'],'')
line(2024,'officer+salaries',3694+140131,s['73902 Salaries & Wages']-s['Wages Due to Jeremiah'],'73902 - dWagesDue')
line(2024,'repairs',3196,s['76000 Repair & Maintenance'],'')
line(2024,'bad debts',9654,s['74000 Bad Debts'],'')
line(2024,'rents',62248,A(s,'73100 Rent or Lease','73110 Office Rent')-2330,'73100+73110 - accrued 2330')
line(2024,'taxes',1817,A(s,'73901 Payroll Taxes'),'73901 (net of -6441.26 CPA-WSA1)')
line(2024,'interest',39431,s['73450 Interest Expense'],'')
line(2024,'emp benefits',10791,s['73640 Insurance - Health'],'')
od={'bank':(33386,A(s,'73400 Financial Fees','73410 Bank Fees','73420 Credit Card Fees','73430 PayPal Fees','Faire Fees','Late Penalty Fees','Melio Credit card fee')),'dues':(27911,s['73500 Dues & Subscriptions']),'contractor':(91815,s['73900 1099 Non-Employee Compensation']),'insurance':(3365,s['73600 Insurance']),'liability':(5437,s['73620 Insurance - Liability']),'legal':(47936,s['73700 Professional Fees']),'marketing':(44441,A(s,*mk)),'misc':(837,A(s,'75500 Reimbursements','Remittance Discrepancy')),'office':(12280,A(s,'73200 Office Expenses','73210 Shipping Supplies','73220 Food Expense')),'utilities':(11446,A(s,'73300 Utilities','Electricity'))}
for k,(r,l) in od.items(): line(2024,'OD '+k,r,l,'')
line(2024,'rental income',17990,s['80005 Rent Income'],'80005')
# ---- 2025
s=S(2025); I=A(s,*inc); C=A(s,*cogs); dAR=s['12000 Accounts Receivable']; dAP=s['31000 Accounts Payable']; dInv=A(s,*inv)
line(2025,'gross receipts',474616,I-dAR,'income - dAR')
line(2025,'COGS',394527,C+dInv-dAP-s['Accrued Expense']-s['Texas State Comptroller Payable'],'COGS+dInv-dAP-dAccrued-dTexas')
line(2025,'other income',156641,s['80001 Other Misc Income'],'80001')
line(2025,'salaries',62919,s['73902 Salaries & Wages']-2*69033,'73902 - 2x69033')
line(2025,'repairs',1982,s['76000 Repair & Maintenance'],'')
line(2025,'bad debts',849,s['74000 Bad Debts'],'')
line(2025,'rents',30573,s['73100 Rent or Lease'],'')
line(2025,'taxes',12910,A(s,'73901 Payroll Taxes','73800 Taxes & Licenses'),'')
line(2025,'interest',15268,s['73450 Interest Expense'],'')
line(2025,'advertising',11881,A(s,*mk)-s['72400 Travel'],'marketing group excl travel')
od={'bank':(8478,A(s,'73400 Financial Fees','73410 Bank Fees','73430 PayPal Fees','Faire Fees','Late Penalty Fees','Merchant Fees','Melio services fee','Remittance Discrepancy')),'dues':(24985,s['73500 Dues & Subscriptions']),'contractor':(19004,s['73900 1099 Non-Employee Compensation']),'insurance':(18095,A(s,'73600 Insurance','73620 Insurance - Liability','73640 Insurance - Health')),'legal':(58122,s['73700 Professional Fees']),'marketing(900)':(900,s['Charitable Contributions']),'office':(9104,A(s,'73200 Office Expenses','73210 Shipping Supplies','73220 Food Expense')),'travel':(5369,A(s,'72400 Travel','Gas')),'utilities':(4184,s['73300 Utilities'])}
for k,(r,l) in od.items(): line(2025,'OD '+k,r,l,'')
df=pd.DataFrame(out,columns=['year','line','return','ledger','diff','how'])
print(df.to_string(index=False))
# net per books from QB identity
for y,qbni in ((2023,None),(2024,None),(2025,None)):
    s=S(y)
    pl=[a for a in s.index if (a[:1] in '6789' and a[:5].isdigit()) or a in ['Charitable Contributions','Cost of Goods Sold','Depreciation','Discounts given','Electricity','Expiration Allowance','Faire Fees','Free fill','Gains/Loss on Asset Sale/Disposal','Gas','Insurance Proceeds - Loss','Inventory Adjustment','Inventory Shrinkage','Late Penalty Fees','Marketing Allowance','Melio Credit card fee','Melio services fee','Merchant Fees','On-Invoice Discounts','Pass Thru Deduction','QuickBooks Payments Fees','Reconciliation Discrepancies','Remittance Discrepancy','Returned Check','Sales Tax Expense','Sales of Product Income','Shipping Income','Shipping/Transit Discounts','Slotting Fees','Spoilage Allowance','Swell Discount','Tax Exempt Income','Uncategorized Expense','Uncollectible Sales']]
    incs=set(inc)|{'80000 Interest Earned','80001 Other Misc Income','80005 Rent Income'}
    ni=sum(s[a] if a in incs else (-s[a]) for a in pl)
    # gains account is 'other expense' negative => -(-x)=+x handled by -s
    adj=-s.get('12000 Accounts Receivable',0)-A(s,*inv)+s.get('31000 Accounts Payable',0)+s.get('Accrued Expense',0)+s.get('Wages Due to Jeremiah',0)+s.get('Texas State Comptroller Payable',0)
    print(y,'QB NI',round(ni,2),'cash-adjusted (AR,Inv,AP,Accrued,WagesDue,Texas)',round(ni+adj,2))
