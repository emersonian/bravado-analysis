from common import *
g=qb()
own=['Due from James','Due from Jer','33500 Due to Jeremiah','Wages Due to Jeremiah',"53000 Jer's Draw","54000 James' Draw",'Member Equity - Tallerine','Member Equity - Nelson']
print(g.type.value_counts())
je=g[(g.account.isin(own))&(g.type.str.contains('Journal',na=False))]
keys=je[['num','date']].drop_duplicates()
for _,k in keys.sort_values('date').iterrows():
    sub=g[(g.num==k.num)&(g.date==k.date)&(g.type.str.contains('Journal',na=False))] if isinstance(k.num,str) else g[(g.num.isna())&(g.date==k.date)&(g.type.str.contains('Journal',na=False))&(g.account.isin(own))]
    if len(sub)>40:
        sub=sub[sub.account.isin(own)]
    print('=====',k.num,k.date.date(), 'n=',len(sub))
    print(sub[['account','name','memo','split','amount']].to_string(index=False))
