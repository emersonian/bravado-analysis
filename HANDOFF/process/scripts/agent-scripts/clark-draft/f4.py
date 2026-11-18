import pandas as pd, sys, itertools
pd.set_option('display.width',280); pd.set_option('display.max_rows',800); pd.set_option('display.max_colwidth',100)
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv'); pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
f=pd.read_csv(D+'finaloop_gl.csv',low_memory=False)
f['dt']=pd.to_datetime(f['datetime_utc']); f['d']=f.dt.dt.date.astype(str)
names=list(bs.Account)
iA=names.index('Credit card - Chase - UnitedSM Explorer Card 5839'); iE=names.index('Retained earnings')
A=set(names[:iA]); L=set(names[iA:iE]); E=set(names[iE:])
p=list(pl.Account)
def rng(a,b): return p[p.index(a):p.index(b)+1]
inc=rng('Gift wrap - Amazon Bravado Spice - United States','Shipping income - Wholesale')+['Interest income','Auto-class in progress - Money received','Cashback & rewards','Money-in']
sign={}
for a in f.account.unique():
    if a in A: sign[a]=1      # debit-natural
    elif a in L or a in E: sign[a]=-1
    elif a in inc: sign[a]=-1
    else: sign[a]=1
f['dr']=f.amount*f.account.map(sign)
m=f.groupby(f.dt.dt.to_period('M')).dr.sum().round(2)
print(m, m.sum())
dd=f.groupby('d').dr.sum().round(2)
print(dd[dd.abs()>0.05].to_string())
