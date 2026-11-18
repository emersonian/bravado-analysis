from common import *
f=pd.read_pickle('fl_typed.pkl'); g=qb()
pd.set_option('display.max_colwidth',90)
op=f[f.dt<'2026-01-01'].copy()
gb=op.groupby(['Source','Description'],dropna=False).dr.sum().round(2)
print('opening groups',len(gb),'nonzero',(gb!=0).sum()); print(gb[gb!=0])
nonre=op[op.account!='Retained earnings']; re=op[op.account=='Retained earnings']
# per group: nonRE dr sum vs RE
a=nonre.groupby(['Source','Description'],dropna=False).dr.sum().round(2); b=re.groupby(['Source','Description'],dropna=False).dr.sum().round(2)
j=pd.concat([a,b],axis=1,keys=['non','re']).fillna(0); j['d']=(j.non+j.re).round(2); print('groups w/o equal RE offset:',(j.d!=0).sum()); print(j[j.d!=0])
print('non-RE groups without any RE line:', (j.re==0).sum()); print(j[(j.re==0)&(j.non!=0)].head(20))
# quoted descriptions
for k in ['Checking#positive','per customer','A/P balance','Total Debt','Internal transfer closing','Payout from SHOPIFY']:
    x=op[(op.Description.astype(str)+' '+op.Source.astype(str)).str.contains(k,regex=False)&(op.account!='Retained earnings')]
    print(k); print(x[['account','amount','Source','Description']].to_string(index=False))
# QB social security deferral and 2024 NI
print(g[(g.account=='34310 Social Security')&(g.date>='2023-01-01')][['date','type','num','memo','amount']].to_string())
