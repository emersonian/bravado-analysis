exec(open('load.py').read())
pd.set_option('display.max_colwidth',100)
d=g[(g.date=='2023-03-07')&(g.type=='Deposit')]
print(d[['account','date','type','name','memo','split','amount']].to_string(index=False))
# search for box truck / truck mentions
m=g[g.memo.fillna('').str.contains('box truck|order picker|fork ?lift|chevrolet|chevy|silverado|racking',case=False)]
print(m[['account','date','type','num','memo','split','amount']].assign(memo=lambda x:x.memo.str.slice(0,90)).to_string(index=False))
# search amounts 10039, 3694, 1100 exact etc
for v in (10039,3694,12135,12134.87,5516.0):
    x=g[(g.amount.abs().round(0)==round(v))]
    print('amount ~',v, len(x)); print(x[['account','date','type','num','memo','amount']].assign(memo=lambda x:x.memo.fillna('').str.slice(0,70)).head(8).to_string(index=False))
