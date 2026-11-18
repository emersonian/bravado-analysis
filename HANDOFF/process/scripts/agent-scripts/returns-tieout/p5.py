exec(open('load.py').read())
d=g[(g.account=='73902 Salaries & Wages')&(g.year.isin([2023,2024,2025]))].copy()
d['memo2']=d.memo.fillna('').str.slice(0,60)
print(d.groupby(['year','type']).amount.agg(['sum','count']))
# by memo pattern
d['k']=d.memo2.str.replace(r'\d','#',regex=True).str.slice(0,40)
for y in (2023,2024,2025):
    x=d[d.year==y]
    print('=====',y, x.amount.sum())
    print(x.groupby(['type','k']).amount.agg(['sum','count']).sort_values('sum',ascending=False).head(40).to_string())
