import pandas as pd, itertools, re
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
c={'ERC1':17248.74,'ERC2':7329.17,'ERC3':62268.27,'ERC4':14443.33,'AJE455':7661.73,'AJE456':43743.70,'AJE496':3034.90,'AJE422':911.02}
for a,x in g[g.y==2025].groupby('account'):
    if re.match(r'[6-9]\d{4} ',a) or a in ('Late Penalty Fees','Charitable Contributions','Remittance Discrepancy','Melio services fee','Inventory Adjustment','Faire Fees','Merchant Fees','Gas'):
        v=round(x.amount.sum(),2)
        if abs(v)>0.5 and not a.startswith('61') and a!='80001 Other Misc Income': c[a]=v
print(len(c))
items=list(c.items())
for target in (131781,24316,156097,30491.49):
    print('TARGET',target)
    for n in range(1,6):
        cnt=0
        for combo in itertools.combinations(items,n):
            # require at least one 80001 component
            for signs in itertools.product((1,-1),repeat=n):
                if signs[0]<0: continue
                s=sum(sg*v for sg,(k,v) in zip(signs,combo))
                if abs(abs(s)-target)<=1.5:
                    cnt+=1
                    if cnt<=6: print(n,round(s,2),[(sg,k) for sg,(k,v) in zip(signs,combo)])
        print(' n=',n,'hits',cnt)
        if n>=4 and len(items)>30: break
