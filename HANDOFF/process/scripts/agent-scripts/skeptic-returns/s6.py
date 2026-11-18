import pandas as pd, re
D='/tmp/claude-0/-home-user-bravado-analysis/73f84ad8-a4ee-55bd-a118-545c9fdbfe6c/scratchpad/data/'
g=pd.read_csv(D+'qb_gl.csv',parse_dates=['date']); g['y']=g.date.dt.year
bb=pd.read_csv(D+'qb_beginning_balances.csv',index_col=0).iloc[:,0]
A=sorted(g.account.unique())
def f(pat):
    m=[a for a in A if a.startswith(pat)]
    assert len(m)==1,(pat,m); return m[0]
def yr(y,*pats): return round(sum(g[(g.account==f(p))&(g.y==y)].amount.sum() for p in pats),2)
def bal(y,*pats): return round(sum(g[(g.account==f(p))&(g.y<=y)].amount.sum()+bb.get(f(p),0) for p in pats),2)
print('=== R2 2023')
y=2023
L=[('repairs 5081',yr(y,'76000')),('bad debts 333',yr(y,'74000')),('rents 122807',yr(y,'73100')),('taxes 32862',yr(y,'73901','73800')),('interest 64336',yr(y,'73450')),('benefits 15117',yr(y,'73640')),
('auto 378',yr(y,'Gas')),('bank 18151',yr(y,'73410','73420','73430','Melio Credit')),('dues 52345',yr(y,'73500')),('contractor 65251',yr(y,'73900')),('ins 6999',yr(y,'73600')),('liab 11740',yr(y,'73620')),('legal 44035',yr(y,'73700')),
('marketing 175002',yr(y,'72000','72100','72200','72300','72400','72500','72600','72601','72700','Slotting')),('meals 3981',round(yr(y,'73220')/2,2)),('misc 3582',yr(y,'75500','Remittance')),('office 15617',yr(y,'73200','73000','Reconciliation')),('postage 630',yr(y,'73210')),('travel 38646',yr(y,'75000')),('util 22387',yr(y,'73300','Electricity'))]
for a,b in L: print(a,b)
print('sum other ded',round(sum(b for a,b in L[6:]),2))
print('=== R2 2024'); y=2024
L=[('repairs 3196',yr(y,'76000')),('bad debts 9654',yr(y,'74000')),('rents 62248',yr(y,'73100','73110')),('taxes 1817',yr(y,'73901','73800')),('interest 39431',yr(y,'73450')),('benefits 10791',yr(y,'73640')),
('bank 33386',yr(y,'73400','73410','73420','73430','Faire Fees','Late Penalty','Melio Credit')),('dues 27911',yr(y,'73500')),('contractor 91815',yr(y,'73900')),('ins 3365',yr(y,'73600')),('liab 5437',yr(y,'73620')),('legal 47936',yr(y,'73700')),
('marketing 44441',yr(y,'72000','72100','72200','72300','72400','72500','72600','72601','Free fill','Slotting')),('misc 837',yr(y,'75500','Remittance')),('office 12280',yr(y,'73200','73210','73220')),('util 11446',yr(y,'73300','Electricity'))]
for a,b in L: print(a,b)
print('sum other ded',round(sum(b for a,b in L[6:]),2))
x=g[(g.account==f('Accrued Expense'))]; print(x[['date','type','num','memo','split','amount']].to_string())
print('=== R2 2025'); y=2025
L=[('repairs 1982',yr(y,'76000')),('bad debts 849',yr(y,'74000')),('rents 30573',yr(y,'73100')),('taxes 12910',yr(y,'73901','73800')),('interest 15268',yr(y,'73450')),('advertising 11881',yr(y,'72000','72100','72200','72300','72500','72600')),
('bank 8478',yr(y,'73400','73410','73430','Faire Fees','Late Penalty','Merchant Fees','Melio services','Remittance')),('dues 24985',yr(y,'73500')),('contractor 19004',yr(y,'73900')),('ins 18095',yr(y,'73600','73620','73640')),('legal 58122',yr(y,'73700')),
('marketing 900',yr(y,'Charitable')),('office 9104',yr(y,'73200','73210','73220')),('travel 5369',yr(y,'72400','Gas')),('util 4184',yr(y,'73300'))]
for a,b in L: print(a,b)
print('sum other ded',round(sum(b for a,b in L[6:]),2))
print('bank w/o remit', yr(y,'73400','73410','73430','Faire Fees','Late Penalty','Merchant Fees','Melio services'))
