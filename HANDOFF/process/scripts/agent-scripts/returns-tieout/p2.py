exec(open('load.py').read())
def tb(asof):
    s=g[g.date<=asof].groupby('account').amount.sum()
    return s.add(bb,fill_value=0)
t=pd.DataFrame({y:tb(f'{y}-12-31') for y in (2021,2022,2023,2024,2025)}).fillna(0).round(2)
# restrict to balance sheet accounts: those not in P&L. Identify P&L accounts as those starting with 6,7,8,9 digits or in known list
import re
pl_named=['Charitable Contributions','Cost of Goods Sold','Depreciation','Discounts given','Electricity','Expiration Allowance','Faire Fees','Free fill','Gains/Loss on Asset Sale/Disposal','Gas','Insurance Proceeds - Loss','Inventory Adjustment','Inventory Shrinkage','Late Penalty Fees','Marketing Allowance','Melio Credit card fee','Melio services fee','Merchant Fees','On-Invoice Discounts','Pass Thru Deduction','QuickBooks Payments Fees','Reconciliation Discrepancies','Remittance Discrepancy','Returned Check','Sales Tax Expense','Sales of Product Income','Shipping Income','Shipping/Transit Discounts','Slotting Fees','Spoilage Allowance','Swell Discount','Tax Exempt Income','Uncategorized Expense','Uncollectible Sales']
def ispl(a):
    return bool(re.match(r'^[6789]\d{4}',a)) or a in pl_named
b=t[[not ispl(a) for a in t.index]]
b=b[(b.abs().sum(axis=1)>0.005)]
print(b.to_string())
b.to_csv('bs.csv')
