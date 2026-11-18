import itertools
target=208100
bases={'QB/Mark 12/31/25 163,523.09':163523.09,'QB incl draw 168,853.89':168853.89,'Finaloop opening 237,886.89':237886.89}
comps={'+dist 21,752.30':21752.30,'+reimb(FL to 7/23) 27,640.33':27640.33,'+personal 923.50':923.50,'+unclassified 2,125.42':2125.42,
       '-contrib 3,830':-3830.0,'-clearing 6,033.40':-6033.40,'-clearing2 6,033.40':-6033.40,'-69,033':-69033.0,'-4,600':-4600.0}
res=[]
names=list(comps)
for bn,bv in bases.items():
    for r in range(0,len(names)+1):
        for c in itertools.combinations(names,r):
            if '-clearing2 6,033.40' in c and '-clearing 6,033.40' not in c: continue
            if '-69,033' in c and not bn.startswith('Finaloop'): continue
            v=bv+sum(comps[k] for k in c)
            res.append((abs(v-target),round(v,2),round(target-v,2),bn,c))
res.sort()
for x in res[:25]: print(x)
print()
# named natural hypotheses
H={
'H1 Finaloop balance at Jul 23 (226,743.59)':226743.59,
'H2 163,523.09 + distributions + reimbursements':163523.09+21752.30+27640.33,
'H3 H2 - contributions 3,830':163523.09+21752.30+27640.33-3830,
'H4 H3 + personal charges 923.50':163523.09+21752.30+27640.33-3830+923.50,
'H5 H4 - clearing 12,066.80':163523.09+21752.30+27640.33-3830+923.50-12066.80,
'H6 H4 - clearing 6,033.40':163523.09+21752.30+27640.33-3830+923.50-6033.40,
'H7 Finaloop Jul23 - 69,033 + dist + reimb':226743.59-69033+21752.30+27640.33,
'H8 163,523.09 + all cash to him/creditors 52,441.55 - contributions 3,830':163523.09+52441.55-3830,
'H9 163,523.09 + Finaloop net change (-11,143.30)':163523.09-11143.30,
'H10 163,523.09 + reimb only':163523.09+27640.33,
'H11 163,523.09 + dist only':163523.09+21752.30,
'H12 163,523.09 + Mark unallocated reimb 31,312 + dist 21,752.30 - contrib 3,830':163523.09+31312+21752.30-3830,
}
for k,v in H.items(): print(f"{k}: {v:,.2f}  residual (Mark - hyp) {target-v:,.2f}")
