exec(open('fl.py').read())
print('total dr-sum',round(f.dr.sum(),2))
print(f.groupby('typ').dr.sum().round(2))
m=f.groupby(f.dt.dt.to_period('M')).dr.sum().round(2); print(m)
d=f.groupby(f.dt.dt.date).dr.sum().round(2); print(d[d.abs()>0.01])
# ending balances vs BS index
e=f.groupby('account').amount.sum().round(2)
b=bs.set_index('Account')['Ending Balance']
cmp=pd.DataFrame({'gl':e,'idx':b}).dropna(); cmp['d']=(cmp.gl-cmp.idx).round(2); print(cmp[cmp.d.abs()>0.01])
p=pl.set_index('Account')['Year Total']; e2=f[f.dt>'2026-01-01'].groupby('account').amount.sum().round(2)
cmp=pd.DataFrame({'gl':e2,'idx':p}).dropna(); cmp['d']=(cmp.gl-cmp.idx).round(2); print(cmp[cmp.d.abs()>0.01])
