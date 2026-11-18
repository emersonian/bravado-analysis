exec(open('load.py').read())
import itertools, numpy as np
d=g[(g.account=='80001 Other Misc Income')&(g.year==2025)]
items=[]
for _,r in d.iterrows():
    items.append((f"{r.date.date()} {r.num if isinstance(r.num,str) else r['name']}", r.amount))
# group AJE-496 lines? keep individually
extra=[('66000 Other Income 2025',62.03),('67000 Uncategorized Income 2025',1500.0),('80000 Interest Earned',0.92),('Late Penalty Fees',-912.52),('Charitable',-900.0),('Remittance Discrepancy',-12.95),('Melio fee',-278.5),('Bad debts',-849.24),('Inventory Adjustment',708.14)]
print('total 80001',d.amount.sum(), 'ERC', d[(d.name=='United States Treasury')|(d.num=='AJE-380')].amount.sum())
vals=np.array([v for _,v in items]); n=len(vals); print(n,'items')
# all subsets of 80001 items
sums=np.zeros(1<<n)
for i in range(n):
    sums[(np.arange(1<<n)>>i)&1==1]+=vals[i]
for target in (131781.0,24316.0,156097.0):
    idx=np.where(np.abs(sums-target)<=1.0)[0]
    print('target',target,'hits',len(idx))
    for m in idx[:10]:
        print('   ',round(sums[m],2),[items[i] for i in range(n) if (m>>i)&1])
    # nearest
    j=np.argmin(np.abs(sums-target)); print('   nearest',round(sums[j],2),'diff',round(sums[j]-target,2))
# with big groups + extras
big=[('ERC total',101289.51),('AJE-455 Spark CC',7661.73),('AJE-456 Chase 5039',43743.70),('AJE-496 neg AR',3034.90),('AJE-422',911.02)]+extra+[('ERC Jan',17248.74),('ERC Mar',7329.17),('ERC May',62268.27),('ERC Dec',14443.33)]
for target in (131781.0,24316.0):
    for k in range(1,6):
        for comb in itertools.combinations(big,k):
            names=[c[0] for c in comb]
            if 'ERC total' in names and any(x.startswith('ERC ') and x!='ERC total' for x in names): continue
            s=sum(c[1] for c in comb)
            if abs(s-target)<=1.5: print(target,round(s,2),comb)
