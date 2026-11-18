from common import *
import re
m=g.num.str.match(r'AJE-3(8[0-9]|9[0-9])R?$')|g.num.str.contains('CPA')
x=g[m&(g.date.dt.year==2024)]
print(x[['account','date','num','name','memo','amount']].to_string())
# Bad debts 2024 lines
x=g[(g.account=='74000 Bad Debts')&(g.date.dt.year==2024)]
print(x[['date','type','num','name','memo','split','amount']].to_string()); print(x.amount.sum())
