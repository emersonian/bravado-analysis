from common import *
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv'); names=pl.Account.tolist()
def grp(a,b): return names[names.index(a):names.index(b)+1]
G={'income':grp('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale'),
'contra':grp('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart'),
'cogs':grp('Cost of goods sold - Amazon Bravado Spice - United States','Cost of goods sold - Wholesale'),
'fulfil_sell':grp('External stores Fulfillment fees - Amazon Bravado Spice - United States','Inventory reimbursement - Amazon Bravado Spice - United States'),
'opex':grp('Bad debt','R&D expenses'),
'oth_inc':['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in'],
'oth_exp':['Bank charges & fees','Foreign Exchange Gain or Loss','Interest & financing fees','Auto-class in progress - Money spent','Reconciliation discrepancies','Money-out']}
m={a:k for k,l in G.items() for a in l}
x=f[f.account.isin(names)].copy(); x['g']=x.account.map(m); x['mon']=x.dt.dt.to_period('M').astype(str)
x.loc[x.dt>='2026-07-23','mon']='2026-07-23'
t=x.pivot_table(index='mon',columns='g',values='amount',aggfunc='sum',margins=True).fillna(0)
t['net_sales']=t.income-t.contra
print(t[['income','contra','net_sales','cogs','fulfil_sell','opex','oth_inc','oth_exp']].round(2).to_string())
h1=x[x.dt<'2026-07-01'].groupby('g').amount.sum(); print(h1.round(2))
print('H1 op loss before PYA', h1.income-h1.contra-h1.cogs-h1.fulfil_sell-h1.opex-4243.81, 'with', h1.income-h1.contra-h1.cogs-h1.fulfil_sell-h1.opex)
# selected accounts by month
sel=['Salaries & wages (via Gusto)','Employer taxes (via Gusto)','Contractors','Reimbursements to owners','Employee benefit programs','Employee benefit programs (via Gusto)','Reimbursements to employees (via Gusto)','Rent & lease']
print(x[x.account.isin(sel)].pivot_table(index='mon',columns='account',values='amount',aggfunc='sum',margins=True).fillna(0).round(2).rename(columns=lambda c:c[:22]).to_string())
