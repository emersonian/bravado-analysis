from ld import *
x=f[f.account=='Inventory'].copy(); x['m']=x.datetime_utc.dt.to_period('M')
print(x.groupby('m').amount.agg(lambda s:(s[s>0].sum().round(0), s[s<0].sum().round(0))).to_string())
print(x[x.amount.abs()>3000][['datetime_utc','amount','Source','Description']].to_string())
# QB founder accounts: cash vs journal by year
fa=['33500 Due to Jeremiah','Due from Jer',"53000 Jer's Draw",'Wages Due to Jeremiah']
z=q[q.account.isin(fa)&(q.y>=2022)].copy()
z['kind']=z.type.where(z.type=='Journal Entry','cash/other')
print(z.pivot_table(index=['account','kind'],columns='y',values='amount',aggfunc='sum').round(0).fillna(0).to_string())
# net receivable position by year-end: (Due from Jer) - (33500 credit bal) - draws(neg equity) ; minus Wages due
for d in ['2022-12-31','2023-12-31','2024-12-31','2025-12-31','2026-03-27']:
    dfj=bal('Due from Jer',d); dt=bal('33500 Due to Jeremiah',d); dr=bal("53000 Jer's Draw",d); w=bal('Wages Due to Jeremiah',d)
    print(d,'DueFrom',round(dfj,2),'33500',round(dt,2),'Draw',round(dr,2),'=> owed by him',round(dfj-dt-dr,2),'WagesDue',round(w,2),'net',round(dfj-dt-dr-w,2))
# interest income / any interest on owner balance
print(q[q.account=='80000 Interest Earned'].groupby('y').amount.sum())
# credits (repayments) hitting founder accounts from bank
r=z[(z.kind!='Journal Entry')]
r33=r[(r.account=='33500 Due to Jeremiah')&(r.amount>0)]
print('cash credits to 33500 by year (he put money in / paid for company)'); print(r33.groupby('y').amount.agg(['sum','count']))
# 33500 2026 QB lines
print(q[(q.account=='33500 Due to Jeremiah')&(q.y==2026)][['date','type','num','memo','amount','split']].to_string())
# QB net income 2025, 2024
bs_prefix=('1','2','3','5')
