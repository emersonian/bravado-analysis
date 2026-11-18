import pandas as pd, sys
pd.set_option('display.width',300); pd.set_option('display.max_rows',800)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str)
pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv'); p=list(pl.Account); v=pl.set_index('Account')['Year Total']
def rng(a,b): return p[p.index(a):p.index(b)+1]
inc=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale'); con=rng('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart')
cg=[a for a in p if a.startswith('Cost of goods sold')]
ful=rng('External stores Fulfillment fees - Amazon Bravado Spice - United States','Inventory reimbursement - Amazon Bravado Spice - United States')
opx=rng('Bad debt','R&D expenses')
# variants
print('gross',v[inc].sum(),'contra',v[con].sum())
print('sales only (Sales - *)', v[[a for a in inc if a.startswith('Sales')]].sum())
print('net excl shipping income', v[[a for a in inc if a.startswith('Sales')]].sum()-v[con].sum())
print('164673 + ?', 180910.23-164673, 196110.02-164673)
print('COGS 43563 diff',47049.43-43563,' fulf 25165 vs',v[ful].sum(), 'opex 153241 vs',v[opx].sum(), v[opx].sum()-153241)
# cum by date
for name,acc,sg in [('net',inc,1),('con',con,-1)]:
    pass
x=f[f.account.isin(inc)].groupby('d').amount.sum().cumsum()-f[f.account.isin(con)].groupby('d').amount.sum().cumsum().reindex(f[f.account.isin(inc)].groupby('d').amount.sum().index,method='ffill').fillna(0)
print(x[(x>164000)&(x<165500)])
c=f[f.account.isin(cg)].groupby('d').amount.sum().cumsum(); print(c[(c>43300)&(c<43800)])
