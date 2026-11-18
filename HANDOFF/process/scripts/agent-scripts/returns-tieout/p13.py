from datetime import date
from decimal import Decimal as Dm, getcontext
getcontext().prec=30
print((date(2024,7,22)-date(2024,1,1)).days,(date(2024,11,20)-date(2024,7,22)).days,(date(2024,11,26)-date(2024,11,20)).days,(date(2024,12,31)-date(2024,11,26)).days, 204+121+6+35)
parts=[(1000,10000,204),(1000,10000,121),(1000,10000,6),(1000,10700,35)]
tot=Dm(0)
for s,t,d in parts:
    p=Dm(s)/Dm(t)*Dm(d)/Dm(366)*100; tot+=p; print(s,t,d, round(p,5), p)
print('total',tot, 'sum of rounded',sum(round(Dm(s)/Dm(t)*Dm(d)/Dm(366)*100,5) for s,t,d in parts))
pct=Dm('9.93744')/100
for nm,v in [('ord loss',67869),('rental',17990),('gross receipts',862582),('wages 143825',143825),('wages 143826',143826),('UBIA 1320',1320),('loans from SH 100000',100000)]:
    print(nm, v, float(Dm(v)*pct))
print('14293/pct',float(Dm(14293)/pct), '6744/pct',float(Dm(6744)/pct),'1788/pct',float(Dm(1788)/pct),'85719/pct',float(Dm(85719)/pct))
print('7000/10700',7000/10700*100,'1000/10700',1000/10700*100,'7000/10000',70.0)
for j in (6900,6950,7000,7050,7100,7200): print(j, j/10700*100, j/10000*100)
# two Nguyens at 9.93744 each; remaining
print('100-2*9.93744=',100-2*9.93744)
# if 6 shareholders: Jer, James?, Hugh, Christy, Clark, ? 
# Comatri time-weighted if 300 sh (3%) from 7/22 of 10000 and 1000 of 10700 from 11/26
c=300/10000*(121+6)/366+1000/10700*35/366; print('Comatri/Blake hypothetical 300->1000',c*100)
c2=1000/10700*35/366; print('1000 from 11/26 only',c2*100)
