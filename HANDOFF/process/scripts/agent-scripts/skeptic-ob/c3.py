from common import *
g=qb()
print(g[g.account=='SBA Disaster Loan'][['date','type','num','amount','split']].to_string())
print(g[(g.num=='AJE-354')][['account','date','memo','amount']].to_string())
print(g[g.num.isin(['AJE-541','AJE-542','AJE-543'])][['account','date','memo','amount']].to_string())
