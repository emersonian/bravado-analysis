from common import *
f=pd.read_pickle('fl_typed.pkl')
fx=f.account=='Foreign Exchange Gain or Loss'
f.loc[fx,'t']='X'; f.loc[fx,'dr']=f.loc[fx,'amount']
f.to_pickle('fl_typed.pkl')
f['day']=f.dt.dt.date
d=f.groupby('day').dr.sum().round(2); print(d[d!=0])
pl=f[f.t.isin(['I','X'])]; print('PL total',round(-pl.dr.sum(),2))
for cut in ['2026-07-22 23:59:59','2026-07-23 23:59:59']:
    c=f[f.dt<=cut]; p=c[c.t.isin(['I','X'])]
    print(cut,'PL',round(-p.dr.sum(),2))
C=['account','dt','amount','dr','Source','Description','Transaction Classification']
print(f[f.amount.abs().round(2)==6033.40][C].to_string())
a7=f[f.day==pd.Timestamp('2026-04-07').date()]
print(len(a7)); 
# group by Source+dt+Description to find unbalanced groups
gb=a7.groupby(['Source','dt','Description'],dropna=False).dr.sum().round(2); print(gb[gb!=0])
a15=f[f.day==pd.Timestamp('2026-04-15').date()]
gb=a15.groupby(['Source','dt','Description'],dropna=False).dr.sum().round(2); print(gb[gb!=0])
print(a15[a15.Description.astype(str).str.contains('Reimbursement payment')][C].to_string())
print(f[f.Description.astype(str).str.contains('Reimbursement payment')].groupby('account').amount.agg(['sum','count']))
