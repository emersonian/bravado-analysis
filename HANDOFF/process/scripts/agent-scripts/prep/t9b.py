from ld import *
def show(x):
    for _,r in x.sort_values('datetime_utc').iterrows():
        print(str(r.datetime_utc)[:10], f"{r.amount:>10.2f}", '|', r.account[:45], '|', str(r.Source)[:32], '|', str(r.Description)[:100])
bank=f[f.account.str.startswith(('Checking','Savings'))]
print('== SBA bank lines'); show(bank[bank.Description.astype(str).str.contains('SBA',case=False)])
print('== Found account Apr 28 - May 12'); show(bank[(bank.account.str.contains('Found'))&(bank.datetime_utc>='2026-04-28')&(bank.datetime_utc<='2026-05-12')&(bank.amount.abs()>=150)])
# QB SBA payments 2025-2026
x=q[(q.account=='SBA Disaster Loan')]; print(x[['date','type','name','memo','amount']].to_string())
m=q.memo.astype(str).str.contains('SBA',case=False)&q.account.str.contains('Chase|Found')&(q.date>='2025-01-01')
print(q[m][['date','account','memo','split','amount']].to_string())
# outflows to founder accounts after May 1 in May
p=bank[(bank.datetime_utc>='2026-05-01')&(bank.datetime_utc<'2026-06-01')&bank.Description.astype(str).str.contains('5820|CAPITAL ONE|Petal|CITI CARD|APPLECARD|CHASE CREDIT',case=False)]
print('May outflows to personal accts/cards', round(p.amount.sum(),2)); show(p)
