exec(open('load.py').read())
pd.set_option('display.max_colwidth',90)
x=g[g.name.fillna('').str.contains('Nguyen',case=False)&(g.year>=2025)]
print(x[['account','date','type','num','name','memo','split','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,60)).to_string(index=False))
x=g[g.name.fillna('').str.contains('Mark Clark',case=False)&(g.year>=2025)&(g.account=='31000 Accounts Payable')]
print(x[['account','date','type','num','name','memo','split','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,60)).to_string(index=False))
