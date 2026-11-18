exec(open('load.py').read())
pd.set_option('display.max_colwidth',110)
x=g[(g.account=='Due from James')]
print(x[['date','type','num','name','memo','split','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,105)).to_string(index=False))
for n in ['AJE-173','AJE-175','AJE-172','AJE-39']:
    x=g[g.num==n]; print('==',n); print(x[['account','date','memo','amount']].assign(memo=lambda d:d.memo.fillna('').str.slice(0,70)).to_string(index=False))
