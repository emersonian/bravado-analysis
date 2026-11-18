from ld import *
import sys
for a in sys.argv[1:]:
    x=f[f.account==a].sort_values('datetime_utc')
    print('\n==',a,len(x),round(x.amount.sum(),2))
    for _,r in x.iterrows():
        print(str(r.datetime_utc)[:16], f"{r.amount:>11.2f}", '|', str(r.Source)[:60], '|', str(r.Description)[-110:], '|', str(r['Transaction Classification'])[:40])
