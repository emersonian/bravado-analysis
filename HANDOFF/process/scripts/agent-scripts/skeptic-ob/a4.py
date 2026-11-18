from common import *
g=qb()
def show(num,date=None,acctfilter=None):
    s=g[g.num==num]
    if date: s=s[s.date==date]
    print('=====',num,date,len(s), 'types',s.type.unique(), 'dates',s.date.dt.date.unique()[:5])
    if acctfilter: s=s[s.account.str.contains(acctfilter)]
    print(s[['account','date','name','memo','amount']].to_string(index=False))
for n,d in [('28','2020-12-31'),('29','2020-12-31'),('35','2021-01-01'),('WSA CPA',None),('AJE-37',None),('AJE-39',None),('AJE-172',None),('AJE-173',None),('AJE-177',None),('AJE-175',None),('AJE-397',None),('CPA AJE 1 - 2024',None),('AJE-387',None),('AJE-388',None),('AJE-547',None),('AJE-345',None)]:
    show(n,d)
