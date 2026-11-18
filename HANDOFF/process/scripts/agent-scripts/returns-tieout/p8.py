exec(open('load.py').read())
pd.set_option('display.max_colwidth',120)
for n in ['AJE-229','AJE-253','AJE-270','AJE-311','AJE-313','AJE-307','CPA-WSA1','CPA AJE 2 - 2025','AJE-455','AJE-456','AJE-422','AJE-380','AJE-135']:
    x=g[g.num==n]
    print('=====',n, 'dates',sorted(set(x.date.dt.date.astype(str))))
    print(x[['account','date','name','memo','amount']].to_string(index=False))
x=g[g.num=='AJE-496']
print('AJE-496 by account'); print(x.groupby('account').amount.agg(['sum','count']))
print(sorted(g[g.num.fillna('').str.startswith('CPA')].num.unique()))
