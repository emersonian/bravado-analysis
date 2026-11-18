exec(open('load.py').read())
d=g[(g.account=='73902 Salaries & Wages')&(g.year==2025)].copy()
d['memo']=d.memo.fillna('').str.slice(0,70)
print(d[['date','type','num','name','memo','amount']].to_string(index=False))
# AJE-547 legs
print(g[(g.num=='AJE-547')][['account','date','memo','amount']].to_string())
# all Gusto JE on one date
x=g[(g.num=='Gusto')&(g.date=='2025-06-13')]
print(x[['account','date','name','memo','amount']].to_string())
