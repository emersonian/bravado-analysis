from common import *
import itertools
f=pd.read_pickle('fl_typed.pkl')
op=f[f.dt<'2026-01-01']
x=op[op.account.isin(['Inventory vendors - bills','Operational vendors - bills','Money in transit','Checking - Found - Primary 1862'])]
print(x[['account','amount','Source','Description']].to_string(index=False))
# F15 quick search
mark=208100
bases={'QB163523':163523.09,'FL_open':237886.89,'FL_open_less69033':168853.89, 'QB+draw':168853.89}
comp={'dist':21752.30,'reimb':27640.33,'contrib':-3830.0,'personal':923.50,'clear2':-12066.80,'clear1':-6033.40,'moneyout870':870.0,'citi':980.42,'chk7588':250.0,'chasecc':2255.45,'transit25':25.0}
hits=[]
for bn,bv in bases.items():
    for r in range(0,len(comp)+1):
        for c in itertools.combinations(comp,r):
            if 'clear1' in c and 'clear2' in c: continue
            v=bv+sum(comp[k] for k in c)
            if abs(v-mark)<=1000: hits.append((round(mark-v,2),bn,c))
hits.sort(key=lambda h:abs(h[0]))
print(len(hits)); 
for h in hits[:12]: print(h)
