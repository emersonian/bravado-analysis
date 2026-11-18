import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',80)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str); f['m']=f.d.str[:7]
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv'); v=pl.set_index('Account')['Year Total']
p=list(pl.Account)
def rng(a,b): return p[p.index(a):p.index(b)+1]
G={}
G['gross income']=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale')
G['contra']=rng('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart')
G['product COGS']=[a for a in p if a.startswith('Cost of goods sold')]
G['fulfilment/shipping']=['External stores Fulfillment fees - Amazon Bravado Spice - United States','Fulfillment services fees - Walmart','Pick & pack fees - Amazon Bravado Spice - United States','Shipping & freight-out','Shipping & freight-out - Amazon Bravado Spice - United States']
G['selling fees']=['Fees - Shopify - bravado-spice','Fees - Stripe - Bravadospice','Selling fees - Amazon Bravado Spice - Canada','Selling fees - Amazon Bravado Spice - United States','Selling fees - Walmart']
G['inv reimb']=['Inventory reimbursement - Amazon Bravado Spice - United States']
G['comp (Gusto wages, taxes, benefits, contractors)']=['Salaries & wages (via Gusto)','Employer taxes (via Gusto)','Employee benefit programs','Employee benefit programs (via Gusto)','Contractors']
G['marketing all']=rng('Email marketing','Sales commissions')
G['rent']=['Rent & lease']; G['office&meals']=['Meals','Office supplies & equipment','Entertainment']
G['software']=['Software & subscriptions']; G['insurance']=['Insurance']; G['utilities']=['Utilities']
G['prof (legal+other prof)']=['Legal services','Other professional services']; G['financial services']=['Financial services']
G['repairs']=['Repairs & maintenance']; G['bank charges']=['Bank charges & fees']; G['bad debt']=['Bad debt']
G['travel+car']=['Travel','Car & truck']; G['reimb owners']=['Reimbursements to owners']; G['reimb employees']=['Reimbursements to employees (via Gusto)']
G['misc candidates']=['Miscellaneous expenses','Other operations expenses','R&D expenses','Inventory disposal fees - Amazon Bravado Spice - United States','Service fees - Amazon Bravado Spice - United States','Warehouse - Amazon Bravado Spice - United States','Auto-class in progress - Money spent','Reconciliation discrepancies','Money-out']
G['prior year adj']=['Prior year adjustment']; G['other inc']=['Interest income','Cashback & rewards','Money-in','Auto-class in progress - Money received']
G['interest']=['Interest & financing fees','Foreign Exchange Gain or Loss']
used=set()
for k,a in G.items():
    used|=set(a); print(f'{k:55s} {v[a].sum():12.2f}')
print('unused',[a for a in p if a not in used])
P=f[f.account.isin(p)]
m=P.pivot_table(index='account',columns='m',values='amount',aggfunc='sum',fill_value=0)
for k in ['gross income','contra','product COGS','fulfilment/shipping','selling fees','comp (Gusto wages, taxes, benefits, contractors)','marketing all','software','travel+car','reimb owners','bank charges','financial services','insurance','utilities','office&meals']:
    print(k, m.reindex(G[k]).sum().round(0).to_dict())
net=v[G['gross income']].sum()-v[G['contra']].sum()
print('net sales',net, 'x273/203',net*273/203, 'gross x',v[G['gross income']].sum()*273/203)
cos=v[G['product COGS']].sum()+v[G['fulfilment/shipping']].sum()+v[G['selling fees']].sum()+v[G['inv reimb']].sum()
print('cos group',cos,'GM',(net-cos)/net, 'product only GM',(net-v[G['product COGS']].sum())/net, 'prod/gross',v[G['product COGS']].sum()/v[G['gross income']].sum(),'prod/net',v[G['product COGS']].sum()/net)
print('stub sales (net basis)',243334-net,'stub cos',114771-cos,'stub GM',1-(114771-cos)/(243334-net))
print('stub sales gross basis',243334-v[G['gross income']].sum())
# channel mix gross
gi=v[G['gross income']]; print((gi/gi.sum()).round(4).to_string())
for ch,cg,sl in [('Amazon','Cost of goods sold - Amazon Bravado Spice - United States','Sales - Amazon Bravado Spice - United States'),('Dist','Cost of goods sold - Distribution','Sales - Distribution'),('Faire','Cost of goods sold - Faire (via Shopify)','Sales - Faire'),('Shopify','Cost of goods sold - Shopify - bravado-spice','Sales - Shopify - bravado-spice'),('Wholesale','Cost of goods sold - Wholesale','Sales - Wholesale')]:
    print(ch, round(v[cg]/v[sl],3))
print('days', (pd.Timestamp('2026-07-22')-pd.Timestamp('2025-12-31')).days, (pd.Timestamp('2026-09-30')-pd.Timestamp('2025-12-31')).days)
# last date of P&L activity
print(P.groupby('d').size().tail(3))
