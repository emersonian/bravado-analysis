exec(open('fl.py').read())
x=f[f.account=='Checking - Chase - PLAT BUS CHECKING 5189'].sort_values('dt').copy()
x['run']=x.amount.cumsum().round(2)
for _,r in x.iterrows():
    print(f"{r.datetime_utc[:10]}|{r.amount:10.2f}|{r.run:10.2f}|{str(r.Description)[:150]}")
print('=== 04-07 and 04-15 all rows by source: imbalance by Source')
for d in ['2026-04-07','2026-04-15']:
    y=f[f.dt.dt.date==pd.Timestamp(d).date()]
    g=y.groupby(y.Source.astype(str)).dr.sum().round(2); print(d, g[g.abs()>0.01])
y=f[(f.dt.dt.date==pd.Timestamp('2026-04-15').date())&(f.Source.astype(str).str.contains('Gusto|GUSTO'))]; show(y)
