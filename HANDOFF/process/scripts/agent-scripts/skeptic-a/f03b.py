from common import *
m=(g.name.str.contains('Treasury|IRS',case=False)|g.memo.str.contains('Treasury|ERC|IRS ',case=False))&(g.date>='2024-06-01')
print(g[m][['account','date','type','num','name','memo','split','amount']].to_string())
# CPA-WSA1, AJE-397
for n in ['CPA-WSA1','AJE-397','AJE-547']:
    print(g[g.num==n][['account','date','type','num','name','memo','amount']].to_string())
print(g[(g.date=='2024-12-31')&(g.type=='Journal Entry')][['account','date','num','name','memo','amount']].to_string())
