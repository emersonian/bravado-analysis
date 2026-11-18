import pandas as pd, sys, itertools
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',90)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv'); pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
t=pd.read_csv('fin_tb.csv',index_col=0)
names=list(bs.Account)
iA=names.index('Credit card - Chase - UnitedSM Explorer Card 5839'); iE=names.index('Retained earnings')
A=names[:iA]; L=names[iA:iE]; E=names[iE:]
for col in ('open','end'):
    a=t.loc[A,col].sum(); l=t.loc[L,col].sum(); e=t.loc[E,col].sum()
    print(col,'assets',round(a,2),'liab',round(l,2),'equity accts',round(e,2),'A-L-E =',round(a-l-e,2))
p=list(pl.Account)
def rng(a,b): return p[p.index(a):p.index(b)+1]
inc=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale')
contra=rng('Discounts & promotions - Amazon Bravado Spice - United States','Refunds & returns - Walmart')
cogs=rng('Cost of goods sold - Amazon Bravado Spice - United States','Inventory reimbursement - Amazon Bravado Spice - United States')
opex=rng('Bad debt','R&D expenses')
oth=rng('Interest income','Money-out')
print(len(inc)+len(contra)+len(cogs)+len(opex)+len(oth),len(p))
v=pl.set_index('Account')['Year Total']
print('inc',v[inc].sum().round(2),'contra',v[contra].sum().round(2),'cogs',v[cogs].sum().round(2),'opex',v[opex].sum().round(2))
print(v[oth])
# baseline: income - contra - cogs - opex + other income - other exp
othinc=['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']
othexp=['Bank charges & fees','Foreign Exchange Gain or Loss','Interest & financing fees','Auto-class in progress - Money spent','Reconciliation discrepancies','Money-out']
base=v[inc].sum()-v[contra].sum()-v[cogs].sum()-v[opex].sum()+v[othinc].sum()-v[othexp].sum()
print('baseline NI',round(base,2))
target=t.loc[A,'end'].sum()-t.loc[L,'end'].sum()-t.loc[E,'end'].sum()
print('target',round(target,2),'diff',round(target-base,2))
amb=['Fulfillment services reimbursement - Amazon Bravado Spice - United States','Fulfillment services reimbursement - Walmart','Inventory reimbursement - Amazon Bravado Spice - United States','Prior year adjustment','Foreign Exchange Gain or Loss','Selling fees - Amazon Bravado Spice - Canada','Deductions - Ke He','Inventory disposal fees - Amazon Bravado Spice - United States']
for r in range(0,len(amb)+1):
    for c in itertools.combinations(amb,r):
        adj=sum(2*v[x] for x in c)
        if abs(base+adj-target)<0.05: print('flip',c, round(base+adj,2))
