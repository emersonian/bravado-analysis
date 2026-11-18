from common import *
x=g[(g.account=='80001 Other Misc Income')&(g.date.dt.year==2025)]
print(x[['date','type','num','name','memo','split','amount']].to_string())
print(x.amount.sum())
for n in ['AJE-455','AJE-456','AJE-380','AJE-422','AJE-496']:
    print(g[g.num==n][['account','date','num','name','memo','amount']].to_string())
x=g[(g.account=='80001 Other Misc Income')&(g.date.dt.year==2024)]
print(x[['date','type','num','name','memo','split','amount']].to_string())
