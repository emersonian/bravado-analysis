from ld import *
import sys
def dump(a, y0=2020):
    x=q[(q.account==a)&(q.y>=y0)].sort_values('date')
    print('\n==',a,len(x),round(x.amount.sum(),2))
    for _,r in x.iterrows():
        print(str(r.date)[:10], f"{r.amount:>11.2f}", '|', str(r.type)[:14], '|', str(r.num)[:9], '|', str(r['name'])[:22], '|', str(r.memo)[:90], '|', str(r.split)[:32])
for a in sys.argv[1:]: dump(a)
