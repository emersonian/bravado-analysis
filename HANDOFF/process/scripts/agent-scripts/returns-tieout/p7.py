exec(open('load.py').read())
import itertools
def search(target, cands, maxn=4, tol=1.0, must=None):
    names=list(cands); vals=[cands[n] for n in names]
    hits=[]
    for n in range(1,maxn+1):
        for idx in itertools.combinations(range(len(names)),n):
            for signs in itertools.product([1,-1],repeat=n):
                if signs[0]<0 and n>1 and all(s<0 for s in signs): continue
                s=sum(sg*vals[i] for sg,i in zip(signs,idx))
                if abs(s-target)<=tol:
                    hits.append((round(s,2),[(('+' if sg>0 else '-')+names[i], round(vals[i],2)) for sg,i in zip(signs,idx)]))
    return hits
y=2025
d=g[g.year==y]; s=d.groupby('account').amount.sum()
w=d[d.account=='73902 Salaries & Wages']
c={}
c['73902 total']=s['73902 Salaries & Wages']
c['Gusto wages']=w[w.num=='Gusto'].amount.sum()
c['AJE-547']=69033.00
for k in ['Regular Wages','Holiday Wages','Paid Time Off Time Off','Sick Time Off']:
    c['Gusto '+k]=w[w.memo==k].amount.sum()
c['73901 payroll taxes']=s['73901 Payroll Taxes']
c['73900 contractors']=s['73900 1099 Non-Employee Compensation']
c['73640 health ins']=s['73640 Insurance - Health']
c['80001 other misc income']=s['80001 Other Misc Income']
erc=d[(d.account=='80001 Other Misc Income')&((d.name=='United States Treasury')|(d.num=='AJE-380'))]
for _,r in erc.iterrows(): c[f'ERC {r.date.date()}']=r.amount
c['ERC total']=erc.amount.sum()
wd=d[d.account=='Wages Due to Jeremiah']
c['WagesDue debits 2025']=-wd[wd.amount<0].amount.sum()
c['WagesDue AJE-345']=2000.0; c['WagesDue AJE-387']=15915.89; c['WagesDue AJE-388']=5500.0
c['WagesDue net change']=wd.amount.sum()
c['WagesDue bal 2024']=107880.70; c['WagesDue bal 2025']=176913.70
c['33500 change']=-s['33500 Due to Jeremiah']
c['Jer draw 2025']=-s["53000 Jer's Draw"]
c['Nguyen loan repaid']=11233.0
for a in ['71100 Shipping & Delivery - COS','71200 Other Costs - COS','71300 Ingredients - COS','71400 Co-Packer - COGS','73100 Rent or Lease','73700 Professional Fees','73500 Dues & Subscriptions','Accrued Expense','31000 Accounts Payable','12000 Accounts Receivable']:
    c[a]=abs(s[a])
c['AP bal 2025']=170239.81; c['Accrued bal 2025']=5842.42
print(len(c),'candidates'); 
for k,v in c.items(): print(f'  {k}: {v:,.2f}')
for h in search(62919.0,c,maxn=3,tol=1.0): print(h)
print('--- 4-term, tol 0.6')
h4=search(62919.0,c,maxn=4,tol=0.6)
print(len(h4))
for h in h4[:80]: print(h)
