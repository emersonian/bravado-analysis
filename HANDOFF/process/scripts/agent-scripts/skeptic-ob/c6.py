from common import *
m=pd.read_pickle('m.pkl'); f=pd.read_pickle('fl_typed.pkl')
pd.set_option('display.max_colwidth',200)
x=m[(m.kind=='other')&(m.other.isin(['NETS ZERO','NO MATCH']))]
print(x[['account','dt','amount','k','other']].to_string(index=False))
for _,r in x.iterrows():
    c=f[(f.dt==r.dt)&(f.amount.abs().round(2)==abs(round(r.amount,2)))]
    print(c[['account','amount','Source','Description']].to_string(index=False)[:1500]); print('--')
