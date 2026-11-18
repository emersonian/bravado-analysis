from ld import *
pmt=100000*0.01/(1-1.01**-24); print('PMT 24mo 1%',round(pmt,2))
b=100000
for i in range(3):
    it=round(b*0.01,2); pr=4707-it; b-=pr; print(i+1,it,pr,b)
print('12 mo simple interest on 88767 at 1%/mo', 88767*0.01*12, '13 mo', 88767*0.01*13)
# wages due 2024
w=q[(q.account=='Wages Due to Jeremiah')]
for y in (2023,2024,2025):
    x=w[w.y==y]; print(y,'credits',round(x[x.amount>0].amount.sum(),2),'debits',round(x[x.amount<0].amount.sum(),2), 'n3125', round(x[(x.amount>0)&(x.type=='Journal Entry')&x.num.astype(str).str.startswith('AJE')].amount.sum()/3125.01,3))
print('69033/3125.01',69033/3125.01, '75000-69033',75000-69033)
# 33500 2025 JE credits/debits
x=q[(q.account=='33500 Due to Jeremiah')&(q.y==2025)&(q.type=='Journal Entry')]
print('33500 2025 JE credits',round(x[x.amount>0].amount.sum(),2),'debits',round(x[x.amount<0].amount.sum(),2), len(x[x.amount>0]))
for y in (2023,2024):
    x=q[(q.account=='33500 Due to Jeremiah')&(q.y==y)&(q.type=='Journal Entry')]
    print(y,'33500 JE credits',round(x[x.amount>0].amount.sum(),2),'debits',round(x[x.amount<0].amount.sum(),2))
r=f[f.account=='Reimbursements to owners']
print('reimb n',len(r),'round-100 n',(r.amount%100==0).sum(), 'sum round', r[r.amount%100==0].amount.sum())
card=r[r.Description.str.contains('PMT|Petal',case=False)]; print('reimb card pmts',round(card.amount.sum(),2),len(card),'transfers',round(r.amount.sum()-card.amount.sum(),2))
d=f[f.account=='Distributions - Jeremiah Tallerine']; print('dist', round(d.amount.sum(),2))
print('total 2026', 21752.30+27640.33+923.50+955.42+250+870+25+5)
# Finaloop AP change
ap=f[f.account.isin(['Inventory vendors - bills','Operational vendors - bills'])]
print('FL AP open',round(ap[ap.datetime_utc<'2026-01-01'].amount.sum(),2),'Jul23',round(ap.amount.sum(),2))
print('Mark AP change',204880-170240,' Mark RE move', -966646+974507, 63482-966646+974507+0, 'FL RE vs Mark', -903834.43+974507, ' FLRE+loss', -903834.43-63482)
print('Mark due-from minus wages 9/30', 208100-177063, ' FL', 226743.59-176913.70, 'FL ex 69033', 226743.59-69033-176913.70)
print('gross margin', 1-114771/243334, 1-314141/464997, 1-576381/805745, 'if inv 25844:', 1-(114771+59829-25844.42)/243334)
print('annualized sales', 243334*12/9, 'GP ann', 128563*12/9)
print('Jer share',7200/10700, 7000/10700)
print('SBA 4 x 1705', 4*1705)
