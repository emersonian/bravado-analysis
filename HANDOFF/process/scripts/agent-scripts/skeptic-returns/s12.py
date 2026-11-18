import pandas as pd, itertools, re
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
c={}
for a,x in g[g.y==2025].groupby('account'):
    v=round(x.amount.sum(),2)
    if abs(v)>=500: c['d25 '+a]=v
for a,x in g[g.y<=2025].groupby('account'):
    if re.match(r'[6-9]\d{4} ',a): continue
    v=round(x.amount.sum()+bb.get(a,0),2)
    if abs(v)>=500: c['bal25 '+a]=v
w=g[(g.account=='73902 Salaries & Wages')&(g.y==2025)]
for k in ['Regular Wages','Holiday Wages','Paid Time Off','Sick Time']:
    c['gusto '+k]=round(w[w.memo.fillna('').str.contains(k)].amount.sum(),2)
c['gusto all']=131952.09; c['AJE-547']=69033.0; c['WD debits']=23415.89; c['AJE-387']=15915.89; c['AJE-388']=5500; c['ERC total']=101289.51
for v in (17248.74,7329.17,62268.27,14443.33,43743.70,7661.73): c['e%s'%v]=v
# dedupe values
items=list(c.items()); print(len(items))
def search(target,tol,maxn):
    hits=[]
    vals=[(k,v) for k,v in items]
    for n in range(1,maxn+1):
        for combo in itertools.combinations(vals,n):
            for signs in itertools.product((1,-1),repeat=n):
                if signs[0]<0: continue
                s=sum(sg*v for sg,(k,v) in zip(signs,combo))
                if abs(abs(s)-target)<=tol: hits.append((round(s,2),[(sg,k,v) for sg,(k,v) in zip(signs,combo)]))
    return hits
for h in search(62919,1.0,2): print(h)
print('--- 3 terms')
h3=search(62919,1.0,3); print(len(h3))
for h in h3: print(h)
