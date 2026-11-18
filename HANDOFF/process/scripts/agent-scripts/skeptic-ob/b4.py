from common import *
f=fl()
bs=pd.read_csv(D+'finaloop_Balance_Sheet_Index.csv'); pl=pd.read_csv(D+'finaloop_Profit_and_Loss_Index.csv')
bsl=list(bs.Account)
ia=bsl.index('Credit card - Chase - UnitedSM Explorer Card 5839'); ie=bsl.index('Retained earnings')
typ={}
for i,a in enumerate(bsl): typ[a]='A' if i<ia else ('L' if i<ie else 'E')
gl_accts=set(f.account.unique())
print('GL accts not in BS/PL idx:', sorted(gl_accts-set(bsl)-set(pl.Account)))
print('idx accts not in GL:', sorted((set(bsl)|set(pl.Account))-gl_accts))
# check GL sums vs index
s=f.groupby('account').amount.sum().round(2)
chk=bs.set_index('Account')['Ending Balance']
d=(s.reindex(chk.index).fillna(0)-chk).round(2); print('BS idx diffs', d[d!=0].to_dict())
chk=pl.set_index('Account')['Year Total']
d=(s.reindex(chk.index).fillna(0)-chk).round(2); print('PL idx diffs', d[d!=0].to_dict())
# regression for PL signs
f['day']=f.dt.dt.date
f['bsdr']=np.where(f.account.map(typ)=='A',f.amount,np.where(f.account.map(typ).isin(['L','E']),-f.amount,0.0))
plrows=f[~f.account.isin(typ)]
X=plrows.pivot_table(index='day',columns='account',values='amount',aggfunc='sum').fillna(0)
y=-f.groupby('day').bsdr.sum().reindex(X.index).fillna(0)
coef,res,rk,sv=np.linalg.lstsq(X.values,y.values,rcond=None)
sg=pd.Series(coef,index=X.columns)
print(sg.round(3).to_string())
sg.round().to_pickle('plsign.pkl'); pd.Series(typ).to_pickle('bstyp.pkl')
